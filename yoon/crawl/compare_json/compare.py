import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


origin_file = '/home/yoonjae/study/yoon/crawl/compare_json/origin.json'
change_log_file = '/home/yoonjae/study/yoon/crawl/compare_json/shorttext.txt'


with open('origin.json') as data_file:
    old_json = json.load(data_file)
with open('new.json') as data_file:
    new_json = json.load(data_file)

    email_text_file = 'shorttext.txt'
    email_file_read = open(email_text_file, 'w')

    def scan_json(notifi_number, search_type):

        for new_count in new_json[notifi_number]['data']:
            compare_count = 0
            for old_count in old_json[notifi_number]['data']:

                if new_json[notifi_number]['data'][new_count][search_type] == old_json[notifi_number]['data'][old_count][search_type]:
                    compare_count += 1
            if compare_count < 1:
                email_file_read.write(new_json[notifi_number]['data'][new_count][search_type])

    def send_email():
        smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)
        smtp.ehlo()
        smtp.login('asas1994', 'Complete19!94')

        msg = MIMEMultipart()
        msg['Subject'] = '[크롤추가 메일발송]'
        msg['From'] = 'asas1994@naver.com'
        msg['To'] = 'asas1994@naver.com'
        msg.attach(MIMEText('내용입니다'))

        part = MIMEBase('application', 'octet-stream')

        part.set_payload(open(change_log_file, 'rb').read())
        part.add_header('Content-Disposition', 'attachment; filename=update.txt')
        msg.attach(part)

        smtp.sendmail('asas1994@naver.com', 'asas1994@naver.com', msg.as_string())
        smtp.quit()

scan_json(0, 'publish_num')




