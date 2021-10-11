import requests

from TopHCAPI.others.filepath import readFilepath
from TopHCAPI.others.yamlexcelload import loadyaml


class BaseApi:
    def __init__(self):
        self.headers = self.post_token()


    def send(self, **data):  #data可能是字典，所以要进行解析
        #使用request完成多请求的改造（post,get,delete,update）,因为requests调用的是request方法
        return requests.request(**data).json()  #直接使用关键字传参，将请求结构体传给requests.request方法


    # 获取企业云登录的token(用户身份验证信息)
    # 请求方式：post（HTTPS）
    # 请求地址：https://10.30.45.91/v1/authentication/login
    # 请求包体：
    # 参数说明：
    def post_token(self):
        filepath = readFilepath.LoginDataPath  # LoginDataPath
        data = loadyaml(filepath)
        data1 = data['TH-CP-LOGIN-0001']
        # 使用字典的方式，将要发送的请求所有需要的信息传递给发送api请求的方法
        token = self.send(**data1)['data']['token']  # **data:对字典内容进行解析
        headers = {
        "Authorization": "Bearer" + " " + token
        }
        return headers


