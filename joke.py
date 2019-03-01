from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.qiushibaike.com/hot/")
current=driver.find_element_by_css_selector(".current")
page_list=driver.find_elements_by_css_selector(".page-numbers")
for i in page_list:
    maxpage=0
    if maxpage<int(i.text):
        maxpage=int(i.text)
for j in range(0,maxpage):
    author=driver.find_elements_by_css_selector(".author a h2")
    content=driver.find_elements_by_css_selector(".content")
    num=driver.find_elements_by_css_selector(".stats-vote")
    pinglun=driver.find_elements_by_css_selector(".stats-comments a")
    print("第%d页有%d个笑话" % (j+1, len(author)))
    for i in range(0,len(author)):
        print("作者：",author[i].text,"\n内容:",content[i].text,"\n",num[i].text,pinglun[i].text)
    next=driver.find_element_by_css_selector(".next")
    next_text=driver.find_element_by_link_text(next.text)
    next_text.click()