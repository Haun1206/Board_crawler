from selenium import webdriver
import time
import json

import selenium

options= webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
# options.add_argument("--headless")

wd = webdriver.Chrome('./chromedriver.exe', options=options)
wd.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259")


result = []
# news1 = wd.find_elements_by_css_selector("#main_content > div.list_body.newsflash_body > ul.type06_headline > li")
# news2 = wd.find_elements_by_css_selector("#main_content > div.list_body.newsflash_body > ul.type06 > li")
for index in range(5):
    sub_result = {}
    nlist = wd.find_element_by_css_selector('#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child({0})'.format(index+1))
    title = nlist.find_element_by_css_selector("dl > dt:not(.photo) > a")
    summary = nlist.find_element_by_css_selector("dl > dd > span.lede")
    sub_result['title'] = title.text
    sub_result['summary'] = summary.text
    sub_result['link'] = title.get_attribute('href')

    title.click()
    
    content = wd.find_element_by_css_selector("#articleBodyContents")
    try:
        img =  wd.find_element_by_css_selector("#articleBodyContents > span.end_photo_org > img")
        sub_result['img_link'] = img.get_attribute('src')
    except selenium.common.exceptions.NoSuchElementException:
        sub_result['img_link'] = ""

    try:
        img_scr = wd.find_element_by_css_selector("#articleBodyContents > span.end_photo_org > em")
        img_text = img_scr.text
    except selenium.common.exceptions.NoSuchElementException:
        img_text = ""
        
    try:
       headline =  wd.find_element_by_css_selector("#articleBodyContents > strong")
       headline_text = headline.text
    except selenium.common.exceptions.NoSuchElementException:
       headline_text = ""

    all_text = content.text
    content_text = all_text.replace(headline_text, '').replace(img_text, '')
    
    sub_result['headline'] = headline_text
    sub_result['img_text'] = img_text
    sub_result['content'] = content_text

    result.append(sub_result)
    
    wd.back()
    time.sleep(1)
wd.quit()


with open("data/naver.json", "w", encoding='UTF-8') as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))