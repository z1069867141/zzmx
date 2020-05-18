import os
import sys
sys.path.append(os.getcwd())
from business.shop_business.shop_detail_not_login_business import product_detail_business
from selenium import webdriver
import unittest
from log.user_log import userlog

class product_detail_not_login_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Chrome()
        self.driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/detail?112?undefined")
        self.sd = product_detail_business(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_click_return_button(self):
        self.logger.info("this is test_click_return_button")
        result = self.sd.click_return()
        self.assertTrue(result,"test_click_return_button run")

    def test_click_return_shop_button(self):
        self.logger.info("this is test_click_return_shop_button")
        result = self.sd.click_return_shop_button()
        self.assertTrue(result,"test_click_return_shop_button run")

    def test_click_add_favourite_product(self):
        self.logger.info("this is test_click_add_favourite_product")
        result = self.sd.click_add_favourite_button()
        self.assertTrue(result,"test_click_add_favourite_product run")

    def test_click_shopping_bag(self):
        self.logger.info("this is test_click_shopping_bag")
        result = self.sd.click_shopping_bag_button()
        self.assertTrue(result,"test_click_shopping_bag run")
    
    def test_click_share_button(self):
        self.logger.info("this is test_share_button")
        result = self.sd.click_share()
        self.assertTrue(result,"test_share_button run")

    def test_click_add_shopping_button(self):
        self.logger.info("this is test_click_add_shopping_button")
        result = self.sd.click_add_product()
        self.assertTrue(result,"test_click_add_shopping_button run")

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(product_detail_not_login_test("test_click_add_shopping_button"))
    unittest.TextTestRunner().run(suit)