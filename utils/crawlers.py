from abc import ABC, abstractmethod

import requests


class Crawler(ABC):
    @abstractmethod
    def search(self, keyword: str) -> list:
        pass

    @abstractmethod
    def download(self, keyword, path) -> None:
        pass


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


if __name__ == "__main__":
    # Tests
    pass
