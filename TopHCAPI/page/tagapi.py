

import requests

#from project02.RequestsWework.AO.base.baseapi import BaseApi
#from project02.RequestsWework.PO.base.base_token import BaseToken
from TopHCAPI.base_page.base_token import BaseToken
from TopHCAPI.base_page.baseapi import BaseApi


class TagApi(BaseApi):
    #调用get_token方法得到token值
    def __init__(self):
        self.get_token = BaseToken().post_token()

    # 1.创建标签
    # 请求方式：POST（HTTPS）
    # 请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
    # 请求包体：
    # 参数说明：
    def tag_create(self, tagname, tagid):
        data1 = {
                "tagname": tagname,
                "tagid": tagid
            }
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {            #"params": self.get_token(),直接传会报错，因为params的值应该是一个字典
                "access_token": self.get_token,
                },
            "json": data1,
        }
        return self.send(**data)

    #2.更新标签
    # 请求方式：POST（HTTPS）
    #请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
    #请求包体：
    #参数说明：
    def tag_update(self, tagid, tagname):
        data1 = {
            "tagid": tagid,
            "tagname": tagname
            }
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {
                "access_token": self.get_token,
            },
            "json": data1,
        }
        return self.send(**data)

    #3.删除标签
    # 请求方式：GET（HTTPS）
    #请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
    #参数说明：
    def tag_delete(self,tagid):
        tagid = tagid
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {
                "access_token": self.get_token,
                "tagid": tagid
            }
        }
        return self.send(**data)

    #4.获取标签成员
    #请求方式：GET（HTTPS）
    #请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
    #参数说明：
    def tag_get(self,tagid):
        tagid = tagid
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params": {
                "access_token": self.get_token,
                "tagid": tagid
            }
        }
        return self.send(**data)

    #5.增加标签成员
    #请求方式：POST（HTTPS）
    #请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN
    #参数说明：
    def tag_add(self,tagid,tagname,partylist):
        data1 = {
            "tagid": tagid,
            "tagname": tagname,
            "partylist": partylist
        }
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {  # "params": self.get_token(),直接传会报错，因为params的值应该是一个字典
                "access_token": self.get_token,
            },
            "json": data1,
        }
        return self.send(**data)



