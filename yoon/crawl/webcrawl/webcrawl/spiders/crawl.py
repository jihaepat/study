import scrapy
from webcrawl.items import WebcrawlItem

# logo_image = scrapy.Field()  # 상표 로고
# company_name_image = scrapy.Field()  # 회사 이름
# category = scrapy.Field()  # 상품분류
# registration_number = scrapy.Field()  # 등록번호
# validity_date = scrapy.Field()  # 독점기간
# group = scrapy.Field()  # 상표 그룹
# price = scrapy.Field()  # 가격

class spider_url(scrapy.Spider):
    name = "spider_url"

    def start_requests(self):
        yield scrapy.Request('http://www.shangbiao.com/tm/?t=t&p=25', callback=self.page_count)

    def page_count(self, response):
        print(response)
        end_page = response.xpath('/html/body/div[1]/ul/li[5]/a/text()').extract_first()
        print(end_page)
        for i in range(int(end_page)):
            yield scrapy.Request('http://www.shangbiao.com/tm/{0}?t=t&p=25'.format(i), callback=self.parse)

    def parse(self, response):
        print(response)
        origin_url = 'http://www.shangbiao.com'
        response_url = response.xpath('/html/body/div[1]/div[5]/ul/li/a/@href').extract()
        real_url = [(origin_url + ind) for ind in response_url]
        for page_item in real_url:
            yield scrapy.Request(page_item, callback=self.main)

    def main(self, response):
        item = WebcrawlItem()

        split_category = response.xpath('/html/body/div[1]/div[2]/div[2]/dl[1]/dd/text()').extract_first()
        sum_category = (split_category.splitlines()[1].strip()+split_category.splitlines()[2].strip())

        sum_registration_number_image = response.xpath('/html/body/div[1]/div[2]/div[2]/dl[2]/dd/img/@src').extract()
        item['logo_image'] = response.xpath('/html/body/div[1]/div[2]/div[2]/h4/img/@src').extract()
        item['company_name_image'] = response.xpath('/html/body/div[1]/div[2]/div[2]/h4/img/@src').extract()
        item['category'] = sum_category
        item['registration_number_image'] = sum_registration_number_image
        item['group'] = response.xpath('/html/body/div[1]/div[2]/div[2]/dl[4]/dd/text()').extract()
        item['price'] = response.xpath('/html/body/div[1]/div[2]/div[2]/div/dl[1]/dd/em/i/text()').extract()

        yield item
