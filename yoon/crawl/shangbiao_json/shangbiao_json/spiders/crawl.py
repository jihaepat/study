import scrapy
import pyautogui
import json
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



WAIT_TIME_SHORT =1
WAIT_TIME_LONG =4
class spider_url(scrapy.Spider):
    name = 'CR'
    chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'


    driver = webdriver.Chrome(chromedriver)
    driver.set_window_size(1400, 1080)
    driver.set_window_position(2650, 1000)
    driver.get('http://www.shangbiao.com/search')

    def start_requests(self):
        insert_data = self.driver.find_element_by_xpath('//*[@id="sub_button"]')
        #Json File Read
        read_json = json.load(open('ipnavi.json'))
        sleep(WAIT_TIME_LONG)
        for x in range(len(read_json['data'])):
            sleep(WAIT_TIME_LONG)
            read_json_name = (read_json['data'][x]['name'])
            temp = self.driver.find_element_by_xpath('//*[@id="sub_button"]')
            temp.clear()
            sleep(WAIT_TIME_SHORT)
            temp.send_keys(read_json_name)
            sleep(WAIT_TIME_SHORT)
            temp.send_keys(Keys.RETURN)
            sleep(WAIT_TIME_SHORT)
            search_click = self.driver.find_element_by_xpath('//*[@id="namebrand"]')
            #마우스 움직임 발생
            pyautogui.moveRel(0, 10)
            sleep(WAIT_TIME_SHORT)
            pyautogui.moveRel(0, -10)
            search_click.send_keys(Keys.RETURN)
            sleep(WAIT_TIME_LONG)

            # # 페이지 10->50으로 변경
            self.driver.find_element_by_xpath('//*[@id="sel_page_size"]').click()
            sleep(WAIT_TIME_SHORT)
            self.driver.find_element_by_xpath('//*[@id="sel_page_size"]/option[3]').click()
            sleep(WAIT_TIME_LONG)
            content_end_num = len(self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr'))
            total_num = int(self.driver.find_element_by_xpath('//*[@id="keyword01"]/div/div[1]/h5/span').text)
            count = 0
            while True:
                page_num_input = self.driver.find_element_by_xpath('//*[@id="page_jump"]')
                page_num_input.click()
                sleep(WAIT_TIME_SHORT)
                page_num_input.clear()
                sleep(WAIT_TIME_SHORT)
                page_num_input.send_keys(count+1)
                sleep(WAIT_TIME_SHORT)
                page_num_input.send_keys(Keys.RETURN)

                self.driver.find_element_by_xpath('//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/input[2]').send_keys(
                    Keys.ENTER)
                count += 1
                sleep(WAIT_TIME_LONG)
                print(count)
                content_end_num = len(self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr'))
                print(content_end_num)
                button_list = []
                #다음페이지 버튼이 있는지 확인
                for i in range(content_end_num):
                    name = self.driver.find_element_by_xpath('//*[@id="ajbrandsearch"]/tr[{}]/td[3]/ul/li[1]/div/a'.format(i + 1))
                    origin_number = self.driver.find_element_by_xpath(
                        '//*[@id="ajbrandsearch"]/tr[{}]/td[5]/ul/li[1]/div'.format(i + 1))
                    print(name.text, origin_number.text, x)
                page_count = 0
                for j in range(len(self.driver.find_elements_by_xpath('//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/li'))):
                    if self.driver.find_element_by_xpath('//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/li[{}]'.format(j + 1)).get_attribute('class') == 'num next-page':
                        page_count += 1
                if page_count == 0:
                    break














            # page = 10
            # if content_end_num > 0 and content_end_num <= 10: #10
            #     page = 10
            #     print('1번')
            #     pass
            # elif content_end_num > 10 and content_end_num <= 50: #20
            #     page = 20
            #     print('2번')
            #     self.driver.find_element_by_xpath('//*[@id="sel_page_size"]/option[2]').click()
            # elif content_end_num > 50: #50
            #     page = 50
            #     print('3번')
            #     self.driver.find_element_by_xpath('//*[@id="sel_page_size"]/option[3]').click()
            #
            # if content_end_num % page != 0:
            #     page_num = int(content_end_num / page) + 1
            #     print('+1', page_num, content_end_num, x)
            # else:
            #     page_num = int(content_end_num / page)
            #     print('+0', page_num, content_end_num, x)
            #
            #
            #
            #
            # for x in range(page_num):
            #     sleep(WAIT_TIME_LONG)
            #     if int(self.driver.find_element_by_xpath('//*[@id="keyword01"]/div/div[1]/h5/span').text) > 100:
            #         break
            #     page_num_input = self.driver.find_element_by_xpath('//*[@id="page_jump"]')
            #     page_num_input.click()
            #     sleep(WAIT_TIME_SHORT)
            #     page_num_input.clear()
            #     sleep(WAIT_TIME_SHORT)
            #     page_num_input.send_keys(x+1)
            #     sleep(WAIT_TIME_SHORT)
            #     page_num_input.send_keys(Keys.RETURN)
            #     sleep(WAIT_TIME_SHORT)
            #     self.driver.find_element_by_xpath('//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/input[2]').send_keys(
            #         Keys.ENTER)
            #     sleep(1)
            #     # 페이지에 표시된 수와 틀린경우가 있어서 실 페이지 게시물 체크
            #     content_end_num = len(self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr'))
            #     print(content_end_num)
            #     for i in range(content_end_num):
            #         name = self.driver.find_element_by_xpath('//*[@id="ajbrandsearch"]/tr[{}]/td[3]/ul/li[1]/div/a'.format(i + 1))
            #         origin_number = self.driver.find_element_by_xpath(
            #             '//*[@id="ajbrandsearch"]/tr[{}]/td[5]/ul/li[1]/div'.format(i + 1))
            #         print(name.text, origin_number.text)
