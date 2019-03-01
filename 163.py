from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
driver.get("https://mail.163.com/")
driver.switch_to.frame(0)
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
email_input=driver.find_element_by_name("email")
email_input.send_keys("805135162@163.com")
pwd_input=driver.find_element_by_name("password")
pwd_input.send_keys("123456")
login=driver.find_element_by_id("dologin")
login.click()