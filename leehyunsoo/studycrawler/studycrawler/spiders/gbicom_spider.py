import re
import os
import json
import codecs

import scrapy


class GBIcomSpider(scrapy.Spider):
    name = "gbicom"
    start_url = 'http://www.gbicom.cn'

    def start_requests(self):
        self.check_data_dict = self.check_before_data()
        print(self.check_data_dict['new'])
        print(self.check_data_dict['before'])
        yield scrapy.Request(self.start_url, callback=self.load_page_category)

    def load_page_category(self, response):
        get_categoty_href = response.xpath(
            '//*[@id="container"]/div[2]/div/ul/li/a[@class="clearfix"]/@href').extract()
        split_ar = []
        for ind in get_categoty_href:
            split_ar.append(re.findall('\d+', ind.split('c')[1])[0])

        make_category_url = [('http://www.gbicom.cn/search/' + id + '/2/all/1/desc/1,,,,,1/1') for id in split_ar]
        for category_url in make_category_url:
            yield scrapy.Request(url=category_url, callback=self.load_page_per_num)

    def load_page_per_num(self, response):
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
        data = {
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
        self.save_data(data)

    # TODO : 데이터 저장시 마지막 요소에 ',' 제거
    # TODO : 기존에 있는 데이터에 대한 처리 여부 전면 수정
    # -> 해당 사이트의 경우 매매사이트이므로 상표 번호를 모두 가져와 데이터 수집시 비교해야 한다고 판단함

    # TODO : 실제 스크립트에 적용하지 않음 -> 테스트를 위해 작성했던 스크립트의 페이징 방식과 다른 부분이 존재하여 아직 적용하지 못함
    def check_before_data(self):
        file_list = os.listdir()
        json_file_list = [file_name for file_name in file_list if
                          file_name.split('.')[-1] == 'json' and self.name in file_name.split('.')[0]]
        json_file_list.sort(reverse=True)
        if len(json_file_list) < 2:
            return {'new': json_file_list[0], 'before': json_file_list[0]}
        else:
            print(json_file_list[1])
            return {'new': json_file_list[0], 'before': json_file_list[1]}

    def save_data(self, data):
        file_ = codecs.open(self.check_data_dict['new'], 'a', encoding='utf8')
        file_.write(json.dumps(data, ensure_ascii=False) + ',\n')

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
