import os
import sys
sys.path.append(os.getcwd())
from handle.home_page_handle import Home_page
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class home_page(object):
    def __init__(self,driver):
        self.home_page = Home_page(driver)

    # check home page three button
    def check_button(self,click_button,title_name):
        """
        click_button:about_zzmx
                     zzmx_material
                     QA_center
        title_name:关于真珠，真珠素材，答疑中心
        """
        self.home_page.click_button(click_button)
        return self.check_title_name(title_name)

    def check_title_name(self,title_name):
        """
        title_name include title and tabber's title
        """
        if self.home_page.get_title_name() == title_name:
            print("True")
            return True
        else:
            return False
    
    # check picture button
    def check_click_product_button(self,element,text):
        """
        home page:three product in the picture
        first element:first_picture
        second element:second_picture
        third element:third_picture
        """
        self.home_page.click_product_button(element)
        return self.check_product_title(text)

    def check_product_title(self,text):
        if self.home_page.get_product_detail_page_title() == text:
            return True
        else: 
            return False

    # check tabber
    def check_seller_tabber(self,title_name):
        self.home_page.click_seller_tabber()
        return self.check_tabber_title_name(title_name)

    def check_tabber_title_name(self,title_name):
        if self.home_page.get_seller_page_title() == title_name:
            return True
        else: 
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/home")
    a = home_page(driver)
    a.click_button("sharing_rule","分享规则")

    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC

    # driver = webdriver.Firefox()
    # driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/article?aId=11")
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "van-ellipsis"))
    #     )
    #     a=element.text
    #     print(a)
    # finally:
    #     driver.quit()