import requests

def test_demo():
    url = "http://httpbin.testing-studio.com/cookies"
    header = {
        'User-Agent': 'hogearts',
        'teacher':'AD'
    }
    cookie_data = {"hogwarts":"school"}
    r = requests.get(url=url, headers = header, cookies=cookie_data)
    print(r.request.headers)


111