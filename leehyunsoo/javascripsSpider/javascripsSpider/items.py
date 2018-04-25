# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MainPageItem(scrapy.Item):
    # 기간 번호
    period_number = scrapy.Field()
    # 공고 일자
    publication_date = scrapy.Field()
    # 이의 신청 마감일
    application_deadline = scrapy.Field()


class DataItem(scrapy.Item):
    # 상표명
    brand_name = scrapy.Field()
    # 공시일
    publish_data = scrapy.Field()
    # 등록번호
    register_number = scrapy.Field()
    # 상표유형
    announcement_type = scrapy.Field()
    # 신청인
    applicant_person = scrapy.Field()
