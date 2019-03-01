from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
try:
    driver.implicitly_wait(20)
    driver.get("http://127.0.0.1/forum.php.")

    name=driver.find_element_by_name("username")
    name.send_keys("admin")
    pwd=driver.find_element_by_name("password")
    pwd.send_keys("zx980504")
    login=driver.find_element_by_css_selector(".fastlg_l .pn")
    login.click()
    time.sleep(10)
    mod=driver.find_element_by_css_selector(".fl_tb tr td h2 a")
    mod.click()

    menu = driver.find_element_by_xpath("//div[@id='pgt']/a")
    time.sleep(10)
    hidden_submenu = menu.find_element_by_xpath("//ul[@id='newspecial_menu']/li/a")
    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

    title=driver.find_element_by_name("subject")
    title.send_keys("hello")

    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    text_input=driver.find_element_by_tag_name("body")
    text_input.send_keys("hello")

    driver.switch_to.window(driver.current_window_handle)
    post_table=driver.find_element_by_id("postsubmit")
    post_table.click()

    reply=driver.find_element_by_id("post_reply")
    reply.click()

    driver.switch_to.window(driver.current_window_handle)
    area=driver.find_element_by_id("postmessage")
    area.send_keys("hello")
    driver.switch_to.window(driver.current_window_handle)
    reply_add=driver.find_element_by_id("postsubmit")
    reply_add.click()
    driver.switch_to.window(driver.current_window_handle)
    logout=driver.find_element_by_link_text("退出")
    logout.click()


finally:
    time.sleep(10)
    driver.quit()
