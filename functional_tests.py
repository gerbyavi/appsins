from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_r_u_invited(self):  #4
        # Gerby goes to his site
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('ASINS', self.browser.title)  #5
        self.fail('Finish the test!')  #6

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #
