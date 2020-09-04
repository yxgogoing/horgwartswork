# -*- coding:utf-8 -*-
#@Time   :2020/8/27 16:42
#@Author :yax
#@File   :Add_department_page.py
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from work6_PageObject.page.Contact_Page import ContactPage


class AddDepartment(BasePage):
    def add_department(self, department):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.NAME, 'name').send_keys(department)
        self.find(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body [id="1688853196058519_anchor"]').click()
        self.find(By.LINK_TEXT, '确定').click()
        return ContactPage()

    def get_department_error_message(self):
        return self.driver.find_element(By.ID, 'js_tips').text