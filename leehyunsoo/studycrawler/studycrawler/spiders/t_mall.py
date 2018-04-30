import re
import os
import json
import codecs
from time import sleep

import scrapy

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Tmall(scrapy.Spider):
    name = 'tmall'
    start_url = 'https://www.tmall.com/'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        print(123123)
        print(response.xpath('//*[@id="J_FloorTMGJ"]/div[2]/div[2]/div[2]/a[1]/div/img/@src').extract_first())
