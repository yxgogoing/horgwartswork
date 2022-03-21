# 创建utils类，所有的业务函数都需要获取token，所有放在utils类中，utils类不能多
from test_request.api_page.base_api import  BaseApi


class WeWorkUtils(BaseApi):
    # 加_使get_token只能在类内调用token
    def get_token(self, corpsecret,corpid='wwwesaa'):
        data = {
           "method": "get",
           "url": f"https://...",
           "params": {"corpid": corpid, "corpsecret": corpsecret}
        }

        result = self.send_api(data)
        return result["access_token"]
