import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from cfg import *


class Login_UI:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # 禁用Chrome的日志记录功能
        options.add_experimental_option('excludeSwitches', ['enable=logging'])

        self.wd = webdriver.Chrome(options=options)
        # 设置隐式等待时间为10秒
        self.wd.implicitly_wait(10)

    def login(self, username="jinyong", password="123456"):
        self.wd.get(loginurl)
        elements = self.wd.find_elements(By.CSS_SELECTOR, '.el-input__inner')
        elements[0].clear()
        elements[0].send_keys(username)
        elements[1].clear()
        elements[1].send_keys(password)
        element = self.wd.find_element(By.TAG_NAME, 'button')
        element.click()


login_ui = Login_UI()


