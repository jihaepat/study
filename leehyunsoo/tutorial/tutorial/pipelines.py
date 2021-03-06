# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime


class TutorialPipeline(object):

    def open_spider(self, spider):
        nowDatetime = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        print(spider.name, ' is started at ', nowDatetime)
        file = open('/home/leehyunsoo/4TB/crawl/log.txt', 'a')
        file.write((spider.name + ' is started at ' + nowDatetime + '\n'))
        file.close()
        # pass

    def process_item(self, item, spider):
        # print(item)
        return item

    def close_spider(self, spider):
        nowDatetime = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        print(spider.name, ' is end at ', nowDatetime)
        file = open('/home/leehyunsoo/4TB/crawl/log.txt', 'a')
        file.write((spider.name + ' is end at ' + nowDatetime + '\n'))
        file.close()
