from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage
from test_appium.page.contactaddpage import ContactAddPage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_menul_element = (MobileBy.XPATH,"//*[@text='手动输入添加']")

    def addmenber_menual(self):
        self.find_and_click(self.addmember_menul_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        toasttext = self.get_toasttext()
        return toasttext