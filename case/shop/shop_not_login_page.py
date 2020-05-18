import os
import sys
sys.path.append(os.getcwd())
from business.shop_business.shop_list_not_login_bussiness import Shoplist_business
from selenium import webdriver
import unittest
from log.user_log import userlog

class shop_not_login_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Chrome()
        self.driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/seller")
        self.sp = Shoplist_business(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_click_product_button(self):
        self.logger.info("this is test_click_product_button")
        result = self.sp.click_product()
        self.assertTrue(result,"test_click_product_button run")

    def test_switch_tabber_shopping_bag(self):
        self.logger.info("this is test_switch_tabber_shopping_bag")
        result = self.sp.click_switch_tabber()
        self.assertTrue(result,"test_switch_tabber_shopping_bag run")
    
    def test_click_search_button(self):
        self.logger.info("this is test_click_search_button")
        result = self.sp.click_search()
        self.assertTrue(result,"test_click_search_button run")

    def test_click_share_button(self):
        self.logger.info("this is test_lick_share_button")
        result = self.sp.click_share()
        self.assertTrue(result,"test_lick_share_button run")

    def test_click_add_product_button(self):
        self.logger.info("this is test_click_add_product_button")
        result = self.sp.click_add_product()
        self.assertTrue(result,"test_click_add_product_button run")

if __name__ == "__main__":
    report_file_path = os.path.join(os.getcwd()+"/report/"+"login.html")
    f = open(report_file_path,"wb")
    # suit = unittest.main()
    """
    指定执行的test
    suit = unittest.TestSuite()
    suit.addTests(login_test("test_login_forward_process"))
    unittest.TextTestRunner().run(suit)
    """
    suit = unittest.TestSuite()
    suit.addTest(sp_test("test_click_add_product_button"))
    # suit.addTest(login_test("test_login_code_error"))
    unittest.TextTestRunner().run(suit)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    # runner.run(suit)