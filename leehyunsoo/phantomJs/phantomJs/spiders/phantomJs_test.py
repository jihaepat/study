import scrapy
from selenium import webdriver
from ghost import G


class PhanteomJsTest(scrapy.Spider):
    name = 'phantom'
    start_urls = ['http://sbgg.saic.gov.cn:9080/tmann/annInfoView/homePage.html']

    def __init__(self):
        # self.driver = webdriver.PhantomJS('/home/leehyunsoo/4TB/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        self.driver = webdriver.PhantomJS('/home/leehyunsoo/4TB/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')



    # def start_requests(self):
    #     yield

    def parse(self, response):
        self.driver.get(response.url)
        print(self.driver.find_elements_by_xpath('//tr[@class="odd_bg"]/td[1]'))
        self.driver.close()
