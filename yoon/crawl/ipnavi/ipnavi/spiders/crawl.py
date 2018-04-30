import scrapy
import re
from ipnavi.items import IpnaviItem

class spider_url(scrapy.Spider):
    name = 'CR'
    """
    name = scrapy.Field()
    no = scrapy.Field()
    date = scrapy.Field()
    count = scrapy.Field()
    """

    def start_requests(self):
        yield scrapy.Request('https://www.ip-navi.or.kr/broker/listByBroker.navi', callback=self.search_end_num)

    def search_end_num(self, response):
        search_end_page_num = int(re.findall('\d+', str(response.xpath('//*[@id="contents"]/div[2]/div[2]/div/a[7]/@onclick').extract()))[0])
        for i in range(search_end_page_num):
            url = 'https://www.ip-navi.or.kr/broker/listByBroker.navi?pageNum={}&fDate=&tDate=&search_keyword='.format(i + 1)
            yield scrapy.Request(url, callback=self.crawl_page)

    def crawl_page(self, response):
        item = IpnaviItem()

        no_count = len(response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr'))
        for i in range(no_count):
            item['no'] = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr[{}]/td/text()'.format(i + 1)).extract_first()
            item['name'] = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr[{}]/td[2]/a/text()'.format(i+1)).extract_first()
            # item['date'] = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr[{}]/td[4]/text()'.format(i + 1)).extract_first()
            # item['count'] = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr[{}]/td[3]/text()'.format(i + 1)).extract_first()
            yield item