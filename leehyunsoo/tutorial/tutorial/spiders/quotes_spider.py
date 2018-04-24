import scrapy


class QuotesSpider(scrapy.Spider):
    name = "test"
    page_num = 1
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        print(self.page_num,'\n')
        for quote in response.css('div.quote'):
            print(type(quote))
            # yield {
            #     'text': quote.css('span.text::text').extract_first(),
            #     'author': quote.css('small.author::text').extract_first(),
            #     'tags': quote.css('div.tags a.tag::text').extract(),
            # }
        #     print(quote.css('span.text::text').extract_first())
        #     print(quote.css('small.author::text').extract_first())
        #     print(quote.css('div.tags a.tag::text').extract())
        # print('\n')
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            self.page_num += 1
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback = self.parse)
