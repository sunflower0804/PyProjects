'''
    这个文件用于读取yaml文件数据
'''


import yaml

class  YamlUtil:
    # 读取yaml文件的方法
    def loadyaml(filename):
        #首先拿到yaml文件
        with open(filename, 'r', encoding='UTF-8') as f:
            #然后读取yaml文件中的数据
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return data

#调试
#a = YamlUtil.loadyaml(r'D:\WorkTools\PyProjects\TopHC\test_case\calculate_module\cserver_module\test_search_text1.yaml')
#print(a['cluster1'])