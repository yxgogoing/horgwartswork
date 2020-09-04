import shelve
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

loginurl = 'https://work.weixin.qq.com/wework_admin/frame#index'


class Test_wecomeImportCintacts():
    def setup(self):
        # 复用浏览器,获取cookie
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # 添加隐士等待，避免因响应太慢定位不到元素
        self.driver.implicitly_wait(5)
       

    def teardown(self):
        #执行完后关闭浏览器
        self.driver.quit()

    #获取cookie，并保存到shelve
    def test_cookie(self):
        self.driver.get(loginurl)
        # cookies = self.driver.get_cookies()
        # print(cookies)
        #将cookie保存到shelve数据库中
        db = shelve.open("mydb/logincookie")
        # db['cookie'] = cookies
        # 读取shelve中的cookie数据
        cookies = db['cookie']
        db.close()
        # self.driver.get(loginurl)

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get(loginurl)
        # 进入导入通讯录选项
        self.driver.find_element_by_xpath("//span[contains(.,'导入通讯录')]").click()
        # 上传一个xls文件
        upload = self.driver.find_element_by_xpath("//input[@id='js_upload_file_input']")
        upload.send_keys("C:\/Users\pc\通讯录.xlsx")
        # 断言
        assert "通讯录" in self.driver.find_element_by_id("upload_file_name").text

        time.sleep(3)


