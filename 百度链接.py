from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

# dir=os.path.dirname(__file__)
# gecko_driver_path="./geckodriver.exe"
# driver=webdriver.Firefox(executable_path=gecko_driver_path)
# driver.get("http://www.baidu.com ")

# selen_tag=driver.find_elements_by_tag_name("a")
# for i in selen_tag:
#     print(i.text)
# driver.quit()

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
try:
    driver.get("http://www.baidu.com")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.switch_to.window(driver.current_window_handle)
    about_us=driver.find_element_by_link_text("关于百度")
    about_us.click()
    driver.switch_to.window(driver.current_window_handle)
    contection_us=driver.find_element_by_link_text("联系我们")
    contection_us.click()
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    email_list=driver.find_elements_by_class_name("mail-content-text")
    for i in email_list:
        str=i.text
        if "@" in str:
            print(str)
finally:
    driver.quit()
