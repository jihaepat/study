import scrapy
import keyboard
from selenium import webdriver
from time import sleep


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class spider_url(scrapy.Spider):
    name = 'CR'
    option = webdriver.ChromeOptions()
    option.add_argument('user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    driver = webdriver.Chrome('/media/yoonjae/4TB2/chromedriver', chrome_options=option)


    def start_requests(self):

        try:
            title = WebDriverWait(self.driver, 100) \
                .until(EC.presence_of_element_located((By.XPATH, '//*[@id="txnS02"]/a')))
            print(title.text)
        finally:
            sleep(3)
            button = self.driver.find_element_by_xpath(
                '//*[@id="txnS02"]/a')
            button.click()
            button.send_keys('息中心')
            sleep(1)

        self.driver.quit()
