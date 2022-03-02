import requests
import json

corpid = 'wwf5102788743115b9'
corpsecret = '9Z7qRu5BaktsdGWFeaxRBjIKcaJwl4Qf44SVnMEjdJw'

def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result['access_token']

def test_get():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    print(requests.get(url.json()))

def test_add():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    date ={
        "userid" : "labixiaoxin",
        "name" : "蜡笔小新",
        "mobile" : "18620048156"
    }
    requests.post(url,json=date)
    '''转成json格式'''

