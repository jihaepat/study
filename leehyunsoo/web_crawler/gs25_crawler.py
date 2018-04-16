from time import sleep

import requests
from bs4 import BeautifulSoup


def crawler_1():
    # HTTP GET Request
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')

    # HTML 소스 가져오기
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    # HTTP Header 가져오기
    header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok
    return None


def crawler_2(max_page):
    page = 1
    while page < max_page:
        url = 'https://beomi.github.io/beomi.github.io_old/'
        # url = 'http://gs25.gsretail.com/gscvs/ko/store-services/locations'
        load = requests.get(url)
        # sleep(3)
        html = load.text
        soup = BeautifulSoup(html,'lxml')
        for title in soup.select('h3 > a'):
        # for title in soup.select('tr > td > a'):
            print(title.text)
        # print(soup)
        page += 1

crawler_2(2)