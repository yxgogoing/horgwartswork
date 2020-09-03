from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslistpage import AddressListPage
from test_appium.page.basepage import BasePage
from test_appium.page.selectname import SelectMember


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH,"//*[@text='通讯录']")
    back_button = (MobileBy.ID,"com.tencent.wework:id/hjo")
    def goto_addresslist(self):
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)

    def back_and_click_contact(self):
        sleep(5)
        #点击返回通讯录
        self.find_and_click(self.back_button)
        #点击通讯录
        self.find_and_click(self.addresslist_element)
        return SelectMember(self.driver)

