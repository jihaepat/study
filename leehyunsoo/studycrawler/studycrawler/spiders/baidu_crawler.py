import re
import os
import json
import codecs
from time import sleep

import scrapy

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class baidu(scrapy.Spider):
    name = 'baidu'
    # 처음 검색 페이지가 scrapy에서 로드가 안되서 music으로 로드한 후 selenium에서 각각의 검색어 별로 이동
    start_urls = ['http://music.baidu.com/']

    maximum_page = 100

    def __init__(self):
        self.set_driver()

    def parse(self, response):
        self.load_page()

    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument(
        #     '--user-agent=Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)')
        # chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)

    def load_page(self):
        keyword = [
            'sulbing','skII','asic'
        ]
        for word in keyword:
            self.get_data_elements_go_next_page(word)

        self.driver.close()

    def get_data_elements_go_next_page(self, word):
        raw_url = 'https://www.baidu.com/s?'
        print(word)

        for page_num in range(0, 100):
            print(page_num)
            made_url = raw_url + 'wd={}&pn={}0'.format(word, str(page_num))
            print(made_url)
            self.driver.get(made_url)
            data_elements = self.driver.find_elements_by_xpath('//div[@id="content_left"]/div/h3/a')
            data_href = [ind.get_attribute('href') for ind in data_elements]
            now_page_num = int(self.driver.find_element_by_xpath('//*[@id="page"]/strong/span[2]').text)

            for url in data_href:
                self.load_data(url)
            self.driver.get(made_url)

            try:
                next_page = self.driver.find_element_by_xpath('//*[@id="page"]/a[@class="n"]')
                href = next_page.get_attribute('href')
                print(href)
                if now_page_num > self.maximum_page:
                    raise Exception
            except:
                return 0
            sleep(1)

    def load_data(self, url):
        print(url)
        regax = re.compile('(19|20)\d+(-|.|/|){1}(\d)(-|.|/|){1}(\d)')
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(3)
            body = self.driver.find_element_by_tag_name('body').text
            if regax.findall(body):
                file = open('check.txt', 'a')
                file.write(url + '\n')
        except :
            error_file = open('not_open.txt', 'a')
            error_file.write(url+'\n')
