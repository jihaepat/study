# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class PipelinePipeline(object):
    def open_spider(self, spider):
        print('start_crawl')
        self.file = open('test.json', 'w', encoding='utf-8')
        # self.file.write('[\n')

    def close_spider(self, spider):
        # self.file.write(']\n')
        self.file.close()
        print('enc_crawl')

    def close_spider(self, spider):
        # self.file.write(']\n')
        self.file.close()
        print('enc_crawl')
