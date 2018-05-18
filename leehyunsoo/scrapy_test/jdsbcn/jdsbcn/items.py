# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class JdsbcnItem(scrapy.Item):
    brand_name = Field()
    category = Field()
    expiration_date = Field()
    ID = Field()
    img_url = Field()
