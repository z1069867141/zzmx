import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class my_p(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = os.path.join(os.getcwd()+"/config/"+"my_information.ini")
        self.mp = FindElement(self.driver,file_path=self.file_path,node="information")

    def click_set_button(self):
        self.mp.get_element("set_button").click()

    def click_talk_button(self):
        self.mp.get_element("talk").click()

    def click_login_button(self):
        self.mp.get_element("login_button").click()

    def click_all_order_button(self):
        self.mp.get_element("all_order").click()

    def click_wait_pay_button(self):
        self.mp.get_element("wait_pay_button").click()

    def click_good_to_be_received_button(self):
        self.mp.get_element("good_to_be_received").click()

    def click_to_be_delivered_button(self):
        self.mp.get_element("to_be_delivered").click()

    def click_received_button(self):
        self.mp.get_element("received").click()

    def click_my_wallet_button(self):
        self.mp.get_element("my_wallet").click()

    def click_my_favourite_button(self):
        self.mp.get_element("my_favourite").click()

    def click_my_customer_service_button(self):
        self.mp.get_element("customer_service").click()

    def get_login_button_text(self):
        try:
            text = self.mp.get_element("login_page_button").text
            return text
        except:
            return None