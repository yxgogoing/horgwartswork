import requests
from jsonpath import jsonpath
from hamcrest import *

class test_demo():
    # def test_hamcrest(self):
    #     r = requests.get('http://home.testing-stidio.com/categories.json')
    #     print(r.text())
    #     assert r.status_code == 200
    #     assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
    #     assert jsonpath(r.json(),'$..name')[0] == '霍格沃兹测试学院公众号'
    #     assert_that()

    def test_hamcrest(self):
        r = requests.get('http://home.testing-stidio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号')

