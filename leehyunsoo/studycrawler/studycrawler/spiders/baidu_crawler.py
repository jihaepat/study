import re
import os
import json
import codecs
import datetime
import time
from time import sleep

import scrapy

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException, \
    UnexpectedAlertPresentException

regax = re.compile(r'[1|2][9|0]\d\d[-|.|/|\w]\d\d[-|.|/|\w]\d\d')


class Baidu(scrapy.Spider):
    name = 'baidu'
    # 처음 검색 페이지가 scrapy에서 로드가 안되서 music으로 로드한 후 selenium에서 각각의 검색어 별로 이동
    start_urls = ['http://music.baidu.com/']
    maximum_page = 101

    data_file_path = ''
    log_file_path = ''

    end_date = '20180501'

    def __init__(self):
        self.set_driver()

    def parse(self, response):
        try:
            self.load_page()
        except UnexpectedAlertPresentException as un:
            # self.log_write('unexpecteaAlertPresentExcetpion.txt', str(un) + self.driver.current_url + '\n\n')
            pass
        except BaseException as ex:
            self.log_write('load_page_exception.txt', str(ex) + '\n' + self.driver.current_url)

        # self.load_page()

    def set_driver(self):
        # chrome_options = webdriver.ChromeOptions()
        fire_fox_options = webdriver.FirefoxOptions()
        # fire_fox_options.add_argument('-headless')

        # self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)
        self.driver = webdriver.Firefox(executable_path='/home/leehyunsoo/4TB/geckodriver/geckodriver',
                                        options=fire_fox_options)

    def load_page(self):
        keyword = [
            'asics',
            '明朗热狗'  # 명랑핫도그
        ]
        for word in keyword:
            nowDatetime = (datetime.datetime.now()).strftime('%Y_%m_%d_%H:%M:%S')
            self.data_file_path = word + '_' + nowDatetime + '.json'
            self.log_file_path = word + '_error_' + nowDatetime + '.txt'
            self.set_start_json_file(self.data_file_path)
            self.get_data_elements_go_next_page(word)
            self.set_end_json_file(self.data_file_path)

        self.driver.close()

    def get_data_elements_go_next_page(self, word):
        raw_url = 'https://www.baidu.com/s?'
        print(word)

        # first_url = raw_url + 'wd=' + str(word) + '&pn=10'
        # self.driver.get(first_url)
        # gpc = self.set_date_term('2018-04-30', '2018-05-02')

        for page_num in range(0, self.maximum_page):
            self.driver.set_page_load_timeout(60)
            self.made_url = raw_url + 'wd={}&pn={}0&'.format(word, str(page_num))

            self.driver.get(self.made_url)

            data_elements = self.driver.find_elements_by_xpath('//div[@id="content_left"]/div/h3/a')
            data_href = [ind.get_attribute('href') for ind in data_elements]
            now_page_num = int(self.driver.find_element_by_xpath('//div[@id="page"]/strong/span[2]').text)
            print(now_page_num)
            for url in data_href:
                self.load_data(url)
            sleep(3)
            self.driver.get(self.made_url)
            sleep(3)
            try:
                print('페이지 찾는중======================================')
                print(self.driver.current_url)
                print('=================================================')
                next_page = self.driver.find_elements_by_xpath('//*[@id="page"]/a[@class="n"]')
                if now_page_num > 1 and len(next_page) < 2:
                    raise Exception
                if now_page_num > self.maximum_page:
                    raise Exception
            except Exception:
                print('exception 발생===================================\n')
                finish_keyword_file = open('finish.txt', 'a')
                finish_keyword_file.write(word + '페이지 완료')
                finish_keyword_file.close()
                return 0

    def load_data(self, url):
        data_dict = {}
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(url)
            print(self.driver.current_url)

            body = self.driver.find_element_by_xpath('//body').text
            # body_ar = body.split('\n')
            print(regax.findall(body))
            if len(regax.findall(body)) > 1:
                if ''.join(filter(str.isdigit, min(regax.findall(body)))) < self.end_date:
                    data_dict['title'] = self.driver.title
                    data_dict['url'] = self.driver.current_url
                    # data_dict['data'] = self.check_regax(body_ar)
                    # if len(data_dict['data']):
                    self.json_write(self.data_file_path, data_dict)
            elif len(regax.findall(body)) == 1:
                if ''.join(regax.findall(body)) < self.end_date:
                    data_dict['title'] = self.driver.title
                    data_dict['url'] = self.driver.current_url
                    # data_dict['data'] = self.check_regax(body_ar)
                    # if len(data_dict['data']):
                    self.json_write(self.data_file_path, data_dict)

            self.driver.set_page_load_timeout(30)
            self.driver.get(self.made_url)
            sleep(3)

        except TimeoutException:
            print('time_out : ', self.driver.current_url)
            try:
                body = self.driver.find_element_by_xpath('//body').text
                print(regax.findall(body))
                if len(regax.findall(body)) > 1:
                    if ''.join(filter(str.isdigit, min(regax.findall(body)))) < self.end_date:
                        data_dict['title'] = self.driver.title
                        data_dict['url'] = self.driver.current_url

                        self.json_write(self.data_file_path, data_dict)
                elif len(regax.findall(body)) == 1:
                    if ''.join(regax.findall(body)) < self.end_date:
                        data_dict['title'] = self.driver.title
                        data_dict['url'] = self.driver.current_url

                        self.json_write(self.data_file_path, data_dict)
                self.driver.set_page_load_timeout(30)
                self.driver.get(self.made_url)
                sleep(3)
            except TimeoutException:
                pass

            except NoSuchElementException as no_element:
                self.log_write(self.log_file_path, str(no_element) + self.driver.current_url + '\n\n')
                self.driver.set_page_load_timeout(30)
                self.driver.get(self.made_url)
                sleep(3)

            except UnexpectedAlertPresentException as un:
                self.log_write(self.log_file_path, str(un) + self.driver.current_url + '\n\n')
                self.driver.set_page_load_timeout(30)
                self.driver.get(self.made_url)
                sleep(3)

        except UnexpectedAlertPresentException as un:
            # self.log_write(self.log_file_path, str(un) + self.driver.current_url + '\n\n')
            self.driver.set_page_load_timeout(30)
            self.driver.get(self.made_url)
            sleep(3)

        except BaseException:
            self.log_write(self.log_file_path, 'BaseException : ' + self.driver.current_url + '\n\n')
            self.driver.set_page_load_timeout(30)
            self.driver.get(self.made_url)
            sleep(3)

    def log_write(self, file_path, word):
        file = open(file_path, 'a')
        file.write(word + '\n')
        file.close()

    def json_write(self, file_path, dict):
        file = open(file_path, 'a')
        file.write(json.dumps(dict, ensure_ascii=False, indent='\t') + ',')
        file.close()

    def check_regax(self, body_ar):
        result = []
        for x in range(len(body_ar)):
            if ''.join(filter(str.isdigit, ''.join(regax.findall(body_ar[x])))) < self.end_date:
                try:
                    result.append(body_ar[x - 1])
                    result.append(body_ar[x])
                    result.append(body_ar[x + 1])
                except Exception as ex:
                    print('check_regax_exception')
                    pass

        return sorted(set(result), key=result.index)

    def set_start_json_file(self, path):
        file = open(path, 'a')
        file.write('[\n')
        file.close()

    def set_end_json_file(self, path):
        file = open(path, 'a')
        file.write('\n]')
        file.close()

    # 기간검색 필터링
    # 현재 미사용 중 -> 검색결 중 상당수가 입력한 기간에 맞지 않음
    def set_date_term(self, start_data, finish_data):
        sleep(1)

        # fillter 버튼
        filter_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div')
        filter_btn.click()
        sleep(0.3)

        # 날짜 설정 버튼
        data_set_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/span[3]')
        data_set_btn.click()
        sleep(0.3)

        # 값입력 input
        start_date_btn = self.driver.find_element_by_xpath(
            '//*[@id="c-tips-container"]/div[2]/div/div/ul/li[6]/p[1]/input')
        end_date_btn = self.driver.find_element_by_xpath(
            '//*[@id="c-tips-container"]/div[2]/div/div/ul/li[6]/p[2]/input')
        # 입력후 검색 버튼
        search_btn = self.driver.find_element_by_xpath('//*[@id="c-tips-container"]/div[2]/div/div/ul/li[6]/a')

        start_date_btn.clear()
        sleep(0.3)
        start_date_btn.send_keys(start_data)
        sleep(0.3)
        end_date_btn.clear()
        sleep(0.3)
        end_date_btn.send_keys(finish_data)
        sleep(0.3)
        search_btn.click()

        gpc = [ind for ind in (self.driver.current_url).split('&') if 'gpc' in ind]

        return gpc[0]
