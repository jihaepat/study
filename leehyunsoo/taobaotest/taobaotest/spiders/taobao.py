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
    allowed_domains = ['taobao.com']

    def start_requests(self):
        base_url = 'https://world.taobao.com/?spm=a21bo.7723600.8453.1.3b755ec9DLWebP'
        yield scrapy.Request(base_url,callback=self.parse)


    def parse(self, response):
        print(response.url)
