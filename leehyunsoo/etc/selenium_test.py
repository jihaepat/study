from selenium import webdriver

def ttt():
    driver = webdriver.Chrome('/home/leehyunsoo/4TB/chromedriver/chromedriver')
    driver.get('http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=lee&oq=%25ED%2593%25A8%25E3%2585%259C%25E3%2585%25A1&rsv_pq=9dc1d0a400010ecd&rsv_t=52c7zyHhk4X9e7vl3BCI41u4%2BE9gNzTdS7ct3SAy8Zalr%2FSuOzy6pinyB3M&rqlang=cn&rsv_enter=1&inputT=2084&rsv_sug3=15&rsv_sug1=11&rsv_sug7=100&rsv_sug2=0&rsv_sug4=5492')
    img = driver.find_element_by_xpath('//*[@id="4"]/h3/a')
    print(img.get_attribute('href'))

ttt()