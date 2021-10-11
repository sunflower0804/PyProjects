#因为token_access也是公共的，且会发生变化，所以也对它进行封装

from TopHCAPI.base_api.baseapi import BaseApi
from TopHCAPI.others.filepath import readFilepath
from TopHCAPI.others.yamlexcelload import loadyaml


class LoginToken(BaseApi):
    filepath = readFilepath.LoginDataPath  # LoginDataPath
    data = loadyaml(filepath)

    # 获取企业云登录的token(用户身份验证信息)
    # 请求方式：post（HTTPS）
    # 请求地址：https://10.30.45.91/v1/authentication/login
    # 请求包体：
    # 参数说明：
    def login_token(self):
        data1 = self.data['TH-CP-LOGIN-0001']  # 验证集群名称的驱动数据
        # 使用字典的方式，将要发送的请求所有需要的信息传递给发送api请求的方法
        return self.send(**data1)  # **data:对字典内容进行解析

token = LoginToken()

def test_token():
    tt = token.login_token()
    print(tt)


'''



class BaseToken(BaseApi):
    # 获取企业云的access_token(用户身份验证信息)
    # 请求方式：post（HTTPS）
    # 请求地址：http://10.30.33.25:8080/v1/authentication/login
    # 请求包体：
    # 参数说明：
    def post_token(self, is_ldap, tenant, user, password):
        # 使用字典的方式，将要发送的请求所有需要的信息传递给发送api请求的方法
        data = {
            "method": "post",
            "url": "https://10.30.45.91/v1/authentication/login",
            "data": {
                "is_ldap": is_ldap,
                "tenant": tenant,
                "user": user,
                "password": password,
            },
            "verify": False
        }
        return self.send(**data)  # **data:对字典内容进行解析

token = BaseToken()


def test_post_token1():
    #ttype = "application/json"
    user = "xh"
    is_ldap = False
    tenant = "system"
    password = "767e955464233667bfd855686a55b352"
    ss = ee.post_token(is_ldap, tenant, user, password)
    print(ss)

def test_post_token2():
    url = "https://10.30.45.91/v1/authentication/login"
    data = {
        "login_url": "10.30.45.91",
        "user": "xh",
        "is_ldap": False,
        "tenant": "system",
        "password": "admin123."}

    request = requests.post(url, data=json.dumps(data).encode("utf-8"), timeout=20, verify=False)
    #print(dir(request))
    #print(json.loads(request.content))
    print(request.json())


def test_post_token3():
    url = "http://10.30.100.25:8080/v1/authentication/login"
    data = {
        #"login_url": "10.30.100.25",
        #"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
        "user": "xh",
        "is_ldap": False,
        "tenant": "system",
        "password": "767e955464233667bfd855686a55b352"}

    request = requests.post(url, data=json.dumps(data).encode("utf-8"), timeout=20, verify=False)
    #print(dir(request))
    #print(json.loads(request.content))
    print(request.json())

'''
# class Adds(BaseApi):
#     # 获取企业云的access_token(用户身份验证信息)
#     # 请求方式：post（HTTPS）
#     # 请求地址：http://10.30.33.25:8080/v1/authentication/login
#     # 请求包体：
#     # 参数说明：
#     def tag(self, is_ldap, tenant, user, password):
#         # 使用字典的方式，将要发送的请求所有需要的信息传递给发送api请求的方法
#         data = {
#             "method": "post",
#             "url": "http://10.30.100.26:8080/v1/label/type/add",
#             "headers": {
#                 "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJ4aCIsInRlbmFudCI6InN5c3RlbSIsInVzZXJfdXVpZCI6ImFjNGI2NDNiLThlY2UtNDZmZC05ZjZhLTFlYjg0YjMxNGIxZSIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaXNfbGRhcCI6ZmFsc2UsImV4cCI6MTYzMzYxMDQ1MiwiaWF0IjoxNjMzNDkyMjUyLCJjbGllbnRfaXAiOiIxMC4zMC42MS4yMDkifQ.qzoMEDoLRSPSJFEDnJY6EezfFHEg0iLESiPBh6QzOpc"
#             },
#         "json": {
#                 "tenant": "f15a44f9-26f5-4bea-a96b-55f5f1d78fa0",
#                 "name": "13",
#                 "color":"#396afc",
#                 "cluster_uuid":"49bb08f9-1c60-49ee-85d6-6fde276895c5"}
#         }
#         return self.send(**data)  # **data:对字典内容进行解析

# adds = Adds()

# def test_tag():
#     tt = adds.add_tag()
#     print(tt)