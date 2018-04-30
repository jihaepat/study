import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders as enc


def send_mail():
    smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)
    smtp.ehlo()  # say Hello
    smtp.login('lhs950204', 'Rokmc#06!')

    msg = MIMEMultipart()
    msg['Subject'] = '작업완료'
    msg['From'] = 'lhs950204@naver.com'
    msg['To'] = 'lhs950204@naver.com'
    msg.attach(MIMEText('테스트입니다.'))

    part = MIMEBase('application', 'octet-stream')

    # part = MIMEApplication()
    part.set_payload(open('test2.json','rb').read())
    enc.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=ttt.json')
    msg.attach(part)

    smtp.sendmail('lhs950204@naver.com', 'lhs950204@naver.com', msg.as_string())
    smtp.quit()


send_mail()
