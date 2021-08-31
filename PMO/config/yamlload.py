'''
    这个文件用于读取yaml文件数据
'''

#读取yaml文件的方法
import yaml

def loadyaml(filename):
    #首先拿到yaml文件
    files = open(filename, 'r', encoding='utf-8')
    #然后读取yaml文件中的数据
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

#调试
a = loadyaml('../data/login.yaml')
print(a)