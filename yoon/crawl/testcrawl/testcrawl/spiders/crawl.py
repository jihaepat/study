import scrapy
import sys
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from testcrawl.items import TestcrawlItem
from scrapy.http import  Request
from scrapy.selector import Selector

class test_spider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.apt2you.com']
    start_urls = ['http://www.apt2you.com/houseSaleSimpleInfo.do']

    def parse(self, response):
        hxs = Selector(response)
        selects = []
        selects = hxs.xpath('//tbody[@class="line"]/tr')
        items = []
        for sel in selects:
            item = TestcrawlItem()
            item['aptname'] = sel.xpath('th[@scope="row"]/a[@href="#none"]/text()').extract()  # 주택명 추출
            item['link'] = sel.xpath('th[@scope="row"]/a/@onclick').re('\d+')  # 링크 추출
            item['link'][0] = "http://www.apt2you.com/houseSaleDetailInfo.do?manageNo=" + item['link'][0]  # 전체링크주소구성
            item['company'] = sel.xpath('td[1]/text()').extract()  # 건설업체 추출
            item['receiptdate'] = sel.xpath('normalize-space(td[2]/text())').extract()  # 청약기간 추출
            item['result_date'] = sel.xpath('td[@class="end"]/text()').extract()  # 당첨자발표일 추출
            items.append(item)  # Item 1개 세트를 리스트에 담음
        return items