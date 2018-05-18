import scrapy
from time import sleep
from selenium import webdriver
import json
import codecs
from selenium.webdriver.common.keys import Keys


class Spider86sb(scrapy.Spider):
    name = '86sb'
    start_url = 'http://www.86sb.com/products/list'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.load_page)

    def load_page(self, response):

        sleep(1)

        total_page_num = int(''.join(
            filter(str.isdigit, (response.xpath('//*[@id="page_numbers"]/li[11]/span[1]/text()').extract_first()))))
        print(total_page_num)

        made_url = [
            self.start_url + '?tt=0&bt=&orderby=sort%7Cdesc%2Cup_at%7Cdesc&is_index=1&cg=' + str(num) + '#listfirst'
            for num in range(1, total_page_num + 1)]

        for page_url in made_url:
            yield scrapy.Request(url=page_url, callback=self.load_data)


    def load_data(self, response):
        print('load_data')
        sleep(1)
        page_data = [path.get_attribute('href') for path in
                     response.xpath('//*[@id="listfirst"]/dl/dd/a/@href').extract()]
        print(page_data)
        for url in page_data:
            yield scrapy.Request(url=url, callback=self.parse)
        print(page_data)

    def parse(self, response):
        print('parse')
        sleep(1)
        # brand_name = self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/h1')
        # ID = self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[2]/ul/li[2]/p[2]/span')
        # image_src = self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img')
        # data = {
        #     'brand_name': brand_name.text,
        #     'ID': ID.text,
        #     'image_src': image_src.text
        # }
