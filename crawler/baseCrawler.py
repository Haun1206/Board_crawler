from selenium import webdriver

class baseCrawler():
    def __init__(self, url, numPosts) -> None:
        self.url = url
        self.numPosts = numPosts
        
        options= webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")

        self.wd = webdriver.Chrome("./chromedriver", options=options)
        self.wd.get(url)
    
    def crawl(self):
        pass