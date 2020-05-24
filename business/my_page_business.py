import os
import sys
sys.path.append(os.getcwd())
from handle.my_page_handle import my_p
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class my_page(object):
    def __init__(self,driver):
        self.mp_b = my_p(driver)

    def click_set(self):
        self.mp_b.click_set_button()
        return self.check_shop_title()

    def click_talk(self):
        self.mp_b.click_talk_button()
        return self.check_shop_title()

    def click_login(self):
        self.mp_b.click_login_button()
        return self.check_shop_title()

    def click_all_order(self):
        self.mp_b.click_all_order_button()
        return self.check_shop_title()

    def click_wait_pay(self):
        self.mp_b.click_wait_pay_button()
        return self.check_shop_title()

    def click_good_to_be_received(self):
        self.mp_b.click_good_to_be_received_button()
        return self.check_shop_title()

    def click_to_be_delivered(self):
        self.mp_b.click_to_be_delivered_button()
        return self.check_shop_title()

    def click_received(self):
        self.mp_b.click_received_button()
        return self.check_shop_title()

    def click_my_wallet(self):
        self.mp_b.click_my_wallet_button()
        return self.check_shop_title()

    def click_my_favourite(self):
        self.mp_b.click_my_favourite_button()
        return self.check_shop_title()

    def click_my_customer_service(self):
        self.mp_b.click_my_customer_service_button()
        return self.check_shop_title()

    def check_shop_title(self):
        try:
            if self.mp_b.get_login_button_text()=="登录":
                return True
            else: 
                return False
        except:
            return False