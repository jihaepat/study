import scrapy
import pyautogui
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup


class spider_url(scrapy.Spider):
    name = 'CR'
    chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.get('http://www.shangbiao.com/search')

    def start_requests(self):
        insert_data = self.driver.find_element_by_xpath('//*[@id="sub_button"]')
        insert_data.send_keys('张永杰')
        insert_data.send_keys(Keys.RETURN)
        search_name = self.driver.find_element_by_xpath('//*[@id="namebrand"]')
        #마우스 움직임 발생
        pyautogui.moveRel(0, 10)
        sleep(0.2)
        pyautogui.moveRel(0, -10)
        search_name.send_keys(Keys.RETURN)
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="sel_page_size"]').click()
        self.driver.find_element_by_xpath('//*[@id="sel_page_size"]/option[3]').click()
        temp = self.driver.find_element_by_xpath('//*[@id="page_jump"]')
        print(temp)
        for i in range(50):
            name = self.driver.find_element_by_xpath('//*[@id="ajbrandsearch"]/tr[{}]/td[3]/ul/li[1]/div/a'.format(i+1))
            origin_number = self.driver.find_element_by_xpath('//*[@id="ajbrandsearch"]/tr[{}]/td[5]/ul/li[1]/div'.format(i+1))
            print(name.text, origin_number.text)
