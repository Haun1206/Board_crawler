from selenium import webdriver
import time
import pandas as pd
import json
# from bs4 import BeautifulSoup

options= webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
# options.add_argument("--headless")

wd = webdriver.Chrome('./chromedriver.exe', options=options)
wd.get("https://velog.io/@oneook")

result = []

for index in range(3):
    sub_result = {}
    
    writing = wd.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div[4]/div[3]/div/div[{0}]'.format(index+1))
    term = writing.find_elements_by_css_selector("a")
    img = term[0].find_element_by_css_selector("div > img")
    title = term[1]
    summary = writing.find_element_by_css_selector("p")
    
    sub_result['title'] = title.text
    sub_result['summary'] = summary.text
    sub_result['link'] = title.get_attribute('href')
    sub_result['img_link'] = img.get_attribute('src')
    
    
    title.click()
    time.sleep(1) ## velog는 페이지 여는 속도가 비교적 좀더 느림
    
    content = wd.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div')
    sub_result['content'] = content.text

    result.append(sub_result)
    wd.back()
    time.sleep(1)

wd.quit()
    
with open("data/velog.json", "w", encoding='UTF-8') as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))





