from google_images_download import google_images_download

# api 사용법 : 깃 클론 후 pip install  
# git clone https://github.com/Joeclinton1/google-images-download.git
# pip install git+https://github.com/Joeclinton1/google-images-download.git

def get_img_google(keyword, limit=100):
    # 크롬드라이버 다운받아서 위치 지정해주면 100장 제한 이상으로 크롤링 가능 
    chromedriver = './chromedriver' 

    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword,
                "limit": limit, 
                "format":"jpg",
                "type" : "face",
                "chromedriver" : chromedriver}
    paths = response.download(arguments)
    print(paths)

if __name__=='__main__':
    # 키워드만 변경해서 넣어주면 ./download/키워드명 으로 저장 
    keyword = "apple"
    get_img_google(keyword, 10)
