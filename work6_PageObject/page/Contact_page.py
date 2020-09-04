# -*- coding:utf-8 -*-
#@Time   :2020/8/27 17:45
#@Author :yax
#@File   :Contact_page.py
from selenium.webdriver.common.by import By
from work6_PageObject.page.base_page import BasePage

class ContactPage(BasePage):
    def go_to_add_department(self):
        from work6_PageObject.page.add_department_page import AddDepartment
        return AddDepartment(self.driver)

    def get_department_list(self):
        name_list = self.finds(By.CSS_SELECTOR, ".jstree-anchor")
        list1 = []

        for name in name_list:
            list1.append(name.text)
        return list1
