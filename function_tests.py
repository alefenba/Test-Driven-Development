from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.broser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()