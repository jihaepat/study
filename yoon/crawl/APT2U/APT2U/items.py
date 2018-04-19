# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class APT2UItem(scrapy.Item):
    aptname = scrapy.Field()  # 주택명
    link = scrapy.Field()  # 링크주소
    company = scrapy.Field()  # 건설업체
    receiptdate = scrapy.Field()  # 청약기간
    result_date = scrapy.Field()  # 당첨자발표일