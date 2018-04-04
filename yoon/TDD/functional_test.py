from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('일정관리', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('일정목록', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_arrtibute('placeholder'), '할일을 입력하세요')

        inputbox.send_keys('시장에서 미역 사기')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1:시장에서 미역 사기'for row in rows))

        self.fail('테스트 종료')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
