from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup

def implement():
    ## driver 준비
    options= webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    # options.add_argument("--headless")

    wd = webdriver.Chrome('./chromedriver.exe', options=options)
    wd.get("https://velog.io/@oneook")

    result = []

    for index in range(1):
        sub_result = []
        
        writing = wd.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[4]/div[3]/div/div[{0}]'.format(index+1))
        term = writing.find_elements_by_css_selector("a")
        img = term[0].find_element_by_css_selector("div > img")
        title = term[1]
        summary = writing.find_element_by_css_selector("p")
        
        sub_result.append(title.text)
        sub_result.append(summary.text)
        sub_result.append(img.get_attribute('src'))
        
        
        title.click()
        
        content = wd.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div')
        sub_result.append(content.text)

        wd.back()
        time.sleep(1)
    
    wd.quit()
    return result

print(implement()[0])






