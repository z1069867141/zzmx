import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class LoginSMSHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.Login = FindElement(self.driver)

    # 输入手机号
    def send_phone_number(self,phone_number):
        self.Login.get_element("phone_number").send_keys(phone_number)

    # 获取验证码
    def get_phone_code(self):
        self.Login.get_element("get_code").click()

    # 输入验证码
    def send_phone_code_element(self,code):
        self.Login.get_element("Verification_code").send_keys(code)
    
    # 点击登录
    def click_button(self):
        self.Login.get_element("login_button").click()

    # 获取错误信息
    def get_error_message(self):
        time.sleep(2)
        message = self.Login.get_element("error_message").text
        return message
    
    # 获取登录按钮文本
    def get_login_button_text(self):
        try:
            text = self.Login.get_element("login_button").text
            return text
        except:
            return None

    # 切换密码登录
    def click_switch_password(self):
        self.Login.get_element("get_password_mode").click()

    # 获取密码登录文案
    def click_switch_password_text(self):
        try:
            text = self.Login.get_element("get_password_mode").text
            return text
        except:
            return None

class Login_password_Handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.Login = FindElement(self.driver,file_path=None,node="LogPasswordElement")

    def send_phone_number(self,phone):
        self.Login.get_element("phone_number").send_keys(phone)

    def send_password_element(self,password):
        self.Login.get_element("phone_password").send_keys(password)

    def click_button(self):
        self.Login.get_element("login_button").click()

    def click_code_mode_button(self):
        self.Login.get_element("code_mode").click()

    def click_retrieve_the_password(self):
        self.Login.get_element("retrieve_the_password").click()

    # 获取验证码登陆时获取验证码按钮的文案
    def get_code_text(self):
        time.sleep(1)
        try:
            text = self.Login.get_element("get_code_text").text
            return text
        except: 
            return None

    # 获取找回密码返回登陆的文案
    def get_return_password_mode_text(self):
        time.sleep(1)
        try: 
            text = self.Login.get_element("return_password_mode_text").text
            return text
        except:
            return None
    
    # 获取错误信息
    def get_error_message(self):
        time.sleep(1)
        message = self.Login.get_element("error_message").text
        return message

    def get_login_button_text(self):
        time.sleep(1)
        try:
            text = self.Login.get_element("login_button").text
            return text
        except:
            return None

class Login_retireve_password_Handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.Login = FindElement(self.driver,file_path=None,node="Retrieve")

    def send_phone_number(self,phone):
        self.Login.get_element("phone_number").send_keys(phone)

    def send_phone_code(self,code):
        self.Login.get_element("Verification_code").send_keys(code)

    def send_password(self,password):
        self.Login.get_element("password").send_keys(password)

    def send_password_confirm(self,confirm_password):
        self.Login.get_element("confirm_password").send_keys(confirm_password)

    def click_get_verification_code(self):
        self.Login.get_element("get_code").click()

    def click_login_button(self):
        self.Login.get_element("login_button").click()
    
    def click_return_password_mode(self):
        self.Login.get_element("return_password_mode_button").click()

    def get_error_message(self):
        try:
            time.sleep(2)
            text = self.Login.get_element("error_message").text
            return text
        except: 
            return None
    
    def click_button(self):
        self.Login.get_element("login_button").click()


    # 判断返回登录按钮文案是否存在
    def get_return_password_button_text(self):
        try: 
            time.sleep(4)
            text = self.Login.get_element("return_password_mode_text").text
            return text
        except:
            return None

    

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/changepwd")
    element_a = Login_retireve_password_Handle(driver)
    # element_a.send_phone_number("15011111111")
    # element_a.send_password_element("Aa111111")
    element_a.click_return_password_mode()
    a = element_a.get_return_password_button_text()
    print(a)
    # element_a.click_button()