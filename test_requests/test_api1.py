import requests

corpid = 'wwf5102788743115b9'
corpsecret = '9Z7qRu5BaktsdGWFeaxRBjIKcaJwl4Qf44SVnMEjdJw'

#获取token
def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result['access_token']

#创建部门
def test_add_department():
    url =f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}"
    data = {
        "name":"测试3部",
        "parentid":"1",
    }
    r = requests.post(url,json=data).json().get("errcode")
    print(r)

