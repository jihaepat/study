import scrapy
from html2text import html2text
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    name = "test"
    page_num = 1
    start_urls = [
        'http://quotes.toscrape.com/',
        # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        import urllib.request
        import sys
        import re
        ttt = response.xpath('//text()').extract()
        print(ttt)

        # html = response.body.decode("utf-8")
        #
        # body = re.search('<body.*</body>', html, re.I | re.S)
        #
        # body = body.group()
        # body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I | re.S)
        #
        # text = re.sub('<.+?>', '', body, 0, re.I | re.S)
        #
        # nospace = re.sub('&nbsp;| |\t|\r|\n', ' ', text)
        #
        # print(nospace)
        # print('html = ', len(html), ', text = ', len(text), ', nospace = ', len(nospace))
