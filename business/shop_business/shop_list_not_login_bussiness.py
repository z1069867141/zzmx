import os
import sys
sys.path.append(os.getcwd())
from handle.shop.shop_list_not_login_handle import Shoplist_handle
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class Shoplist_business(object):
    def __init__(self,driver):
        self.list = Shoplist_handle(driver)

    def click_product(self):
        self.list.click_product_button()
        return self.check_product_detail_text()

    def check_product_detail_text(self):
        if self.list.get_product_detail_text() == "立即购买":
            return True
        else:
            return False

    def click_switch_tabber(self):
        self.list.switch_tabber_shopping_bag()
        return self.check_tabber_title()

    def check_tabber_title(self):
        if self.list.get_shopping_bag_title()=="购物袋":
            return True
        else: 
            return False

    def click_search(self):
        self.list.click_search_button()
        return self.check_search_text()

    def check_search_text(self):
        if self.list.get_search_text()=="最近搜索":
            return True
        else: 
            return False

    def click_share(self):
        self.list.click_share_button()
        return self.check_login_text()

    def check_login_text(self):
        if self.list.get_login_text()=="登录":
            return True
        else:
            return False

    def click_add_product(self):
        self.list.click_add_product_button()
        return self.check_login_text()