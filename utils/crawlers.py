import requests


class Crawler:
    def get_file_ext(self, url: str) -> str:
        ext = url.split(".")[-1]
        if "?" in ext:
            return ext.split("?")[0]
        return ext

    def search(self, keyword: str) -> list:
        raise NotImplementedError

    def download(self, keyword, dir) -> None:
        raise NotImplementedError


class NaverCrawler(Crawler):
    SEARCH_API = "https://openapi.naver.com/v1/search/image"

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
        }

    def search(self, keyword: str, limit=100) -> list:
        with requests.Session() as s:
            initial_response = s.get(
                NaverCrawler.SEARCH_API,
                headers=self.headers,
                params={"query": keyword, "display": 100, "filter": "large"},
            ).json()

            print(
                f"Searching \"{keyword}\", found total {initial_response['total']}, returning first {limit}!"
            )

            urls = [x["link"] for x in initial_response["items"]]

            if limit > 100:
                if limit > 1000:
                    print("!!! Maximum 1000 result available at once !!!")
                for start in range(2, 11):  # max 1000
                    r = s.get(
                        NaverCrawler.SEARCH_API,
                        headers=self.headers,
                        params={"query": keyword, "display": 100, "start": start},
                    ).json()

                    urls.extend([x["link"] for x in r["items"]])
        return urls

    def download(self, keyword, dir="download", limit=100) -> None:
        urls = self.search(keyword=keyword, limit=limit)

        with requests.Session() as s:
            for idx, url in enumerate(urls):

                ext = self.get_file_ext(url)
                if ext not in ["jpg", "jpeg", "png"]:
                    continue

                try:
                    img = s.get(url, timeout=2).content
                except Exception as e:
                    print(f"fail to download {idx}, skipping...")
                    continue

                print(f"\rSaving {url[:15]}... {idx+1}/{len(urls)}", end="")
                with open(f"{dir}/{keyword}_{idx+1}.{ext}", "wb") as f:
                    f.write(img)
        print(f'finish downloading to "{dir}"')


if __name__ == "__main__":
    # Tests
    pass
