from time import sleep
import json
import codecs
import re

import scrapy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class JSLoadTest(scrapy.Spider):
    name = "JS"
    start_url = 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/homePage.html'

    def start_requests(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)
        yield scrapy.Request(self.start_url, callback=self.get_main_page_url)

    def get_main_page_url(self, response):
        print('get_main_page_url')

        self.driver.get(response.url)

        raw_url = 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum='

        page_num = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[2]/table/tbody/tr[2]').get_attribute('onclick')
        num = int(''.join(filter(str.isdigit, page_num)))

        try:
            file = open('testt.json', 'r')

            data = json.load(file)
            print(data[-1]['period_number'])
            if int(data[-1]['period_number']) < num:
                with open('test2.json', 'a', encoding='utf8') as f:
                    for ind in data:
                        f.write(json.dumps(ind, ensure_ascii=False))
                        f.write(',')
            for ind in range(int(data[-1]['period_number'])+1, 5):
                # for ind in range(1, num+1):
                self.main_page_dict = {
                    'period_number': str(ind),
                    'data': {}
                }
                self.get_data(response=(raw_url + str(ind)))
                self.save_data(self.main_page_dict)
                if ind + 1 != 5:
                    with open('test2.json', 'a') as file:
                        file.write(',')
        except:
            for ind in range(1, 5):
                # for ind in range(1, num+1):
                self.main_page_dict = {
                    'period_number': str(ind),
                    'data': {}
                }
                self.get_data(response=(raw_url + str(ind)))
                self.save_data(self.main_page_dict)
                if ind + 1 != 5:
                    with open('test2.json', 'a') as file:
                        file.write(',')

    def get_data(self, response):
        print('get_data')
        self.driver.get(response)
        sleep(6)
        sel = scrapy.Selector(text=self.driver.page_source)
        total_page_num = int(''.join(
            filter(str.isdigit, (sel.xpath('//*[@id="pages"]/table/tbody/tr/td[6]/span/text()').extract_first()))))

        for page_num in range(1, total_page_num):
            input_box = self.driver.find_element_by_class_name('pagination-num')
            input_box.clear()
            input_box.send_keys(page_num)
            input_box.send_keys(Keys.ENTER)
            sleep(6)

            # 페이지별 개수
            row_num = len(self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[1]'))
            # 상호명
            brand_name = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[7]')
            # 고시일
            publish_data = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[3]')
            # 발표타입
            publish_type = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[4]')
            # 등록번호
            publish_num = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[5]')
            # 신청인
            publish_person = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[6]')
            # 사진 링크
            image_href = self.driver.find_elements_by_xpath('//tr[@class="evenBj"]/td[8]/a')

            for count in range(row_num):
                self.data_dict = {
                    'brand_name': brand_name[count].text,
                    'publish_num': publish_num[count].text,
                    'publish_data': publish_data[count].text,
                    'publish_person': publish_person[count].text,
                    'publish_type': publish_type[count].text,
                    'image_num': (re.findall(r'(\w+)', image_href[count].get_attribute('onclick')))[2],
                    'image_cat': (re.findall(r'(\w+)', image_href[count].get_attribute('onclick')))[3]
                }
                print(json.dumps(self.data_dict, ensure_ascii=False))
                self.main_page_dict['data'][publish_num[count].text] = self.data_dict

    def save_data(self, data):
        file_ = codecs.open('test2.json', 'a', encoding='utf8')
        file_.write(json.dumps(data, ensure_ascii=False))

    def get_img_url(self):
        return 'img_url'
