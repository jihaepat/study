import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "up"
    page_num = 1
    start_urls = [
        'https://www.enclean.com/brand/brand.findStation.list.do?first=f&siSelReq=&oilType=All&checkAll=&solux=0&netplus=0&autoread=0&self=0&speedmate=0&wash=0&store=0&oil=0&gift=0&siSch=&guSel=&oilString=&curPage=1',
    ]

    def parse(self, response):
        url = 'https://www.enclean.com/brand/brand.findStation.list.do?first=f&siSelReq=&oilType=All&checkAll=&solux=0&netplus=0&autoread=0&self=0&speedmate=0&wash=0&store=0&oil=0&gift=0&siSch=&guSel=&oilString=&curPage='
        for quote in response.xpath(
                '//div[@id="content"]/div[2]/form/div[2]/div/table/tbody/tr'):

            yield {
                'title': quote.css('span.st::text').extract_first(),
                'address': quote.css('td.td_addr::text').extract_first(),
                'tel': quote.xpath('td[4]/text()').extract_first()
            }

        now_page_num = response.xpath(
            '//div[@id="content"]/div[2]/form/div[3]/div/div/span/strong/text()').extract_first()

        if now_page_num == str(self.page_num):
            if self.page_num == 10 :
                return 0
            print(self.page_num)
            self.page_num += 1
            yield scrapy.Request(response.urljoin(url + str(self.page_num)))
