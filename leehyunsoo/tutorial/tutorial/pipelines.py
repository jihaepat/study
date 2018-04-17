# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import unicode_literals
from scrapy.mail import MailSender


class TutorialPipeline(object):

    def open_spider(self, spider):
        print('open_spider')
        # mailer = MailSender(mailfrom='test', smtphost='smtp.naver.com',
        #                     smtpport=465, smtpuser='lhs950204', smtppass='rokmc#06!')
        # mailer.send(to=["lhs950204@naver.com"], subject="finish", body="finish")

    def process_item(self, item, spider):
        # print(item)
        return item

    def close_spider(self, spider):
        return 0
