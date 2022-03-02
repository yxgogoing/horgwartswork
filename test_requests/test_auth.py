import requests
from requests.auth import HTTPBasicAuth
def test_auth():
    r = requests.get(url='http://httpbin.testing-studio.com/basic-auth/yx/111',
                 auth=HTTPBasicAuth("yx","123"))
    print(r.text)

