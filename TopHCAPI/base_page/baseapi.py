import requests


class BaseApi:
    def send(self, **data):  #data可能是字典，所以要进行解析
        #使用request完成多请求的改造（post,get,delete,update）,因为requests调用的是request方法
        return requests.request(**data).json()  #直接使用关键字传参，将请求结构体传给requests.request方法
