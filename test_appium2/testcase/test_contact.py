
import pytest
import yaml

from test_appium2.page.app import App


def get_contact():
    with open("../data/contacts.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

class TestWexin:
    def setup(self):
       """
        启动app
       """
       self.app = App()
       self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum',get_contact()[0])
    def test_addcontact(self,name,gender,phonenum):
        mypage = self.main.goto_addresslist().add_member().addmember_menual()\
        .edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save()

        mytoast = mypage.get_toast()
        assert mytoast == '添加成功'
    @pytest.mark.parametrize('name',get_contact()[1])
    def test_delcontact(self,delname):
        del_contact = self.main.back_and_click_contact().select_name().del_member()\
        .edit_member.search_name_id(delname)

        del_results = del_contact.get_results()
        print(f'删除结果：{del_results}')
        assert del_results == '无搜索结果'