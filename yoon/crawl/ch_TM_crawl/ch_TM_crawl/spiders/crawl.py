import scrapy

class ch_spider(scrapy.Spider):
    name ='ch_scrapy'

    def start_requests(self):
        for i in range(2, 3):
            yield scrapy.Request('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum={0}'.format(i), callback=self.parse_url)

    def parse_url(self, response):
        # for sel in response.xpath('/html/body/div[4]/div[2]'):
        print((response.xpath('/html/body').extract()))