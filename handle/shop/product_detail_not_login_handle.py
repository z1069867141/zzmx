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
        self.pdh.get_element("add_favourite_product").click()

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
            text = self.pdh.get_element("shopping_bag_title").text
            return text
        except:
            return None

    def click_share_button(self):
        time.sleep(2)
        self.pdh.get_element("share_product").click()

    def click_add_product_bag(self):
        self.pdh.get_element("add_shopping_bag").click()

    def click_buy_button(self):
        self.pdh.get_element("buy_product").click()

    def get_confirm_button_text(self):
        try:
            text = self.pdh.get_element("confirm_button").text
            return text
        except:
            return None

    def click_buy_confirm_button(self):
        self.pdh.get_element("confirm_button").click()

    def click_plus_product_button(self):
        self.pdh.get_element("plus_product").click()

    def click_mins_product_button(self):
        self.pdh.get_element("mins_produt").click()

    def get_mins_toast_error(self):
        try:
            text = self.pdh.get_element("mins_product_error").text
            return text
        except:
            return None

    def send_product_quantity(self,value):
        self.pdh.get_element("quantity_element_text").send_keys(value)

    def get_quantity_text(self):
        try: 
            element = self.pdh.get_element("quantity_element_text")
            text = element.get_attribute(self.pdh.get_element("quantity_element"))
            return text
        except: 
            return None

    def click_close_button(self):
        self.pdh.get_element("close_button").click()

    def get_choose_quantity_text(self):
        try:
            text = self.pdh.get_element("choose_quantity_button").text
            return text
        except:
            return None