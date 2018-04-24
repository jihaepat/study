from selenium import webdriver
import time

path = '/home/yoonjae/study/yoon/crawl/chromedriver'

driver = webdriver.Chrome(path)
driver.get('http://www.shangbiao.com/tm-search?')
driver.implicitly_wait(3)
elem = driver.find_element_by_name('brand_name')
# elem.clear()
elem.send_keys('6051503')
elem.click()
elem.submit()
elem.close()