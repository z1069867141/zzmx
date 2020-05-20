import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from reading_mode.read_ini import ReadIni
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindElement(object):
    def __init__(self, driver,file_path=None,node=None):
        self.driver = driver
        self.file_path = file_path
        self.node = node

    def get_element(self, key):
        read_ini = ReadIni(self.file_path,self.node)
        data = read_ini.get_value(key)
        data_list = data.split(">")
        by = data_list[0]
        value = data_list[1]
        if by == "classnames":
            No = int(data_list[2])
        try:
            if by == "id":
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, value)))
                return element
            elif by == "name":
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
                return element
            elif by == "classname":
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                return element
            elif by == "classnames":
                return self.driver.find_elements_by_class_name(value)[No]
            elif by == "xpath":
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
                return element
            elif by == "tag_name":
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, value)))
                return element
            elif by == "other":
                return value
        except:
            return None

    def scroll_get_element(self,value):
        js = "document.documentElement.scrollTop=300;"
        self.get_element(value)
        self.driver.execute_script(js)

if __name__ == "__main__":
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get("http://fanrongdemo.qianyansoft.com/Wap/#/detail?112?undefined")
    # element_a = FindElement(driver,file_path=".\\config\\shop_product.ini",node="not_logged_in_shop_list")
    # element_a.get_element("share_button").click()
    time.sleep(5)
    a = driver.find_element_by_tag_name("input")
    c = a.send_keys("2")
    time.sleep(2)
    b = a.get_attribute("placeholder")
    print(b)
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/article?aId=11")
#     file_path = os.path.join(os.getcwd()+"/config/"+"home_page_element.ini")
#     a = FindElement(driver,file_path=file_path,node="home_page")
#     a.get_element("title_name")