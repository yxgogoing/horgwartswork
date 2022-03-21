import requests
from test_request.api_page.base_api import BaseApi
from test_request.api_page.wework_utils import WeWorkUtils


class AddressPage(BaseApi):
    """
    通讯录管理,包括增删改查
    """

    def __init__(self):
        _corpsecret = "xxx"
        utils = WeWorkUtils()
        self.token = utils.get_token(_corpsecret)  # 下面的每个方法都会调get_token，所以设成类属性

    def get_member_info(self):
        # 获取成员信息接口
        data = {
            "method": "get",
            "url": f"https://...",
            "params": {"access_token": self.token,
                       "userid": "labixiaoxin"}
        }
        return self.send_api(data)

    def add_member(self):
        url = f"https://...access_token={self.token}"
        # data只填必填的参数
        data = {
            "json": {"userid": "labixiaoxin",
                    "name": "蜡笔小新",
                    "mobile": "11211111",
                    "department": [1]}
        }
        return self.send_api(data)

    def delete_member(self):
        # 删除
        data = {
            "url": f"https://...access_token={self.token}",
            "methon": "get"
        }
        return self.send_api(data)

    def update_member(self):
        url = f"https://...access_token={self.token}"
        data = {
            "method": "post",
            "url": f"https://...access_token={self.token}",
            "json": {
                "userid": "labixiaoxin",
                "name": "wangwu",
                "mobile": "11211111"
            }
        }
        return self.send_api(data)





