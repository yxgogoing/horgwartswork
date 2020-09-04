# -*- coding:utf-8 -*-
#@Time   :2020/8/27 16:01
#@Author :yax
#@File   :Base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _url = ""

    def __init__(self,driver_base=None):
        # print("driver_base的值时", driver_base)
        if driver_base is None:
            option = Options()
            option = Options
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver:WebDriver = driver_base

        if self._url != "":
            self.driver.get(self._url)

        #隐士等待
        self.driver.implicitly_wait(3)

        def find(self,by,value):
            return self.driver.find_element(by=by, value=value)

        def fins(self,by,value):
            return self.driver.find_element(by=by, value=value)

        def base_quit(self):
            return self.driver.quit()
