import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


URL = 'https://shopping.naver.com/home/p/index.naver'
검색어 = "키오시아 EXCERIA M.2 NVMe"
print("aaa")
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)
print(driver.current_url)

inputElement = driver.find_element(By.XPATH,"//*[@id='autocompleteWrapper']/input[1]")
inputElement.send_keys(검색어)

# 대기
sleep(3)
driver.close()




