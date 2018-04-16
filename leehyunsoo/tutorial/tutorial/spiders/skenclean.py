import scrapy


class QuotesSpider(scrapy.Spider):
    name = "sk"
    page_num = 1
    start_urls = [
        'https://www.enclean.com/brand/brand.findStation.list.do?first=f&siSelReq=&oilType=All&checkAll=&solux=0&netplus=0&autoread=0&self=0&speedmate=0&wash=0&store=0&oil=0&gift=0&siSch=&guSel=&oilString=&curPage=1',
        # 'http://quotes.toscrape.com/page/2/',
    ]
    # url = 'https://www.enclean.com/brand/brand.findStation.list.do?first=f&siSelReq=&oilType=All&checkAll=&solux=0&netplus=0&autoread=0&self=0&speedmate=0&wash=0&store=0&oil=0&gift=0&siSch=&guSel=&oilString=&curPage=1'

    # content > div.inCont.stationVisual > form > div.paging > div > div > span > a:nth-child(4)
    # //div[@id="content"]/div[2]/form/div[3]/div/div/span/a[1]
    def parse(self, response):
        # print(self.page_num,'\n')
        print('start')
        # // *[ @ id = "content"] / div[2] / form / div[3] / div / div / span / a[1]
        for quote in response.xpath(
                '//div[@id="content"]/div[2]/form/div[2]/div/table/tbody/tr/td[2]/span[1]/text()').extract():
            # yield {
            #     'text': quote.css('span.text::text').extract_first(),
            #     'author': quote.css('small.author::text').extract_first(),
            #     'tags': quote.css('div.tags a.tag::text').extract(),
            # }
            print(quote)
        next_page_num = response.css('li.next a::attr(href)').extract_first()
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     # next_page = response.urljoin(next_page)
        #     self.page_num += 1
        #     # yield scrapy.Request(next_page, callback=self.parse)
        #     yield response.follow(next_page, callback = self.parse)
