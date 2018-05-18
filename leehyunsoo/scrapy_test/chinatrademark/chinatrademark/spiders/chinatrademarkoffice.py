import re
import json
from collections import OrderedDict

import scrapy

from chinatrademark.items import ChinatrademarkItem


class ChinatradeMart(scrapy.Spider):
    name = "china"
    page_num = 1
    start_url = 'https://www.chinatrademarkoffice.com/index.php/search/listxb'
    with open('broker_name.json') as broker:
        broker = json.load(broker)
        broker_list = [name['name'] for name in broker]

    def start_requests(self):
        for name in self.broker_list:
            yield scrapy.Request(url=self.start_url + '?int.appPerson={}'.format(name),
                                 callback=self.parse,
                                 meta={"name": name}
                                 )

    def parse(self, response):
        print(response.meta['name'],'-----',response.url)
        row_count = len(response.xpath('//*[@id="xblisthtml"]/table/tbody/tr[1]/td[2]').extract())
        mark_name = response.xpath('//*[@id="xblisthtml"]/table/tbody/tr[1]/td[2]/h3/a[2]/text()').extract()
        img_href = response.xpath('//*[@id="xblisthtml"]/table/tbody/tr[1]/td[1]/a/div/@loadsrc').extract()
        owner = response.xpath('//*[@id="xblisthtml"]/table/tbody/tr[1]/td[2]/font/a/text()').extract()
        number_class_num = response.xpath('//*[@id="xblisthtml"]/table/tbody/tr[1]/td[2]/font/text()[1]').extract()
        regax_number = self.number_regax(number_class_num)
        regax_class_num = self.number_regax(number_class_num)
        for count in range(row_count):
            items = ChinatrademarkItem()
            items['broker_name'] = response.meta['name']
            items['mark_name'] = " ".join(mark_name[count].split())
            items['img_href'] = img_href[count]
            items['owner'] = owner[count]
            items['publish_number'] = regax_number[count]
            items['class_num'] = regax_class_num[count]
            yield items

        next_btn = response.xpath('//*[@id="page"]/a/text()').extract()
        btn_href = response.xpath('//*[@id="page"]/a/@href').extract()
        no_duplicate = list(OrderedDict.fromkeys(next_btn))

        try:
            if btn_href[no_duplicate.index('>')]:
                yield response.follow(btn_href[no_duplicate.index('>')],
                                      callback=self.parse,
                                      meta={"name": response.meta['name']}
                                      )
        except:
            pass

    def number_regax(self, number_ar):
        result = []
        regax = re.compile('\w+r: \d+')
        for number in number_ar:
            result.append((''.join(regax.findall(number))).split(':')[-1])
        return result

    def class_regax(self, class_ar):
        result = []
        regax = re.compile('\w+s: \d+')
        for class_num in class_ar:
            result.append((''.join(regax.findall(class_num))).split(':')[-1])
        return result
