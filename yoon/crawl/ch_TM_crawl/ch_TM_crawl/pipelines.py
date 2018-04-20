# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import unicode_literals
from scrapy.exporters import JsonItemExporter

class ChTmCrawlPipeline(object):
    def process_item(self, item, spider):
        return item
