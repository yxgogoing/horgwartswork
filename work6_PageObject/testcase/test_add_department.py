# -*- coding:utf-8 -*-
#@Time   :2020/8/27 18:39
#@Author :yax
#@File   :test_add_department.py
from work6_PageObject.page.Add_department_page import AddDepartment
from work6_PageObject.page.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def test_add_department(self):
        result = self.main.go_to_contact().go_to_add_department().add_department('测试部').get_department_list()
        assert 'cf' in result

    def test_add_department_fail(self):
        self.main.go_to_contact().go_to_add_department().add_department('')
        result = AddDepartment(self.main.driver).get_department_error_message()
        assert '请输入部门名称' == result

    def teardown(self):
        self.main.base_quit()