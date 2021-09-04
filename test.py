# BeautifulSoup 써서 더 간편하게 해보기
from selenium import webdriver
from bs4 import BeautifulSoup
import time

options= webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")

wd = webdriver.Chrome('./chromedriver.exe', options=options)
wd.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259")

html = wd.page_source
soup = BeautifulSoup(html, 'html.parser')

result = []
news1 = wd.find_elements_by_css_selector("#main_content > div.list_body.newsflash_body > ul.type06_headline > li")
news2 = wd.find_elements_by_css_selector("#main_content > div.list_body.newsflash_body > ul.type06 > li")
for content in news1:
    title = content.find_element_by_css_selector("dl > dt:not(.photo) > a")
    summary = content.find_element_by_css_selector("dl > dd > span.lede")

    result.append([title.text, summary.text])

wd.quit()
