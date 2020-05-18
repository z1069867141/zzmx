import os
import sys
sys.path.append(os.getcwd())
from base.FindElement import FindElement
from selenium import webdriver
import time

class Shoplist_handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = ".\\config\\shop_product.ini"
        self.sl = FindElement(self.driver,file_path=self.file_path,node="not_logged_in_shop_list")

    def click_product_button(self):
        self.sl.get_element("product").click()
        return self.get_product_detail_text()
    
    def get_product_detail_text(self):
        try:
            text = self.sl.get_element("product_detail").text
            return text
        except:
            return None

    def switch_tabber_shopping_bag(self):
        self.sl.get_element("shopping_bag").click()
        return self.get_shopping_bag_title

    def get_shopping_bag_title(self):
        try:
            text = self.sl.get_element("shopping_bag_title").text
            return text
        except: 
            return None

    def click_search_button(self):
        self.sl.get_element("search_button").click()
        return self.get_search_text()

    def get_search_text(self):
        try:
            text = self.sl.get_element("search_text").text
            return text
        except:
            return None

    def click_share_button(self):
        time.sleep(2)
        self.sl.get_element("share_button").click()
        return self.get_login_text()

    def get_login_text(self):
        try:
            text = self.sl.get_element("login_button").text
            return text
        except: 
            return None

    def click_add_product_button(self):
        self.sl.get_element("add_shopping_bag_button").click()
        return self.get_login_text()