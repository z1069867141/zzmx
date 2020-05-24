import os
import sys
sys.path.append(os.getcwd())
from business.my_page_business import my_page
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class mp_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/newusercenter")
        self.mp = my_page(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_click_set(self):
        self.logger.info("this is test_click_set")
        result = self.mp.click_set()
        self.assertTrue(result,"test_click_set run")

    def test_click_talk(self):
        self.logger.info("this is test_click_talk")
        result = self.mp.click_talk()
        self.assertTrue(result,"test_click_talk run")

    def test_click_login(self):
        self.logger.info("this is test_click_login")
        result = self.mp.click_login()
        self.assertTrue(result,"test_click_login run")

    def test_click_all_order(self):
        self.logger.info("this is test_click_all_order")
        result = self.mp.click_all_order()
        self.assertTrue(result,"test_click_all_order run")

    def test_click_wait_pay(self):
        self.logger.info("this is test_click_wait_pay")
        result = self.mp.click_wait_pay()
        self.assertTrue(result,"test_click_wait_pay run")

    def test_click_good_to_be_received(self):
        self.logger.info("this is test_click_good_to_be_received")
        result = self.mp.click_good_to_be_received()
        self.assertTrue(result,"test_click_good_to_be_received run")

    def test_click_to_be_delivered(self):
        self.logger.info("this is click_to_be_delivered")
        result = self.mp.click_to_be_delivered()
        self.assertTrue(result,"click_to_be_delivered run")

    def test_click_received(self):
        self.logger.info("this is test_click_received")
        result = self.mp.click_received()
        self.assertTrue(result,"test_click_received run")

    def test_click_my_wallet(self):
        self.logger.info("this is test_click_my_wallet")
        result = self.mp.click_my_wallet()
        self.assertTrue(result,"test_click_my_wallet run")

    def test_click_my_favourite(self):
        self.logger.info("this is test_click_my_favourite")
        result = self.mp.click_my_favourite()
        self.assertTrue(result,"test_click_my_favourite run")

    def test_click_my_customer_service(self):
        self.logger.info("this is test_click_my_customer_service")
        result = self.mp.click_my_customer_service()
        self.assertTrue(result,"test_click_my_customer_service run")

if __name__ == "__main__":
    # suit = unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(mp_test("test_click_my_favourite"))
    unittest.TextTestRunner().run(suit)