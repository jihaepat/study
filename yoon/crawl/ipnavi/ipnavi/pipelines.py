# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
import operator

class IpnaviPipeline(object):
    prnt_date = datetime.datetime.now().strftime('%Y%m%d%H%M')
    def open_spider(self, spider):
        print('start_crawl')
        print(self.prnt_date)
        self.file = open('/media/yoonjae/4TB2/ipnavi/ipnavi_'+self.prnt_date+'.json', 'w+', encoding='utf-8')
        # self.file.write('[\n')

    def close_spider(self, spider):
        # self.file.write(']\n')
        print('enc_crawl')

    def sort(self):
        sorted(self.file, key='no.get')
        print(self.file.read())
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(line)
        return item