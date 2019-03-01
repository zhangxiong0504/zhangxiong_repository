from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

dir=os.path.dirname(__file__)
chrom_driver_path=dir+"/chromedriver.exe"
driver=webdriver.Chrome(chrom_driver_path)
try:
    #超长等待5秒
    driver.implicitly_wait(5)
    driver.get("http://www.baidu.com ")
    #激活当前页面
    driver.switch_to.window(driver.current_window_handle)
    #输出控制台信息
    print("百度首页已打开",driver.title)
    #找搜索框  输入java
    selen_name=driver.find_element_by_id("kw")
    selen_name.send_keys("java")
    selen_name.submit()
    #获得页面中的百度为您找到相关结果约39,600,000个
    selen_nums=driver.find_element_by_class_name("nums")
    #打印百度为您找到相关结果约39,600,000个
    print("-------",selen_nums.text)
    #激活页面
    driver.switch_to.window(driver.current_window_handle)

    wait_second=10
    driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(selen_nums.text.replace("\n", "$"),wait_second))
    time.sleep(wait_second)
finally:
    driver.quit()