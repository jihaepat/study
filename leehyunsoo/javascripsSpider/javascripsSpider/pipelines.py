# -*- coding: utf-8 -*-
import datetime
import codecs

import smtplib
import email.encoders as enc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


class PhantomjsPipeline(object):

    file_name = ''
    spider_name = ''


    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        nowDatetime = (datetime.datetime.now()).strftime('%Y_%m_%d_%H:%M:%S')
        print(spider.name, ' is started at ', nowDatetime)
        file = open('/home/leehyunsoo/4TB/crawl/log.txt', 'a')
        file.write((spider.name + ' is started at ' + nowDatetime + '\n'))
        file.close()
        self.file_name = spider.name + nowDatetime + '.json'
        data_file = codecs.open(self.file_name, 'a', encoding='utf8')
        data_file.write('[\n')
        data_file.close()

    def close_spider(self, spider):
        nowDatetime = (datetime.datetime.now()).strftime('%Y_%m_%d_%H:%M:%S')
        print(spider.name, ' is end at ', nowDatetime)
        file = open('/home/leehyunsoo/4TB/crawl/log.txt', 'a')
        file.write((spider.name + ' is end at ' + nowDatetime + '\n'))
        file.close()
        data_file = codecs.open(self.file_name, 'a', encoding='utf8')

        data_file.write(']')
        data_file.close()
        self.spider_name = spider.name
        self.send_mail()

    def send_mail(self):
        smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)
        smtp.ehlo()
        smtp.login('lhs950204', 'Rokmc#06!')

        msg = MIMEMultipart()
        msg['Subject'] = '작업완료'
        msg['From'] = 'lhs950204@naver.com'
        msg['To'] = 'lhs950204@naver.com'
        msg.attach(MIMEText('테스트입니다.'))

        part = MIMEBase('application', 'octet-stream')

        # part = MIMEApplication()
        part.set_payload(open(self.file_name, 'rb').read())
        enc.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=ttt.json')
        msg.attach(part)

        smtp.sendmail('lhs950204@naver.com', 'lhs950204@naver.com', msg.as_string())
        smtp.quit()
