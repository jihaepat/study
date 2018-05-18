# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class GbicomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand_name = Field()
    category = Field()
    expiration_date = Field()
    similar_group = Field()
    projectname = Field()
    ID = Field()
    img_url = Field()

