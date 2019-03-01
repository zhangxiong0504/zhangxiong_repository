from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
driver.get("http://www.baidu.com")
assert "baidu" in driver.title

elem = driver.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.ENTER)

