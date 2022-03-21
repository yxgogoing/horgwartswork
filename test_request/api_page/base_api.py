import requests
import json


class BaseApi:
    """
    api的抽象类
    """
    def send_api(self, data: dict):
        """
        发送 api
        """
        print(json.dumps(data, indent=2)) # 每次打印请求数据
        return requests.request(**data).json()  # 解字典
