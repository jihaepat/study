import scrapy
import pyautogui
import json
import re
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from shangbiao_json.items import ShangbiaoJsonItem


WAIT_TIME_SHORT =1.5
WAIT_TIME_LONG = 4

class spider_url(scrapy.Spider):
    name = 'CR'

    chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.set_window_size(1400, 1080)
    driver.set_window_position(2650, 1000)
    driver.get('http://www.shangbiao.com/search')
    read_json = json.load(open('ipnavi.json'))
    page_count_num = 0
    cycle_count = 105
    def start_requests(self):
        sleep(WAIT_TIME_SHORT)
        self.file = open('test4.json', 'w', encoding='utf-8')
        for x in range(len(self.read_json['data']))[105:]:
            sleep(WAIT_TIME_SHORT)
            read_json_name = (self.read_json['data'][x]['name'])
            click_title_box = self.driver.find_element_by_xpath('//*[@id="sub_button"]')
            click_title_box.clear()
            sleep(WAIT_TIME_SHORT)
            click_title_box.send_keys(read_json_name)
            sleep(WAIT_TIME_SHORT)
            click_title_box.send_keys(Keys.RETURN)
            sleep(WAIT_TIME_SHORT)
            if self.cycle_count == 0:
                search_click = self.driver.find_element_by_xpath('//*[@id="namebrand"]') # 한버이상 클릭필요 없음
                # 마우스 움직임 발생
                pyautogui.moveRel(0, 10)
                sleep(WAIT_TIME_SHORT)
                pyautogui.moveRel(0, -10)
                search_click.send_keys(Keys.RETURN)
                sleep(WAIT_TIME_LONG)
            print(x, '번째')


            self.next_page_check()
            self.cycle_count += 1

    # 다음페이지 버튼이 있는지 확인
    def next_page_check(self):
        # # 페이지 10->50으로 변경
        if self.driver.find_element_by_class_name('col-fd5f43').text == '':
            print('없음')
            read_json_name = (self.read_json['data'][self.cycle_count+2]['name'])
            click_title_box = self.driver.find_element_by_xpath('//*[@id="sub_button"]')
            click_title_box.clear()
            sleep(WAIT_TIME_SHORT)
            click_title_box.send_keys(read_json_name)
            sleep(WAIT_TIME_SHORT)
            click_title_box.send_keys(Keys.RETURN)
            sleep(WAIT_TIME_SHORT)

        sleep(WAIT_TIME_SHORT)
        self.driver.find_element_by_xpath('//*[@id="sel_page_size"]').click()
        sleep(WAIT_TIME_SHORT)
        self.driver.find_element_by_xpath('//*[@id="sel_page_size"]/option[3]').click()
        sleep(WAIT_TIME_LONG)

        self.page_count_num = 0
        while True:
            self.next_page_button_click()
            self.page_count_num += 1
            sleep(WAIT_TIME_LONG)

            content_end_num = len(self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr'))
            print(self.page_count_num, '페이지 :', content_end_num, '개')
            name = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[3]/ul/li[1]/div/a') #상표번호
            cat = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[4]/ul/li[1]/div') #카테고리
            register_num = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[5]/ul/li[1]/div') #등록번호
            stable_num = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[4]/ul/li[3]/div') #공고번호
            status = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[3]/ul/li[2]/div/em') #상태
            register_date = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[5]/ul/li[2]/div') #등록 발표일
            offeror_name = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[5]/ul/li[3]/div') #신청인
            img_src = self.driver.find_elements_by_xpath('//*[@id="ajbrandsearch"]/tr/td[2]/div/a/img') #URL

            for i in range(len(name)):
                # if stable_num[i].text != '':
                #     re_stable_num = stable_num[i].text[7:]
                crawl_dic = {
                    'name': name[i].text,
                    'cat': cat[i].text[3:],
                    'register_num': register_num[i].text[5:],
                    'stable_num': stable_num[i].text[7:],
                    'status': status[i].text,
                    'register_date': register_date[i].text[7:],
                    'offeror_name': offeror_name[i].text[4:],
                    'img_src': img_src[i].get_attribute('src'),
                }
                line = json.dumps(dict(crawl_dic), ensure_ascii=False) + ',\n'
                print(line)
                self.file.write(line)
            #다음페이지 버튼 검색

            find_next_button = 0
            for j in range(len(self.driver.find_elements_by_xpath('//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/li'))):
                if self.driver.find_element_by_xpath(
                        '//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/li[{}]'.format(j + 1)).get_attribute(
                        'class') == 'num next-page':
                    find_next_button += 1
            if find_next_button == 0:
                break

    def next_page_button_click(self):
        if int(self.driver.find_element_by_xpath('//*[@id="page_jump"]').get_attribute('value')) != (self.page_count_num + 1):
            page_num_insert = self.driver.find_element_by_xpath('//*[@id="page_jump"]')
            page_num_insert.click()
            sleep(WAIT_TIME_SHORT)
            page_num_insert.clear()
            sleep(WAIT_TIME_SHORT)
            page_num_insert.send_keys(self.page_count_num + 1)
            sleep(WAIT_TIME_SHORT)
            page_num_insert.send_keys(Keys.RETURN)
            self.driver.find_element_by_xpath('//*[@id="myTable"]/table[2]/tbody/tr/td/div/ul/input[2]').send_keys(
                Keys.ENTER)

