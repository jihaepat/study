import scrapy
import os
import json
import codecs



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
        data = {
            'brand_name': response.css('tr.sb_value:nth-child(4) > td:nth-child(1)::text').extract_first(),
            'category': response.css('tr.sb_value:nth-child(2) > td:nth-child(2)::text').extract_first(),
            'expiration_date': response.css('tr.sb_value:nth-child(6) > td:nth-child(2)::text').extract_first(),
            'ID': response.css('tr.sb_value:nth-child(2) > td:nth-child(1)::text').extract_first(),
            'img_url': response.xpath('//table[@class="img_part_table"]//img/@src').extract()
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
