from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.Chrome('/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title