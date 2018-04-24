# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlItem(scrapy.Item):
    logo_image = scrapy.Field()  # 상표 로고
    company_name_image = scrapy.Field()  # 회사 이름
    category = scrapy.Field()  # 상품분류
    registration_number_image = scrapy.Field()  # 등록번호
    validity_date = scrapy.Field()  # 독점기간
    group = scrapy.Field()  # 상표 그룹
    price = scrapy.Field()  # 가격

