from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")

driver.execute_script("windows.alert('第一个弹出框')")
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
