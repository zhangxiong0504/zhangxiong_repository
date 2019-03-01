import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dir=os.path.dirname(__file__)
gecko_driver_path="./geckodriver.exe"
driver=webdriver.Firefox(executable_path=gecko_driver_path)
driver.get("http://www.yahoo.com ")
assert "baidu" in driver.title

elem=driver.find_element_by_name("p")
elem.send_keys("selenumhq"+Keys.ENTER)
