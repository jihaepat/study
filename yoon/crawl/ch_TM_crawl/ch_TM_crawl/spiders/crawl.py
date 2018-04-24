import scrapy
from ch_TM_crawl.items import ChTmCrawlItem

class ch_spider(scrapy.Spider):
    name ='ch_scrapy'

    def start_requests(self):
        for page_count in range(1, 101):
            yield scrapy.Request('https://market.ipr.zbj.com/trademark/?&page={}'.format(page_count), callback=self.page_data)


    def page_data(self, response):
        for i in range(len(response.xpath('/html/body/div[3]/div[4]/div[2]/a'))):
            response_url = response.xpath('/html/body/div[3]/div[4]/div[2]/a/@href').extract()
            for page_item in response_url:
                yield scrapy.Request(page_item, callback=self.main)



    def main(self, response):
        item = ChTmCrawlItem()
        item['name'] = response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/h3/text()').extract_first().replace('\n','')
        item['image'] = response.xpath('/html/body/div[3]/div[3]/div[1]/div[1]/img/@src').extract_first()
        item['category'] = response.xpath('/html/body/div[3]/div[3]/div[2]/div[3]/a/text()').extract_first()
        item['group'] = response.xpath('/html/body/div[3]/div[3]/div[2]/div[4]/p/text()').extract_first()
        item['price'] = response.xpath('/html/body/div[3]/div[3]/div[2]/div[7]/div[1]/p[2]/text()').extract_first()

        # print(item['name'], item['image'], item['category'], item['group'], item['price'])

        yield item
