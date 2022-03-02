from selenium.webdriver.common.by import By
from test_framework.basepage import BasePage


class DemoPage(BasePage):
    _search_button=(By.ID,'home_search')

    #todo：po的数据驱动
    #todo是标记需进一步修改迭代，pycharm中Alt + 6快捷键可调出项目中的全部todo注释
    def login(self, username, password):
        pass

    def forget_password(self):
        pass

    def search(self,keyword):
        self.po_run('search', keyword=keyword)
        return self

    def back(self):
        self.po_run('back')
        return self
