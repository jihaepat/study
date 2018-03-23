import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import keys
import unittest
from time import sleep

from selenium.webdriver.common.keys import Keys



class NewVisitorTest(unittest.TestCase):



    def setUp(self):
        # self.browser = webdriver.Chrome('/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/chromedriver')
        self.browser = webdriver.Firefox(executable_path = '/home/leehyunsoo/work/TDD/study/leehyunsoo/TDD/geckodriver')

        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        table = self.browser.find_element_by_id('id_list_table')

        inputbox.send_keys('공작깃털 사기')

        # sleep(5)
        inputbox.send_keys(Keys.ENTER)

        rows = table.find_elements_by_tag_name('td')

        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
            '신규 작업이 테이블에 표시되지 않는다 -- 해당 텍스트:\n%s' %(
                '123123'
            )
        )

        # self.assertIn('1: 공장깃털 사기', [row.text for row in rows])

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')