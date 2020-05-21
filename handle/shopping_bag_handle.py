import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class shopping_bag(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = os.path.join(os.getcwd()+"/config/"+"shopping_bag.ini")
        self.sb = FindElement(self.driver,file_path=self.file_path,node="shopping_bag")

    def get_text(self):
        try:
            text = self.sb.get_element("text").text
            return text
        except:
            return None

    def click_go_shopping_button(self):
        self.sb.get_element("go_to_shop_button")

    def get_shop_title(self):
        try:
            text = self.sb.get_element("shop_title").text
            return text
        except:
            return None