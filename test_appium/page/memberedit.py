from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage
from test_appium.page.mainpage import MainPage


class MemberEdit(BasePage):
    del_button = (MobileBy.ID, "com.tencent.wework:id/e_1")
    identify_button = (MobileBy.ID,"com.tencent.wework:id/bfe")
    def del_member(self):
         #点击删除按钮
        self.find_and_click(self.del_button)
         #点击确定删除
        self.find_and_click(self.identify_button)

        return MainPage(self.driver)



