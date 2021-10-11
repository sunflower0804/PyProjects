
from TopHCAPI.base_api.baseapi import BaseApi
from TopHCAPI.others.filepath import readFilepath
from TopHCAPI.others.yamlexcelload import loadyaml


class LabelApi(BaseApi):
    filepath = readFilepath.LabelDataPath
    data = loadyaml(filepath)
    # 1.标签类型
    #1.1创建标签类型
    # 请求方式：POST（HTTP）
    # 请求地址：http://10.30.100.26:8080/v1/label/type/add
    # 请求包体：
    # 参数说明：
    def add_label(self):
        data1 = self.data['TH-FN-LABEL-0001']
        return self.send(headers=self.headers, **data1)

    #1.4删除标签类型
    # 请求方式：POST（HTTP）
    # 请求地址：http://10.30.100.26:8080/v1/label/type/add
    # 请求包体：
    # 参数说明：
    def del_label(self):
        data1 = self.data['TH-FN-LABEL-0004']
        return self.send(headers=self.headers, **data1)

    # 2.标签
    #2.1创建标签
    # 请求方式：POST（HTTP）
    # 请求地址：http://10.30.100.26:8080/v1/label/add
    # 请求包体：
    # 参数说明：
    def add_tag(self):
        data1 = self.data['TH-FN-TAG-0001']
        return self.send(headers=self.headers, **data1)

    #2.2查询标签
    # 请求方式：POST（HTTP）
    # 请求地址：http://10.30.100.26:8080/v1/label/type/add
    # 请求包体：
    # 参数说明：
    def get_tag(self):
        data1 = self.data['TH-FN-TAG-0002']
        return self.send(headers=self.headers, **data1)

    #2.3修改标签
    # 请求方式：POST（HTTP）
    # 请求地址：http://10.30.100.26:8080/v1/label/type/add
    # 请求包体：
    # 参数说明：
    def update_tag(self):
        data1 = self.data['TH-FN-TAG-0003']
        return self.send(headers=self.headers, **data1)

    #2.4删除标签
    # 请求方式：POST（HTTP）
    # 请求地址：http://10.30.100.26:8080/v1/label/type/add
    # 请求包体：
    # 参数说明：
    def del_tag(self):
        data1 = self.data['TH-FN-TAG-0004']
        return self.send(headers=self.headers, **data1)





