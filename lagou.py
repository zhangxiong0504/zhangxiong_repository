from selenium import webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions  as ec
from  selenium.webdriver.support.wait import WebDriverWait
import time


driver=webdriver.Chrome("chromedriver.exe")
try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")

    window_list=driver.current_window_handle
    driver.switch_to.window(window_list)

    while True:
        n=1
        driver.implicitly_wait(5)
        jobs=driver.find_elements_by_css_selector(".item_con_list li")
        for job in jobs:
            job_click=job.find_element_by_css_selector(".p_top a span")
            job_click.click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            job_company=driver.find_element_by_css_selector(".company")
            job_name=driver.find_element_by_css_selector(".name")
            job_salary=driver.find_element_by_css_selector(".salary")

            print("公司名称：",job_company.text,"\n" ,"工作职位:",job_name.text,"\n","工作要求:",job_salary.text)
            driver.close()
            driver.switch_to.window(window_list)
        next_page=WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'.item_con_pager .pager_container > *:last-child')))
        next_page_class=next_page.get_attribute("class")
        if "pager_next_disabled" in next_page_class:
            break
        else:
            next_page.click()
            print("当前页%d页，共有%d个职位"%(n,len(jobs)))
            n+1
            time.sleep(3)
finally:
    time.sleep(5)
    driver.quit()