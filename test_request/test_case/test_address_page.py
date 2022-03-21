from test_request.api_page.address_page import AddressPage


class TestAddressPage:
    # 以下实现是方法级别的set_up，导致每个接口调用时候都会执行get_token
    # def setup(self):
    #     self.address_page = AddressPage

    # 设置成类级别
    def setup_class(self):
        self.address_page = AddressPage


    def test_get(self):
        member_message = self.address_page.get_member_info()
        assert member_message['errcode'] == [0, 60111]

    def test_add(self):
        member_message = self.address_page.add_member()
        assert member_message['errcode'] in [0, 60104]

    def test_delete(self):
        member_message = self.address_page.delete_member()
        assert member_message['errcode'] in [0, 60111]

    def test_update(self):
        member_message = self.address_page.update_member()
        assert member_message['errcode'] in [0, 60111]
