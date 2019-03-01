import os
from selenium import webdriver

dir=os.path.dirname(__file__)
ie_driver_path="./IEDriverServer.exe"
driver=webdriver.Ie(ie_driver_path)
driver.get("http://www.baidu.com")
assert "百度" in driver.title