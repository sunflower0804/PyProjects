#from project02.RequestsWework.PO.page_object.tagapi import TagApi
import pytest
import yaml

from TopHCAPI.page.tagapi import TagApi


class TestTagApi:
    def setup(self):
        self.tagapi = TagApi()

    @pytest.mark.parametrize("false, pwd, system, user", yaml.safe_load(open("./logintest.yaml")))
    def test_post_token(self, false, pwd, system, user):
        print(self.tagapi.post_token())

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