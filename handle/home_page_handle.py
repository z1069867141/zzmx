import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class Home_page(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = os.path.join(os.getcwd()+"/config/"+"home_page_element.ini")
        self.home_page = FindElement(self.driver,file_path=self.file_path,node="home_page")

    # into three button
    def click_button(self,button):
        self.home_page.get_element(button).click()
        return self.get_title_name()

    # return title name
    def get_title_name(self):
        try:
            time.sleep(2)
            text = self.home_page.get_element("title_name").text
            print(text)
            return text
        except:
            return None

    # into product detail
    def click_product_button(self,element):
        T = True
        while T:
            try:
                self.home_page.get_element(element).click()
                T = False
                return self.get_product_detail_page_title()
            except:
                self.home_page.scroll_get_element(element)


    # get product product detail page title
    def get_product_detail_page_title(self):
        try: 
            time.sleep(2)
            text = self.home_page.get_element("product_detail_text").text
            return text
        except:
            return None

    def click_seller_tabber(self):
        self.home_page.get_element("seller_tabber").click()
        return self.get_seller_page_title()
        
    def get_seller_page_title(self):
        try: 
            time.sleep(2)
            text = self.home_page.get_element("seller_header").text
            return text
        except:
            return None

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/")
    time.sleep(2)
    # driver.find_element_by_class_name("first").click()
    js = "document.documentElement.scrollTop=500;"
    t = True
    while t:
        try:
            driver.find_element_by_class_name("first").click()
            t=False
        except:
            driver.execute_script(js)
    # a = Home_page(driver)
    # # time.sleep(2)
    # a.get_title_name()

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
#     print(element.text)
# finally:
#     driver.quit()