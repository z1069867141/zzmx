import os
import sys
sys.path.append(os.getcwd())
from handle.shop.product_detail_not_login_handle import Product_detail_handle
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class product_detail_business(object):
    def __init__(self,driver):
        self.detail = Product_detail_handle(driver)

    def click_return(self):
        self.detail.click_return_bottom()
        return self.check_product_title()

    def check_product_title(self):
        try:
            if self.detail.get_product_list_title()!="立即购买":
                return True
            else:
                return False
        except:
            return True

    def click_return_shop_button(self):
        self.detail.click_return_shop_button()
        return self.check_product_title()

    def check_product_title(self):
        if self.detail.get_shop_list_title() == "商铺":
            return True
        else:
            return False

    def click_add_favourite_button(self):
        self.detail.click_add_favourite_product()
        return self.check_login_button_text()
        
    def check_login_button_text(self):
        try:
            if self.detail.get_login_button() == "登录":
                return True
            else:
                return False
        except:
            return False
    
    def click_shopping_bag_button(self):
        self.detail.click_shopping_bag()
        return self.check_shopping_bag_title()

    def check_shopping_bag_title(self):
        try:
            if self.detail.get_shopping_bag_title() == "购物袋":
                return True
            else:
                return False
        except:
            return False
        
    def click_share(self):
        self.detail.click_share_button()
        return self.check_login_button_text()

    def click_add_product(self):
        self.detail.click_add_product_bag()
        return self.check_login_button_text()