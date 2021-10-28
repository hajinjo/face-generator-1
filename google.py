from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def get_img_google(search_name):
    # 드라이버 불러오기
    driver = webdriver.Chrome('./chromedriver') 
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")

    el = driver.find_element_by_name("q") 
    el.send_keys(str(search_name))
    el.send_keys(Keys.RETURN) 

    # 스크롤 끝까지 내리기
    print(" 스크롤중...........")
    elem = driver.find_element_by_tag_name("body") 
    for i in range(60): 
        elem.send_keys(Keys.PAGE_DOWN) 
        time.sleep(0.1) 
    try: 
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[4]/div[2]/input').click() 
        for i in range(60): 
            elem.send_keys(Keys.PAGE_DOWN) 
            time.sleep(0.1) 
    except: 
        pass

    # 이미지 주소 리스트 
    links=[]

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    for image in images:
        if image.get_attribute('src')!=None: 
            links.append(image.get_attribute('src')) 
            print(f'{search_name} 이미지 찾는 중 ... : {len(links)} 개') 
            time.sleep(2)

    print(search_name+' 총 이미지 개수:', len(links))

    # 검색한 이름으로 저장 폴더 생성 
    if not os.path.exists(search_name):
        print("저장 폴더 생성")
        os.mkdir(search_name)

    # 이름_번호 형태로 저장 
    for i, image in enumerate(links):
        url = image
        start = time.time()
        urllib.request.urlretrieve(url, f'./{search_name}/{search_name}_{i+1}.jpg')
        print(f'{i+1}/{len(links)} 다운로드중... Download time : {str(time.time() - start)[:5]} 초')

    driver.close()
    

if __name__=='__main__':

    search_name = "blond hair woman"
    get_img_google(search_name)

