import os
import sys
sys.path.append(os.getcwd())
from business.home_page_business import home_page
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class hp_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/")
        self.hp = home_page(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_about_zzmx_button(self):
        self.logger.info("this is test_about_zzmx_button")
        result = self.hp.check_button("about_zzmx","关于真珠")
        self.assertTrue(result,"test_about_zzmx_button run")

    def test_zzmx_material_button(self):
        self.logger.info("this is test_zzmx_material_button")
        result = self.hp.check_button("zzmx_material","真珠素材")
        self.assertTrue(result,"test_zzmx_material_button run")

    def test_QA_center(self):
        self.logger.info("this is test_QA_center")
        result = self.hp.check_button("QA_center","产品解答")
        self.assertTrue(result,"test_QA_center run")

    def test_first_product(self):
        self.logger.info("this is test_first_product")
        result = self.hp.check_click_product_button("first_picture","立即购买")
        self.assertTrue(result,"test_first_product run")

    def test_second_product(self):
        self.logger.info("this is test_second_product")
        result = self.hp.check_click_product_button("second_picture","立即购买")
        self.assertTrue(result,"test_second_product run")

    def test_third_product(self):
        self.logger.info("this is test_third_product")
        result = self.hp.check_click_product_button("third_picture","立即购买")
        self.assertTrue(result,"test_third_product run")

    def test_seller_tabber(self):
        self.logger.info("this is test_seller_tabber")
        result = self.hp.check_seller_tabber("商铺")
        self.assertTrue(result,"test_seller_tabber run")

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
    # suit.addTests(login_test("test_login_forward_process"))
    # suit.addTest(login_test("test_login_switch_sms_to_password"))
    # suit.addTest(login_test("test_login_switch_sms_to_password"))
    # suit.addTest(login_test("test_login_switch_sms_to_password"))
    suit.addTest(hp_test("test_third_product"))
    # suit.addTest(login_test("test_login_code_error"))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    runner.run(suit)