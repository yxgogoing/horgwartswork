# -*- coding:utf-8 -*-
#@Time   :2020/8/27 16:21
#@Author :yax
#@File   :main_page.py
from selenium.webdriver.common.by import By


from work6_PageObject.page.Base_page import BasePage
from work6_PageObject.page.Contact_page import ContactPage

class MainPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def go_to_contact(self):
        self.find(By.ID, "menu_contacts").click()

        return ContactPage(self.driver)
