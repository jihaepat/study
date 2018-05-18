import scrapy
import os
import json
import codecs

from jdsbcn.items import JdsbcnItem


class JDSBSpider(scrapy.Spider):
    name = "jdsb"
    start_url = 'http://www.jdsb.cn/brands_list----------.html'

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.move_page_url)

    def move_page_url(self, response):
        last_page_href = response.xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/a[7]/@href').extract_first()
        last_page_num = int(last_page_href.split('=')[-1])

        print(last_page_num)
        for count in range(1, last_page_num + 1):
            yield scrapy.Request(url=(self.start_url + '?page=' + str(count)), callback=self.get_data_url)

    def get_data_url(self, response):
        raw_url = 'http://www.jdsb.cn/'
        data = response.xpath('//*[@id="main-nav-holder"]/div/div/ul/li/div/div[2]/a/@href').extract()
        make_data_url = [(raw_url + data_url) for data_url in data]
        for data_url in make_data_url:
            yield scrapy.Request(url=data_url, callback=self.crawling_data)

    def crawling_data(self, response):
        print(response.url)

        item = JdsbcnItem()
        item['brand_name'] = response.css('tr.sb_value:nth-child(4) > td:nth-child(1)::text').extract_first()
        item['category'] = response.css('tr.sb_value:nth-child(2) > td:nth-child(2)::text').extract_first()
        item['expiration_date'] = response.css('tr.sb_value:nth-child(6) > td:nth-child(2)::text').extract_first()
        item['ID'] = response.css('tr.sb_value:nth-child(2) > td:nth-child(1)::text').extract_first()
        item['img_url'] = response.xpath('//table[@class="img_part_table"]//img/@src').extract()

        yield item
