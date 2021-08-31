#因为token_access也是公共的，且会发生变化，所以也对它进行封装
#from project02.RequestsWework.AO.base.baseapi import BaseApi
from TopHCAPI.base_page.baseapi import BaseApi


class BaseToken(BaseApi):
    # 获取企业云的access_token(用户身份验证信息)
    # 请求方式：post（HTTPS）
    # 请求地址：http://10.30.33.25:8080/v1/authentication/login
    # 请求包体：
    # 参数说明：
    def post_token(self, false, pwd, system, user):
        # 使用字典的方式，将要发送的请求所有需要的信息传递给发送api请求的方法
        data = {
            "method": "post",
            "url": "http://10.30.33.25:8080/v1/authentication/login",
            "params": {
                "is_ldap": false,
                "password": pwd,
                "tenant": system,
                "user": user
            }
        }
        return self.send(**data)['access_token']  # **data:对字典内容进行解析

