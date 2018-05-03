import re
import os
import json
import codecs
from time import sleep

import scrapy

import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class baidu(scrapy.Spider):
    name = 'baidu2'
    # 처음 검색 페이지가 scrapy에서 로드가 안되서 music으로 로드한 후 selenium에서 각각의 검색어 별로 이동
    start_urls = ['http://music.baidu.com/']
    # start_urls = ['http://www.baidu.com/']

    maximum_page = 101

    # def __init__(self):
    #     self.set_driver()

    def parse(self, response):
        print(response.url)
        yield scrapy.Request(url='https://www.baidu.com/', callback=self.ttt)

        # self.load_page()

    def ttt(self,response):
        print(response.url)
        print(response.xpath('//*[@id="lg"]/img[1]/@src').extract_first())

    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument(
        #     '--user-agent=Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)')
        # chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)
        # self.driver.set_page_load_timeout(20)

    def load_page(self):
        keyword = [
            'samsung', 'asic'
        ]
        for word in keyword:
            self.get_data_elements_go_next_page(word)

        self.driver.close()

    def get_data_elements_go_next_page(self, word):
        raw_url = 'https://www.baidu.com/s?'
        print(word)

        for page_num in range(0, self.maximum_page):
            print(page_num)
            made_url = raw_url + 'wd={}&pn={}0'.format(word, str(page_num))
            print(made_url)
            self.driver.get(made_url)
            data_elements = self.driver.find_elements_by_xpath('//div[@id="content_left"]/div/h3/a')
            data_href = [ind.get_attribute('href') for ind in data_elements]
            now_page_num = int(self.driver.find_element_by_xpath('//*[@id="page"]/strong/span[2]').text)

            for url in data_href:
                self.load_data(url)
            sleep(1)
            self.driver.get(made_url)

            next_page = self.driver.find_element_by_xpath('//*[@id="page"]/a[@class="n"]')
            href = next_page.get_attribute('href')
            print(href)
            if now_page_num > self.maximum_page:
                return 0
                # raise Exception
            # try:
            #     next_page = self.driver.find_element_by_xpath('//*[@id="page"]/a[@class="n"]')
            #     href = next_page.get_attribute('href')
            #     print(href)
            #     if now_page_num > self.maximum_page:
            #         raise Exception
            # except:
            #     print('boom!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #     return 0
            sleep(1)

    def load_data(self, url):
        print(url)
        regax = re.compile('(19|20)\d+(-|.|/|)\d+(-|.|/|)\d+')
        try:
            self.driver.get(url)
            self.driver.set_page_load_timeout(20)
            body = self.driver.find_element_by_tag_name('body').text
            if regax.findall(body):
                file = open('check.txt', 'a')
                file.write(url + '\n')
        except Exception as ex:
            error_file = open('not_open.txt', 'a')
            error_file.write(str(ex))
            error_file.write(url + '\n')
