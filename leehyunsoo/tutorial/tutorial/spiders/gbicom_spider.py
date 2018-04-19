import scrapy
import re
from scrapy import exceptions


class QuotesSpider(scrapy.Spider):
    name = "china"
    start_url = 'http://www.gbicom.cn'

    # start_url = 'http://www.'

    # 시작시 메인 페이지의 모든 카테고리를 수집후 각각의
    # 카테고리의 url조합을 위해 start_url로 이동 및  set_category_start callback
    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.set_category)

    # 카테고리 url & id 수집 후 각각의 카테고리별 페이지 이동
    def set_category(self, response):
        get_categoty_href = response.xpath(
            '//*[@id="container"]/div[2]/div/ul/li/a[@class="clearfix"]/@href').extract()
        split_ar = []
        for ind in get_categoty_href:
            split_ar.append(re.findall('\d+', ind.split('c')[1])[0])

        make_category_url = [('http://www.gbicom.cn/search/' + id + '/2/all/1/desc/1,,,,,1/1') for id in split_ar]
        for category_url in make_category_url:
            yield scrapy.Request(url=category_url, callback=self.move_page_url)

    def move_page_url(self, response):
        split_url = (response.url).split('/')
        extract_url = '/'.join(split_url[:-2])
        raw_page_num = response.xpath('//*[@id="search-contain"]/div[2]/div[2]/span/text()').extract_first()
        extract_num = re.findall('\d+', raw_page_num)[0]

        for count in range(int(extract_num) + 1):
            yield scrapy.Request(url=(extract_url + '/' + str(count) + ',,,,,1/1'), callback=self.get_data_url)

    def get_data_url(self, response):
        data = response.xpath('//*[@id="search-contain"]/div[2]/div[1]/dl/dt/a/@href').extract()
        make_data_url = [(self.start_url + data_url) for data_url in data]

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
