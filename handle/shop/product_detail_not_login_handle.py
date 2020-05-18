import os
import sys
sys.path.append(os.getcwd())
from base.FindElement import FindElement
from selenium import webdriver
import time

class Product_detail_handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = ".\\config\\shop_product.ini"
        self.pdh = FindElement(self.driver,file_path=self.file_path,node="not_logged_in_product_detail")

    def click_return_bottom(self):
        self.pdh.get_element("return_button").click()

    def get_product_detail_text(self):
        try:
            text = self.pdh.get_element("buy_product").text
            return text
        except:
            return None
    
    def click_return_shop_button(self):
        self.pdh.get_element("return_shop_button").click()

    def get_shop_list_title(self):
        try: 
            text = self.pdh.get_element("product_list_text").text
            return text
        except:
            return None

    def click_add_favourite_product(self):
        self.pdh.get_element("add_favourite_product")

    def get_login_button(self):
        try:
            text = self.pdh.get_element("login_button").text
            return text
        except:
            return None

    def click_shopping_bag(self):
        self.pdh.get_element("shopping_bag").click()

    def get_shopping_bag_title(self):
        try:
            text = self.pad.get_element("shopping_bag_title").text
            return text
        except:
            return None

    def click_share_button(self):
        time.sleep(2)
        self.pdh.get_element("share_product").click()

    def click_add_product_bag(self):
        self.pdh.get_element("add_shopping_bag").click()