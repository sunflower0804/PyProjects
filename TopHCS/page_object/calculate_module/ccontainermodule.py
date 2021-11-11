

#云容器模块
#1.云容器页面
from time import sleep

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
        data1 = self.data['TH-CP-HANG_CN-0001']['data1']  #
        return self.steps(data1)  #捕获挂起云容器成功的提示信息

    # 123恢复
    def recover_Ccontainer(self):
        data0 = self.data['TH-CP-RECOVER_CN-0001']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-RECOVER_CN-0001']['data1']  #
        return self.steps(data1)  #捕获恢复云容器成功的提示信息

    # 124分配
    def allot_Ccontainer(self):
        data0 = self.data['TH-CP-ALLOT_CN-0001']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-ALLOT_CN-0001']['data1']  #
        return self.steps(data1)  #捕获分配云容器成功的提示信息

    # 1.3编辑云容器
    # 131开机编辑
    def edit_Ccontainer1(self):
        data0 = self.data['TH-CP-EDIT_CN-0001']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-EDIT_CN-0001']['data1']  #
        result1 = self.steps(data1)  #捕获不允许添加磁盘的提示信息
        sleep(3)
        # data2 = self.data['TH-CP-EDIT_CN-0001']['data2']  #
        # result2 = self.steps(data2)  #捕获不允许添加主机映射的提示信息
        sleep(3)
        self.keys_PageDown()
        data3 = self.data['TH-CP-EDIT_CN-0001']['data3']  #
        result3 = self.steps(data3)  #捕获添加网卡成功的提示信息
        data5 = self.data['TH-CP-EDIT_CN-0001']['data5']  #
        self.steps(data5)  #捕获添加网卡成功的提示信息
        return result1, result3,   #result2, result3


    # 132关机编辑
    def edit_Ccontainer2(self):
        data0 = self.data['TH-CP-EDIT_CN-0002']['data0']  #
        self.steps(data0)  #搜索云容器
        data1 = self.data['TH-CP-EDIT_CN-0002']['data1']  #
        self.steps(data1)  #关机云容器
        data2 = self.data['TH-CP-EDIT_CN-0002']['data2']  #
        result1 = self.steps(data2)  #捕获添加磁盘成功的提示信息
        sleep(2)
        self.keys_PageDown()
        data3 = self.data['TH-CP-EDIT_CN-0002']['data3']  #
        result2 = self.steps(data3)  #捕获添加主机映射成功的提示信息
        sleep(2)
        data4 = self.data['TH-CP-EDIT_CN-0002']['data4']  #
        result3 = self.steps(data4)  # 捕获不允许添加网卡的提示信息
        sleep(2)
        data5 = self.data['TH-CP-EDIT_CN-0002']['data5']  #
        result4 = self.steps(data5)  # 捕获不允许添加网卡的提示信息
        sleep(2)
        self.keys_PageDown()
        data6 = self.data['TH-CP-EDIT_CN-0002']['data6']
        self.steps(data6)   #后置条件：还原
        return result1, result2, result3, result4


#2.密钥页面
class CipherPage(BasePage):
    filepath = readFilepath.CiperDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    #2.1创建密钥
    def add_Cipher(self):
        data0 = self.data['TH-CP-ADD_CIPHER-0000']
        return self.steps(data0)  #捕获创建密钥成功的提示信息

    # 2.2编辑密钥
    def edit_Cipher(self):
        # data0 = self.data['TH-CP-EDIT_CIPHER-0001']['data0']
        # self.steps(data0)  #搜索密钥
        data1 = self.data['TH-CP-EDIT_CIPHER-0001']['data1']
        return self.steps(data1)  #捕获编辑密钥成功的提示信息

    #2.3删除密钥
    def del_Cipher(self):
        # data0 = self.data['TH-CP-EDIT_CIPHER-0001']['data0']
        # self.steps(data0)  #搜索密钥
        data1 = self.data['TH-CP-DEL_CIPHER-0001']['data1']
        return self.steps(data1)  #捕获删除密钥成功的提示信息

#3.配置页面
class DisposePage(BasePage):
    filepath = readFilepath.DisposeDataPath
    data = loadyaml(filepath)  # 获取测试驱动数据文件，并解析

    # 3.1添加镜像
    # 311添加第三方镜像加速器
    def add_Image1(self):
        data0 = self.data['TH-CP-ADD_IMAGE-0000']
        return self.steps(data0)  # 捕获添加第三方镜像加速器成功的提示信息

    # 312添加私有镜像源
    def add_Image2(self):
        data0 = self.data['TH-CP-ADD_IMAGE-0001']
        return self.steps(data0)  # 捕获添加私有镜像源成功的提示信息

    # 3.2删除镜像
    def del_Image(self):
        data0 = self.data['TH-CP-DEL_IMAGE-0001']
        return self.steps(data0)  #捕获删除镜像成功的提示信息

    # 3.3编辑配置信息
    def detel_Dispose(self):
        data0 = self.data['TH-CP-DETEL_DISPOSE-0001']['data0']
        return self.steps(data0)  #捕获删除镜像成功的提示信息