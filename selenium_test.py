import selenium

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


#네이버쇼핑
URL = 'https://shopping.naver.com/home/p/index.naver'
검색어 = "푸디파이 85g"
업체명 = "뉴런렙타일"
print(URL)
print(검색어)


i = 0
while i <= 1:
    i = i + 1
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)

    # 텍스트박스 입력
    inputElement = driver.find_element(By.XPATH, "//*[@id='autocompleteWrapper']/input[1]")
    inputElement.send_keys(검색어)

    # 검색버튼 클릭
    searchElement = driver.find_element(By.XPATH, "//*[@id='autocompleteWrapper']/a[2]")
    searchElement.click()
    sleep(2)

    # 리스트 클릭
    listElement = driver.find_element(By.XPATH,
                                      "//*[@id='__next']/div/div[2]/div/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[3]/div/a")
    listElement.click()
    sleep(2)
    
    # 업체 클릭

    storeElement = driver.find_element(By.XPATH, "//a[contains(text(), '와우펫x창조')]")
    storeElement.click()

    sleep(5)

    driver.close()




#브라우저 로딩 타임아웃 1분
# driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
#웹브라우저 창 사이즈
# driver.manage().window().setSize(Dimension(1024, 768));


#
# #텍스트박스 입력
# inputElement = driver.find_element(By.XPATH,"//*[@id='autocompleteWrapper']/input[1]")
# inputElement.send_keys(검색어)
#
# sleep(3)
#
# #검색버튼 클릭
# searchElement = driver.find_element(By.XPATH,"//*[@id='autocompleteWrapper']/a[2]")
# searchElement.click()
#
# sleep(3)
#
# listElement = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/div/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[3]/div/a")
# listElement.send_keys(Keys.SHIFT + Keys.RETURN)
#
# sleep(10)
#
# driver.close()






