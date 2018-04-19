from __future__ import unicode_literals
from scrapy.exporters import JsonItemExporter
import pprint

class JsonPipeline(object):
    def __init__(self):
        print('__init__')
        self.file = open("newsCrawl.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()


    def close_spider(self, spider):
        print('close_spider')
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        print(item)
        self.exporter.export_item(item)

        return item
