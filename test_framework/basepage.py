
#个人理解：basepage中放基本的操作方法，po的执行结合yam定义成key来调用这些操作


import logging

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _driver:WebDriver = None
    _current_element: WebElement = None

    def start(self):

       caps = {
           'platformName': 'android',
           'deviceName': 'ceshiren.com',
           'appPackage': 'com.xueqiu.android',
           'appActivity': '.view.WelcomeActivityAlias',
           'noReset': True
       }
       self._driver = webdriver.Remote('127.0.0.1:4723/wd/hub',caps)
       self._driver.implicitly_wait(20)
       return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    def po_run(self, po_method, **kwargs):
        with open('page_demo.yaml') as f:
            yaml_data = yaml.safe_load(f)

            for step in yaml_data[po_method]:

                if isinstance(step, dict):
                # isinstance判断类型的函数，判断step是否是dict
                    for key in step.keys():
                        if key == 'id':
                            locator = (By.ID, step[key])
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            text = str(step[key])
                            for k,v in kwargs.items():
                                text = text.replace('${' + k +'}', v)
                                self.send_keys(text)
                        #key还可以添加其他步骤，如页面返回，滑动，web最大化窗口等基本操作
                        else:
                            logging.error(f"dont know {step}")



