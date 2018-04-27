import scrapy
from time import sleep
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ch_TM_image.items import ChTmImagePipeline
from selenium import webdriver

class ch_imgage_crawl(scrapy.Spider):
    name = 'crawl'

    chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/homePage.html')
    end_page = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]')
    end_page = int(end_page.text[1:-1])

    def start_requests(self):
        for i in range(self.end_page):
            print (self.driver)
