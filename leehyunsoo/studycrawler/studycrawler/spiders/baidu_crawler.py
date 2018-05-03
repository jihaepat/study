import re
import os
import json
import codecs
import datetime
import time
from time import sleep

import scrapy

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException


class baidu(scrapy.Spider):
    name = 'baidu'
    # 처음 검색 페이지가 scrapy에서 로드가 안되서 music으로 로드한 후 selenium에서 각각의 검색어 별로 이동
    start_urls = ['http://music.baidu.com/']
    maximum_page = 1

    data_file_path = ''
    log_file_path = ''

    def __init__(self):
        self.set_driver()

    def parse(self, response):
        self.load_page()

    def set_driver(self):
        # chrome_options = webdriver.ChromeOptions()
        fire_fox_options = webdriver.FirefoxOptions()
        # fire_fox_options.add_argument('-headless')

        # self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)
        self.driver = webdriver.Firefox(executable_path='/home/leehyunsoo/4TB/geckodriver/geckodriver',
                                        options=fire_fox_options)

    def load_page(self):
        keyword = [
            'asic', 'samsung'
        ]
        for word in keyword:
            nowDatetime = (datetime.datetime.now()).strftime('%Y_%m_%d_%H:%M:%S')
            self.data_file_path = word + '_' + nowDatetime + '.json'
            self.log_file_path = word + '_' + nowDatetime + '.txt'
            self.set_start_json_file(self.data_file_path)
            self.get_data_elements_go_next_page(word)
            self.set_end_json_file(self.data_file_path)

        self.driver.close()

    def get_data_elements_go_next_page(self, word):
        raw_url = 'https://www.baidu.com/s?'
        print(word)
        first_url = raw_url + 'wd=' + str(word) + '&pn=10'
        self.driver.get(first_url)
        gpc = self.set_date_term('2018-04-30', '2018-05-02')

        for page_num in range(0, self.maximum_page):
            self.made_url = raw_url + 'wd={}&pn={}0&'.format(word, str(page_num)) + gpc
            print(self.made_url)

            self.driver.get(self.made_url)

            data_elements = self.driver.find_elements_by_xpath('//div[@id="content_left"]/div/h3/a')
            data_href = [ind.get_attribute('href') for ind in data_elements]
            now_page_num = int(self.driver.find_element_by_xpath('//*[@id="page"]/strong/span[2]').text)

            for url in data_href:
                self.load_data(url)
            sleep(1)
            try:
                next_page = self.driver.find_element_by_xpath('//*[@id="page"]/a[@class="n"]')
                href = next_page.get_attribute('href')
                print(href)
                if now_page_num > self.maximum_page:
                    raise Exception
            except:
                return 0
            # sleep(1)

    def load_data(self, url):
        data_dict = {}
        regax = re.compile('(19|20)\d+(-|.|/|)\d+(-|.|/|)\d+')
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(url)
            print(self.driver.current_url)

            body = self.driver.find_element_by_xpath('//body').text
            body_ar = body.split('\n')

            if regax.findall(body):
                data_dict['title'] = self.driver.title
                data_dict['url'] = self.driver.current_url
                data_dict['data'] = self.check_regax(body_ar)
                self.json_write(self.data_file_path, data_dict)
            self.driver.get(self.made_url)
            sleep(3)

        except TimeoutException:
            print('time_out')
            try:
                body = self.driver.find_element_by_xpath('//body').text
                body_ar = body.split('\n')
                if regax.findall(body):
                    data_dict['title'] = self.driver.title
                    data_dict['url'] = self.driver.current_url
                    data_dict['data'] = self.check_regax(body_ar)
                    self.json_write(self.data_file_path, data_dict)
                self.driver.get(self.made_url)
                sleep(3)

            except TimeoutException:
                pass
            except NoSuchElementException as no_element:
                self.log_write(self.log_file_path, str(no_element) + self.driver.current_url + '\n\n')
                self.driver.get(self.made_url)
                sleep(3)

        except NoSuchElementException as no_element:
            self.log_write(self.log_file_path, str(no_element) + self.driver.current_url + '\n\n')
            self.driver.get(self.made_url)
            sleep(3)


        except WebDriverException as wd:
            self.log_write(self.log_file_path, str(wd) + self.driver.current_url + '\n\n')
            self.driver.get(self.made_url)
            sleep(3)

        except BaseException:
            self.log_write(self.log_file_path, 'BaseException : ' + self.driver.current_url + '\n\n')
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
        regax = re.compile(r'[1|2][9|0]\d*[-|.|/|\w]\d\d[-|.|/|\w]\d\d')
        result = []
        for x in range(len(body_ar)):
            if regax.findall(body_ar[x]):
                try:
                    result.append(body_ar[x - 1])
                    result.append(body_ar[x])
                    result.append(body_ar[x + 1])
                except:
                    result.append(body_ar[x])
        return sorted(set(result), key=result.index)

    def set_start_json_file(self, path):
        file = open(path, 'a')
        file.write('[\n')
        file.close()

    def set_end_json_file(self, path):
        file = open(path, 'a')
        file.write('\n]')
        file.close()

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
