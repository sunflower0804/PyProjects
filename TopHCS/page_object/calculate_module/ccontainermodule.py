

#云容器模块
#1.云容器页面
from TopHCS.base.basepage import BasePage
from TopHCS.others.filepath import readFilepath
from TopHCS.others.yamlexcelload import loadyaml


class CcontainerPage(BasePage):

    filepath = readFilepath.CcontainerDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    # 1.1新建云容器（前置条件：已存在私有镜像仓库）
    # 111单个创建
    def add_Ccontainer1(self):
        data = self.data['TH-CP-ADD_CN-0000']  #
        return self.steps(data)  #捕获创建云容器成功的提示信息

    #112批量创建
    def add_Ccontainer2(self):
        data = self.data['TH-CP-ADD_CN-0001']  #
        return self.steps(data)  #捕获创建云容器成功的提示信息

    # 1.2云容器操作
    # 121开启
    # 121-1单个开启
    def start_Ccontainer1(self):
        data0 = self.data['TH-CP-ON_CN-0001']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-ON_CN-0001']['data1']  #
        return self.steps(data1)  #捕获开启云容器成功的提示信息

    #121-2批量开启
    def start_Ccontainer2(self):
        data0 = self.data['TH-CP-ON_CN-0002']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-ON_CN-0002']['data1']  #
        return self.steps(data1)  #捕获批量开启云容器成功的提示信息

    # 122挂起
    def hang_Ccontainer(self):
        data0 = self.data['TH-CP-HANG_CN-0001']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-ON_CN-0002']['data1']  #
        return self.steps(data1)  #捕获批量开启云容器成功的提示信息
    # 123恢复
    # 124分配

#2.密钥页面
class CipherPage(BasePage):
    pass

#3.配置页面
class DisposePage(BasePage):
    pass