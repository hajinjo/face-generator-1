from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from random import normalvariate
from selenium.webdriver.common.by import By 
import urllib.request
from time import sleep
import os

class PinterestScraper(object):
    # 크롬드라이버 경로 설정 
    def __init__(self, login_name, login_pass, chromedriver_path='./chromedriver'):
        self.login_name = login_name
        self.login_pass = login_pass
        try:
            self.driver = webdriver.Chrome() 
        except WebDriverException:
            self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.get("https://www.pinterest.com")
        self.path = ''

        self.driver.implicitly_wait(2)

    # 로그인 하는 함수 
    def login(self):
        try:
            path = '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button'
            login_elem = self.driver.find_element(By.XPATH, path)
            login_elem.send_keys(Keys.ENTER)
            sleep(abs(normalvariate(3, 0.2)))
            email_elem = self.driver.find_element_by_name('id')
            email_elem.send_keys(self.login_name)
            sleep(abs(normalvariate(3, 0.2)))
            pw_elem = self.driver.find_element_by_name('password')
            pw_elem.send_keys(self.login_pass)
            sleep(abs(normalvariate(3, 0.2)))
            login_elem = self.driver.find_element_by_class_name('SignupButton')
            login_elem.send_keys(Keys.RETURN)
        except NoSuchElementException:
            sleep(abs(normalvariate(3, 0.2)))
            email_elem = self.driver.find_element_by_name('id')
            email_elem.send_keys(self.login_name)
            sleep(abs(normalvariate(3, 0.2)))
            pw_elem = self.driver.find_element_by_name('password')
            pw_elem.send_keys(self.login_pass)
            sleep(abs(normalvariate(3, 0.2)))
            login_elem = self.driver.find_element_by_class_name('SignupButton')
            login_elem.send_keys(Keys.ENTER)

    def set_destination_folder(self, path):
        if not os.path.exists(path):
            print("저장 폴더 생성")
            os.mkdir(path)
        self.path = path

    def scrape_pictures(self, query, n_pgdn=2):

        if ' ' in query:
            query.replace(' ', '  ')  # Pinterest likes to bring up a history
                                      # instead of letting you type your first space
        search_input = self.driver.find_element(By.NAME, 'searchBoxInput') # searchInput에서 변경 
        search_input.send_keys(query)

        search_input = self.driver.find_element(By.NAME, 'searchBoxInput')
        search_input.send_keys(Keys.RETURN)

        sleep(2) 

        # 한번에 가져올 수 있는 링크 수 한계있음 
        # 스크롤해서 페이지 바꾸고 새로운 링크 받아서 저장하기 반복 횟수 설정 
        refresh_num = 30
        for num in range(refresh_num):
            print(num, '번째 스크랩 중..')

            # 스크롤 하기 
            body = self.driver.find_element_by_css_selector('body')
            scroll_num = 3
            print("스크롤 중.....")
            n=1
            for j in range(scroll_num):
                body.send_keys(Keys.PAGE_DOWN)
                print("스크롤 중 : ", n)
                n += 1
                sleep(1) 
            
            sleep(5)

            # 이미지 주소 찾기 
            pics_list = self.driver.find_elements(By.XPATH, "//div[contains(@data-test-id, 'image')]/div/img[@srcset]")
            src_elem= [] 
            url_list = []

            # srcset : 4가지 사이즈별 주소가 전부 들어있음 
            for elem in pics_list:
                src_elem.append(elem.get_attribute("srcset"))

            # 4가지 사이즈중 original 사이즈 이미지 주소만 저장 
            for origin in src_elem:
                url_list.append(origin.split()[-2])
            url_list = list(set(url_list))
            print(url_list)

            # 이름_번호 형태로 저장 
            for i, image in enumerate(url_list):
                path_name = image.split('/')[-1]
                urllib.request.urlretrieve(image, f'./{query}/{path_name}') 
                print(f'{i+1}/{len(url_list)} 다운로드중... ')
            
        self.driver.close()

def main():

    # 핀터레스트 로그인 아이디, 패스워드 
    id = ""
    password = ""
    # 검색할 키워드 
    keyword = "apple"

    my_scraper = PinterestScraper(login_name=id, login_pass=password)
    my_scraper.set_destination_folder(os.path.join(os.curdir, keyword)) # 키워드로 폴더 생성 
    my_scraper.login()
    sleep(2.2)
    my_scraper.scrape_pictures(keyword)

if __name__ == "__main__":
    main()
