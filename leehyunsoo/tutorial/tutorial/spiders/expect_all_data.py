import scrapy
import re
from scrapy import exceptions


class QuotesSpider(scrapy.Spider):
    name = "all_china"
    start_url = 'http://www.gbicom.cn/search/0/2/all/1/desc/0,,,,,1/1'

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.move_page_url)

    def move_page_url(self, response):
        raw_page_num = response.xpath('//*[@id="search-contain"]/div[2]/div[2]/span/text()').extract_first()
        extract_num = re.findall('\d+', raw_page_num)[0]

        for count in range(int(extract_num) + 1):
            yield scrapy.Request(url=('http://www.gbicom.cn/search/0/2/all/1/desc'
                                      + '/' + str(count) + ',,,,,1/1'), callback=self.get_data_url)

    def get_data_url(self, response):
        url = 'http://www.gbicom.cn'
        data = response.xpath('//*[@id="search-contain"]/div[2]/div[1]/dl/dt/a/@href').extract()
        make_data_url = [(url + data_url) for data_url in data]

        for data_url in make_data_url:
            yield scrapy.Request(url=data_url, callback=self.crawling_data)

    def crawling_data(self, response):
        print(response.url)
        yield {
            'brand_name': (response.xpath('//*[@id="brandName"]/text()').extract_first()).splitlines()[0],
            'category': response.xpath(
                '//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/text()').extract_first(),
            'expiration date': response.xpath(
                '//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/text()').extract_first(),
            'similar_group': response.xpath(
                '//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[3]/td/a/text()').extract(),
            'projectname': response.xpath(
                '//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[4]/td/a/em/text()').extract_first(),
            'ID': response.xpath('//*[@id="content_header"]/div/div[1]/div[2]/div[1]/span/em/text()').extract_first(),
            'img_url': response.xpath('//*[@id="content_header"]/div/div[1]/div[1]/div/img/@src').extract_first()
        }

# url 상세 내용
# search/카테고리 id/구매조건?(1,2 -> 2로 사용)/상표 유형(all)/상표 유형값?/현재 페이지 종류/페이지 번호,,,,,1/1
# raw_url = 'http://www.gbicom.cn/search/1/2/all/1/desc/2,,,,,1/1'


# # 상표 이름
# print((response.xpath('//*[@id="brandName"]/text()').extract_first()).splitlines()[0])
# # 카테고리
# print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/text()').extract_first())
# # 유효기간
# print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/text()').extract_first())
# # 비슷한 그룹
# print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[3]/td/a/text()').extract())
# # 해당프로젝트
# print(response.xpath('//*[@id="content_header"]/div/div[2]/div/div[1]/table/tbody/tr[4]/td/a/em/text()').extract_first())
# # 상표 ID
# print(response.xpath('//*[@id="content_header"]/div/div[1]/div[2]/div[1]/span/em/text()').extract_first())
#
