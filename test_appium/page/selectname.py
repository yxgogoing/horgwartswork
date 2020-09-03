from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage

from test_appium.page.memberedit import MemberEdit


class SelectMember(BasePage):
    click_back_element = (MobileBy.XPATH, "//*[@text='zh1']")

    def select_member(self):
        self.find_and_click(self.click_back_element)
        self.driver.implicitly_wait(5)

        return MemberEdit(self.driver)