import scrapy
from time import sleep
from selenium import webdriver
import json
import codecs
from selenium.webdriver.common.keys import Keys


class Spider86sb(scrapy.Spider):
    name = '86sb'
    start_urls = ['http://www.86sb.com/products/list']

    def __init__(self):
        self.set_driver()

    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)')
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver', options=chrome_options)

    def parse(self, response):
        print('parse')
        self.driver.get(response.url)
        sleep(2)
        total_page_num = int(''.join(
            filter(str.isdigit, (self.driver.find_element_by_xpath('//*[@id="page_numbers"]/li[11]/span[1]')).text)))
        print(total_page_num)

        made_url = [
            self.start_urls[0] + '?tt=0&bt=&orderby=sort%7Cdesc%2Cup_at%7Cdesc&is_index=1&cg=' + str(num) + '#listfirst'
            for num in range(1, total_page_num + 1)]

        for page_url in made_url:
            self.load_page(page_url)

        self.driver.close()

    def load_page(self, url):
        self.driver.get(url)
        sleep(2)
        page_data = [path.get_attribute('href') for path in
                     self.driver.find_elements_by_xpath('//*[@id="listfirst"]/dl/dt/a')]
        for url in page_data:
            self.load_data(url)
        print(page_data)

    def load_data(self,url):
        self.driver.get(url)
        sleep(1)
        brand_name = self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/h1')
        ID = self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[2]/ul/li[2]/p[2]/span')
        image_src = self.driver.find_element_by_xpath('/html/body/section[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img')
        data = {
            'brand_name':brand_name.text,
            'ID': ID.text,
            'image_src': image_src.text
        }
        self.save_data(data)

    def save_data(self, data):
        file_ = codecs.open(self.check_data_dict['new'], 'a', encoding='utf8')
        file_.write(json.dumps(data, ensure_ascii=False))