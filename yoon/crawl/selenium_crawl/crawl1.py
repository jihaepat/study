from bs4 import BeautifulSoup
from selenium import webdriver

chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'
driver = webdriver.Chrome(chromedriver)
# driver = webdriver.PhantomJS()
driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=2')

for i in range(len('//*[@id="annTB"]/tbody')-1):
    info_data = driver.find_element_by_xpath('//*[@id="annTB"]/tbody/tr[{}]'.format(i + 1))
    print(info_data.text)

# for i in range(len('//*[@id="annTB"]/tbody')-1):
img_data = driver.find_element_by_xpath('//*[@id="annTB"]/tbody/tr[2]/td[8]/a'.format(i + 2))
img_data.click()
driver.implicitly_wait(10)
img_data_url = driver.find_element_by_xpath('//*[@id="imgs"]')
print(img_data_url.text)
img_data_close = driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/a')
img_data_close.click()
#     img_data_url =driver.find_element_by_xpath('//*[@id="list_shot"]/ul/li[{}]'.format(i + 1))
#     print(img_data_url.text)

# //*[@id="imgs"]