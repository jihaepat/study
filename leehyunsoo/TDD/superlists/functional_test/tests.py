import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import keys
import unittest
from time import sleep


from selenium.webdriver.common.keys import Keys



class NewVisitorTest(LiveServerTestCase):



    def setUp(self):

        self.browser = webdriver.Chrome('/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/chromedriver')
        # self.browser = webdriver.Chrome()
        # self.browser = webdriver.Firefox(executable_path = '/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/geckodriver')
        # self.browser = webdriver.Firefox(executable_path = '/Users/leehyunsoo/work/TDD/study/leehyunsoo/TDD/geckodriver')


    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        # table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_id('td')
        self.assertIn(row_text, ([rows[x].text for x in range(len(rows))]))

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1: 공작깃털 사기')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        self.browser.quit()
        self.browser = webdriver.Chrome('/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/chromedriver')
        # self.browser = webdriver.Firefox(executable_path = '/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/geckodriver')

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('공작깃털 사기', page_text)
        self.assertNotIn('그물 만들기', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('우유 사기')
        inputbox.send_keys(Keys.ENTER)

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        print(page_text)
        self.assertIn('공작깃털 사기', page_text)
        self.assertIn('우유 사기', page_text)

        self.fail('Finish the test!')