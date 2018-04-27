from selenium import webdriver
chromedriver = '/home/yoonjae/study/yoon/crawl/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=2')

def page_count():
    for i in range(len('//*[@id="annTB"]/tbody')-1):
        print(i)
        return i
def info_crawl():

    pass

def image_chrawl():
    pass