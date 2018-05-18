import scrapy
from html2text import html2text
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    name = "test"
    page_num = 1
    start_url = \
        'http://www.86sb.com/products/list'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.second)

    # 'http://quotes.toscrape.com/page/2/',

    def first(self, response):
        print(response.status)
        print(response.xpath('//*[@id="div1"]/div[4]/li[28]/dl/dd[1]/p/abbr/text()').extract())
        total_page_num = int(''.join(
            filter(str.isdigit, (response.xpath('//*[@id="page_numbers"]/li[11]/span[1]/text()').extract_first()))))
        print(total_page_num)

        made_url = [
            self.start_url + '?tt=0&bt=&orderby=sort%7Cdesc%2Cup_at%7Cdesc&is_index=1&cg=' + str(num) + '#listfirst'
            for num in range(1, total_page_num + 1)]

        print(response.url)
        for x in made_url:
            yield scrapy.Request(url = x, callback=self.second)

    def second(self, response):
        ttt = response.xpath('//*[@id="listfirst"]/dl/dd/h2/a/@href').extract()
        for asdf in ttt:
            yield response.follow(asdf, callback=self.third)

    def third(self, response):
        print(response.url)
        name = response.xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/h1/text()').extract()
        img_url = response.xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img/@src').extract()
        print(name, '----', img_url)
