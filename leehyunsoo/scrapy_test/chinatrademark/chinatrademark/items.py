# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ChinatrademarkItem(scrapy.Item):
    broker_name= Field()
    mark_name = Field()
    img_href = Field()
    owner = Field()
    publish_number = Field()
    class_num = Field()
