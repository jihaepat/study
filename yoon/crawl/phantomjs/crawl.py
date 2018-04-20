from selenium import webdriver

driver = webdriver.PhantomJS() # or add to your PATH
driver.set_window_size(1024, 768) # optional
driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1')
print(driver.find_element_by_xpath('//*[@id="annTB"]/tbody/tr[2]/td[4]'))

# driver.get('http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1')
# enter = driver.find_element_by_xpath('//*[@id="loadWin"]/input')
# enter.click()
# html = driver.page_source
# print(html)
