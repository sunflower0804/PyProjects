#from project02.RequestsWework.PO.page_object.tagapi import TagApi

from TopHCAPI.pageapi.home_module.loginapi import BaseToken
from TopHCAPI.pageapi.home_module.homemodelapi import HomeApi


class TestHomeApi:
    def setup(self):
        self.tokenapi = BaseToken()
        self.homeapi = HomeApi()

    def test_create(self):
        print(self.tagapi.tag_create('卡尔特人',21))

    def test_update(self):
        print(self.tagapi.tag_update(21,'凯尔特人'))  #这里函数调用错了print(self.test_update(24,'勇士'))导致报错：TypeError: test_update() takes 1 positional argument but 3 were given

    def test_delete(self):
        print(self.tagapi.tag_delete(21))

    def test_get(self):
        assert 0 == self.tagapi.tag_get(23)['errcode']

    def test_add(self):
        #assert 'ok' == self.tagapi.tag_add(3,'kill',4)['errmsg']
        print(self.tagapi.tag_add(3,'kill',4)['errmsg'])