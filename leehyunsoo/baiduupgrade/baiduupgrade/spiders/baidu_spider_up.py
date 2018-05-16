import re
import os
import json
import codecs
import datetime
import time
from time import sleep

import scrapy


regax = re.compile(r'[1|2][9|0]\d\d[-|.|/|\w]\d\d[-|.|/|\w]\d\d')


class Baidu(scrapy.Spider):
    name = 'baidu'

    base_url = 'https://www.baidu.com/s?'
    maximum_page = 1

    key_word = ['asics', '明朗热狗']

    end_date = '20180501'

    def start_requests(self):
        made_url = [self.base_url + 'wd={}&'.format(word) for word in self.key_word]
        for url in made_url:
            key_word = self.key_word[made_url.index(url)]
            for page_num in (0, self.maximum_page):
                yield scrapy.Request(url=url + '&pn={}0'.format(str(page_num)),
                                     meta={'keyword': key_word},
                                     callback=self.load_data)

    def load_data(self, response):
        print('load_data')
        data_href = response.xpath('//div[@id="content_left"]/div/h3/a/@href').extract()
        for href in data_href:
            yield scrapy.Request(url=href,
                                 meta={'keyword': response.meta['keyword']},
                                 callback=self.parse)

    def parse(self, response):
        print(response.url)
        print('++++++++++++++++++++++',response.meta['keyword'])
