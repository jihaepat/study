import re
import os
import json
import codecs
import datetime
import time
from time import sleep

import scrapy

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException


class Taobao(scrapy.Spider):
    name = 'taobao'
    # 처음 검색 페이지가 scrapy에서 로드가 안되서 music으로 로드한 후 selenium에서 각각의 검색어 별로 이동
    start_urls = ['http://music.baidu.com/']


    def parse(self, response):
        self.load()

    def load(self):
        self.driver = webdriver.Firefox(executable_path='/home/leehyunsoo/4TB/geckodriver/geckodriver')
        self.driver.get('https://www.taobao.com/?spm=a230r.1.0.0.2f1376c9k7NADM')