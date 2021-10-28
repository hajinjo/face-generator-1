import requests
import os


API_URL = "https://openapi.naver.com/v1/search/image"

auth_headers = {
    "X-Naver-Client-Id": "",  # <---Client-Id
    "X-Naver-Client-Secret": "",  # <---Client-Secret
}


def get_file_ext(img_url):
    """URL에서 이미지 확장자(jpg, png 등)를 리턴"""
    ext = img_url.split(".")[-1]
    if "?" in ext:
        return ext.split("?")[0]
    return ext


def get_links(keyword, long=False):
    """Naver API를 이용해 검색된 이미지 URL을 리턴"""
    init_r = requests.get(
        API_URL, params={"query": keyword, "display": 100}, headers=auth_headers
    ).json()
    print(f"Searching {keyword}, Found Total {init_r['total']}!")
    urls = [x["link"] for x in init_r["items"]]
    if long and init_r["total"] > 100:
        with requests.Session() as s:
            for start in range(2, 11):  # max 1000
                r = s.get(
                    API_URL,
                    params={"query": keyword, "display": 100, "start": start},
                    headers=auth_headers,
                ).json()
                urls.extend([x["link"] for x in init_r["items"]])

    return urls


def download_imgs(keyword, limit=100):
    """이미지를 검색하여 원하는 개수만큼 저장한다 (기본값 100개, 최대 1000개)"""
    if limit > 100:
        urls = get_links(keyword, True)
    else:
        urls = get_links(keyword)

    keyword = "_".join(keyword.split(" "))  # 띄어쓰기가 있는 경우 처리 (경로명으로 사용하기위해)

    with requests.Session() as s:
        for idx, url in enumerate(urls[:limit]):
            ext = get_file_ext(url)  # 파일 확장자(jpg, png 등)

            if ext not in ["jpg", "jpeg", "png"]:
                continue

            img = s.get(url).content

            os.makedirs(f"{keyword}", exist_ok=True)  # 디렉토리 생성

            with open(f"{keyword}/{keyword}_{idx+1}.{ext}", "wb") as f:
                f.write(img)
                print(
                    f"Saving {keyword}/{keyword}_{idx+1}.{ext}...[{idx+1}/{len(urls[:limit])}]",
                    end="\r",
                )

    print("\ndone!")


if __name__ == "__main__":
    download_imgs("apple", 10)
