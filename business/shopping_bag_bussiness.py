import os
import sys
sys.path.append(os.getcwd())
from handle.shopping_bag_handle import shopping_bag
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class shopping_b(object):
    def __init__(self,driver):
        self.sb = shopping_bag(driver)
    
    def check_text(self):
        try:
            if self.sb.get_text()=="这么多好产品，你都不加入购物袋么？":
                return True
            else: 
                return False
        except:
            return False

    def click_go_shopping(self):
        self.sb.click_go_shopping_button()
        return self.check_shop_title

    def check_shop_title(self):
        try:
            if self.sb.get_text()=="商铺":
                return True
            else: 
                return False
        except:
            return False