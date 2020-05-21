import os
import sys
sys.path.append(os.getcwd())
from business.shopping_bag_bussiness import shopping_b
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class sb_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/shoppingcart")
        self.sb = shopping_b(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_text(self):
        self.logger.info("this is test_text")
        result = self.sb.check_text()
        self.assertTrue(result,"test_text run")

    def test_click_go_shopping_button(self):
        self.logger.info("this is test_click_go_shopping_button")
        result = self.sb.click_go_shopping()
        self.assertTrue(result,"test_click_go_shopping_button run")

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(sb_test("test_click_go_shopping_button"))
    unittest.TextTestRunner().run(suit)