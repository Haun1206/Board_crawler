from selenium import webdriver
import time
import pandas as pd
import openpyxl
#from bs4 import BeautifulSoup


def implement():
    options= webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")

    wd = webdriver.Chrome('./chromedriver.exe', options=options)
    wd.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259")


    result = []
    # news1 = wd.find_elements_by_css_selector("#main_content > div.list_body.newsflash_body > ul.type06_headline > li")
    # news2 = wd.find_elements_by_css_selector("#main_content > div.list_body.newsflash_body > ul.type06 > li")
    for index in range(3):
        sub_result = []
        nlist = wd.find_element_by_css_selector('#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child({0})'.format(index+1))
        title = nlist.find_element_by_css_selector("dl > dt:not(.photo) > a")
        summary = nlist.find_element_by_css_selector("dl > dd > span.lede")
        sub_result.append(title.text)
        sub_result.append(summary.text)
        title.click()
        
        ## 기사 내용 페이지
        content = wd.find_element_by_css_selector("#articleBodyContents")
        img =  wd.find_element_by_css_selector("#articleBodyContents > span.end_photo_org > img") ##image.get_attribute('src')
        sub_result.append(img.get_attribute('src'))

        img_scr = wd.find_element_by_css_selector("#articleBodyContents > span.end_photo_org > em")
        summary_2 =  wd.find_element_by_css_selector("#articleBodyContents > strong")

        all_text = content.text
        summary_text = summary_2.text
        img_text = img_scr.text

        content_text = all_text.replace(summary_text, '').replace(img_text, '')
        
        sub_result.append(summary_text)
        sub_result.append(img_text)
        sub_result.append(content_text)
        result.append(sub_result)
        
        wd.back()
        time.sleep(1)
    wd.quit()

    return result

# print(implement()[0])



