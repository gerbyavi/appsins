from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest

class NewVisitorTest(LiveServerTestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

    def test_post_request(self):
#        self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('B005XUNG5I')
        inputbox.send_keys(Keys.ENTER) # DF2 import Keys from selenium.webdriver.common.keys import Keys
        self.check_above_post_request_found_in_html_table('B005XUNG5I') # calling yazum function - not start with word test

    def check_above_post_request_found_in_html_table(self, textaje):
        table = self.browser.find_element_by_id('id_list_table') # catching table
        rows = table.find_elements_by_tag_name('tr') # catching table's rows
#        self.assertIn(textaje, [row.text for row in rows]) # checking expected text create with send keys found in html

    def test_r_u_invited(self):  #4
        # Gerby goes to his site
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('ASINS', self.browser.title)  #5
        self.fail('Finish the test!')  #6

#if __name__ == '__main__':  #7
#    unittest.main(warnings='ignore')  #
