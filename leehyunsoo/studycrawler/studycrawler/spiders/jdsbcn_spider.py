import scrapy
from scrapy.selector import Selector


class JDSBSpider(scrapy.Spider):
    name = "jdsb"
    start_url = 'http://www.jdsb.cn/brands_list----------.html'

    # 첫페이지 이동
    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.move_page_url)

    # 각각 페이지 이동
    def move_page_url(self, response):
        last_page_href = response.xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/a[7]/@href').extract_first()
        last_page_num = int(last_page_href.split('=')[1])

        print(last_page_num)
        for count in range(1, last_page_num + 1):
            yield scrapy.Request(url=(self.start_url + '?page=' + str(count)), callback=self.get_data_url)

    def get_data_url(self, response):
        raw_url = 'http://www.jdsb.cn/'
        data = response.xpath('//*[@id="main-nav-holder"]/div/div/ul/li/div/div[2]/a/@href').extract()
        make_data_url = [(raw_url + data_url) for data_url in data]
        for data_url in make_data_url:
            yield scrapy.Request(url=data_url, callback=self.crawling_data)

    def crawling_data(self, response):
        print(response.url)

        yield {
            'brand_name': response.css('tr.sb_value:nth-child(4) > td:nth-child(1)::text').extract_first(),
            'category': response.css('tr.sb_value:nth-child(2) > td:nth-child(2)::text').extract_first(),
            'expiration date': response.css('tr.sb_value:nth-child(6) > td:nth-child(2)::text').extract_first(),
            'ID': response.css('tr.sb_value:nth-child(2) > td:nth-child(1)::text').extract_first(),
            'img_url': response.xpath('//table[@class="img_part_table"]//img/@src').extract()
        }

# # 상표 등록 번호
# print(response.css('tr.sb_value:nth-child(2) > td:nth-child(1)::text').extract_first())
# # 상표 카테고리
# print(response.css('tr.sb_value:nth-child(2) > td:nth-child(2)::text').extract_first())
# # 시험발표날짜
# print(response.css('tr.sb_value:nth-child(2) > td:nth-child(3)::text').extract_first())
# # 예비 발표 기간 번호
# print(response.css('tr.sb_value:nth-child(2) > td:nth-child(4)::text').extract_first())
#
# # 상표이름
# print(response.css('tr.sb_value:nth-child(4) > td:nth-child(1)::text').extract_first())
# # 상표 적용 날짜
# print(response.css('tr.sb_value:nth-child(4) > td:nth-child(2)::text').extract_first())
# # 상표 유형
# print(response.css('tr.sb_value:nth-child(4) > td:nth-child(3)::text').extract_first())
# # 영구 보존 유무
# print(response.css('tr.sb_value:nth-child(4) > td:nth-child(4)::text').extract_first())
#
# # 상표 지주 회사
# print(response.css('tr.sb_value:nth-child(6) > td:nth-child(1) > a::text').extract_first())
# # 독점권의 기간
# print(response.css('tr.sb_value:nth-child(6) > td:nth-child(2)::text').extract_first())

# # img url
# print(response.xpath('/*[@class="img_part_table"]//img/@src').extract())
