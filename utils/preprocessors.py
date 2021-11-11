from io import BytesIO

import requests
from PIL import Image


class Preprocessor:
    def get_face(self, img: bytes) -> tuple:
        raise NotImplementedError

    def crop(self, img: bytes, area: tuple) -> bytes:
        im = Image.open(BytesIO(img))
        cropped = im.crop(area)
        buffer = BytesIO()
        cropped.save(buffer, "JPEG")
        return buffer.getvalue()

    def resize(self, img: bytes, resolution: int) -> bytes:
        im = Image.open(BytesIO(img))
        im = im.resize((resolution, resolution), Image.ANTIALIAS)
        buffer = BytesIO()
        im.save(buffer, "JPEG")
        return buffer.getvalue()


class NaverPreprocessor(Preprocessor):
    FACE_API = "https://openapi.naver.com/v1/vision/face"

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.headers = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
        }
        self.s = requests.Session()

    def __del__(self):
        self.s.close()

    def get_face(self, img: bytes) -> tuple:
        r = self.s.post(
            NaverPreprocessor.FACE_API, files={"image": img}, headers=self.headers
        ).json()

        if r['info']['faceCount'] == 0:
            raise Exception("No Face Found")
        if r['info']['faceCount'] > 1:
            print("WARNING: Does Not Support Multiple Faces, returning only 1.")
        
        roi = r['faces'][0]['roi']
        x, y, w, h = roi['x'], roi['y'], roi['width'], roi['height']

        margin = 100

        return (x-margin, y-margin-25, x+w+margin, y+h+margin-25)

if __name__ == "__main__":
    # Tests
    pass