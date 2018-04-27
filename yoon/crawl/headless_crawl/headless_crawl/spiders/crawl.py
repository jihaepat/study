import scrapy
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from headless_crawl.items import HeadlessCrawlItem
from selenium import webdriver


class ch_spider(scrapy.Spider):
    name ='HCrawl'

    chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/homePage.html')
    end_page = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]')
    end_page = int(end_page.text[1:-1])
    print(end_page)

    def start_requests(self):
        for i in range(1595, self.end_page): #
            self.driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum={}'.format(i+1))
            cat_button = self.driver.find_element_by_xpath('//*[@id="annTypes"]/option[2]')
            sleep(0.5)
            cat_button.click()
            ok_button = self.driver.find_element_by_xpath('//*[@id="loadWin"]/input')
            ok_button.click()
            sleep(7)
            img_button = self.driver.find_element_by_xpath('//*[@id="annTB"]/tbody/tr[2]/td[8]/a')
            img_button.click()

            try:
                title = WebDriverWait(self.driver, 10) \
                    .until(EC.presence_of_element_located((By.CSS_SELECTOR, '#list_shot > ul > li.newclass > img')))
                print(title.text)
            finally:
                end_url_page_click = self.driver.find_element_by_xpath('//*[@id="downdiv"]/span[10]/a')
                end_url_page_click.click()
                sleep(3)
                end_page_num = int(self.driver.find_element_by_xpath('//*[@id="nowPage"]').get_attribute('value'))
                end_page_num_div = int(end_page_num / 20)

                reset_page = self.driver.find_element_by_xpath('//*[@id="downdiv"]/span[7]/a')
                reset_page.click()
                self.driver.find_element_by_xpath('//*[@id="nowPage"]').clear()

            for next_page in range(end_page_num_div+1):
                sleep(1)
                if end_page_num >(next_page) * 20 + 4:
                    self.driver.find_element_by_xpath('//*[@id="nowPage"]').clear()
                    self.driver.find_element_by_xpath('//*[@id="nowPage"]').send_keys((next_page) * 20 + 4)
                sleep(1)
                self.driver.find_element_by_xpath('//*[@id="nowPage"]').send_keys(Keys.RETURN)
                sleep(1)
                img_url_save = self.driver.find_elements_by_xpath('//*[@id="list_shot"]/ul/li/img')
                for x in img_url_save:
                    if x.get_attribute('src') != '':
                        print(x.get_attribute('src'))
                print('-' * 30, '(', next_page+1, ')')



            # img_close_button = self.driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/a')
            # img_close_button.click()


                # for i in range(20):
                #     img_url_save = self.driver.find_element_by_xpath('//*[@id="list_shot"]/ul/li[{}]/img'.format(i+1))
                #     print(img_url_save.get_attribute('src'))
                # print('-' * 30, '(', next_page + 1, ')')
                #
