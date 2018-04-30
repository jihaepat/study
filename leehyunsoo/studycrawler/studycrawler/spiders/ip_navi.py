import re
import os
import json
import codecs

import scrapy

class IPNavi(scrapy.Spider):
    name = 'ipnavi'
    start_url = 'https://www.ip-navi.or.kr/broker/listByBroker.navi'
    brokers = {}

    def start_requests(self):
        yield scrapy.Request(self.start_url, callback=self.load_page)



    def load_page(self, response):
        self.check_data_dict = self.check_before_data()
        print(self.check_data_dict['new'])
        print(self.check_data_dict['before'])

        raw_url = 'https://www.ip-navi.or.kr/broker/listByBroker.navi?'
        total_page = response.xpath('//*[@id="contents"]/div[2]/div[2]/div/a[7]/@onclick').extract_first()
        total_page_num = int(''.join(filter(str.isdigit, total_page)))
        made_url = [raw_url + 'pageNum={}&fDate=&tDate=&search_keyword='.format(str(page_num)) for page_num in
                    range(1, total_page_num + 1)]
        for url in made_url:
            yield scrapy.Request(url, self.get_broker)

    def get_broker(self, response):
        p = re.compile('[0-9_-]')
        raw_num = len(response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr').extract())
        # name
        broker_name = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td[2]/a/text()').extract()

        # infringe trademark count
        infringe_trademark_count = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td[3]/text()').extract()

        # start broking date
        start_broking_date = response.xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td[4]').extract()
        compiled_start_broking_date = []
        for x in start_broking_date:
            compiled_start_broking_date.append(''.join(p.findall(x)))

        for count in range(raw_num):
            # pass
            self.brokers.update({
                'broker_name': broker_name[count],
                'infringe_trademark_count': infringe_trademark_count[count],
                'start_broking_date': compiled_start_broking_date[count]
            })
            yield self.brokers

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

    # def save_data(self, data):
    #     # print(data)
    #     # print(json.dumps(data,ensure_ascii=False))
    #     file_ = codecs.open(self.check_data_dict['new'], 'a', encoding='utf8')
    #     file_.write(json.dumps(data, ensure_ascii=False)+',\n')
