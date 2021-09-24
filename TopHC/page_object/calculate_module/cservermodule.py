import pytest
from selenium.webdriver.common.by import By
from TopHC.base.basepage import BasePage
from TopHC.others.yamlexcelload import loadyaml
from TopHC.others.filepath import readFilepath

#1.云服务器模块
# 1.1云服务器页面
class ServicePage(BasePage):
    filepath = readFilepath.ServerDataPath
    data = loadyaml(filepath)
    # 1.1.1 云服务器页面/集群信息导航栏信息校验
    # (1)集群目录信息校验
    def search_clustersUI1(self):
        data1 = self.data['TH-CP-CLUSTER-0001']
        return self.steps(data1)


    #（2）集群云服务器信息校验
    def search_clustersUI2(self):
        data2 = self.data['TH-CP-CLUSTER-0002']
        return self.steps(data2)

    #(3)集群目录结构信息校验
    def search_clustersUI3(self):
        data3 = self.data['TH-CP-CLUSTER-0003']['data01']+self.data['TH-CP-CLUSTER-0003']['data02']
        return self.steps(data3)

    #(4)集群目录下服务器信息校验
    def search_clustersUI4(self):
        data4 = self.data['TH-CP-CLUSTER-0004']['data01']+self.data['TH-CP-CLUSTER-0004']['data02']+self.data['TH-CP-CLUSTER-0004']['data03']
        return self.steps(data4)

    # 1.1.2.云服务器页面/集群信息导航栏功能校验
    # (5)集群目录新增组功能验证/正常场景
    def search_clustersUI5(self):
        data51 = self.data['TH-CP-CLUSTER-0005']['data01']
        self.steps(data51)
        data52 = self.data['TH-CP-CLUSTER-0005']['data02']
        self.move_mouse(data52['by'], data52['locator'])
        data53 = self.data['TH-CP-CLUSTER-0005']['data03']
        #self.move_and_click(data53['by'], data53['locator'])
        self.click(data53['by'], data53['locator'])

    # (6)集群目录新增组功能验证/异常场景
    def search_clustersUI6(self):
        pass

    # (7)集群目录组名称重命名功能验证/正常场景
    def search_clustersUI7(self):
        pass

    #（8）集群目录组名称重命名功能验证/异常场景
    def search_clustersUI8(self):
        pass

    #（9）集群目录组添加云服务器入口验证
    def search_clustersUI9(self):
        pass

    #（10）集群目录组移动验证
    def search_clustersUI10(self):
        pass

    #（11）集群目录组删除验证
    def search_clustersUI11(self):
        pass

    # 1.2.1.云服务器页面/菜单栏功能校验/搜索
    #（1）虚拟机搜索/功能入口参数校验
    def search_VM1(self):
        data12 = self.data['TH-CP-VM-0001']
        return self.text(data12['by'], data12['locator'], attr = data12['attr'])

    # (2) 搜索功能验证/正常场景
    def search_VM2(self):
        data13 = self.data['TH-CP-VM-0002']
        return self.steps(data13)

    # (3) 搜索功能验证/正常场景
    def search_VM3(self):
        data14 = self.data['TH-CP-VM-0003']
        return self.steps(data14)

    # 1.2.2.云服务器页面/菜单栏功能校验/虚拟机批量操作



    # 1.2.3.云服务器页面/菜单栏功能校验/添加云服务器
    #1.2.3.1 创建云服务器
    # <1 自定义
    # <1-1 基本信息页参数校验
    def creat_VM_page1(self):
        # <1-1-1云服务器输入框验证
        data0 = self.data['TH-CP-VM-000']['data01']  #获取添加云服务器-->创建云服务器元素
        data1 = self.data['TH-CP-VM-0004']     #云服务器提示框，获取弱提示属性
        data2 = self.data['TH-CP-VM-0005']     #获取云服务器输入框输入为空后的提示信息元素
        data3 = self.data['TH-CP-VM-0006']     #获取云服务器提示框输入为特殊字符后的提示信息元素
        data4 = self.data['TH-CP-VM-0007']     #获取云服务器提示框输入为大于32位字符后的提示信息元素
        data5 = self.data['TH-CP-VM-0008']  # 获取云服务器提示框输入为大于32位字符后的提示信息元素
        self.steps(data0)      #依次点击添加云服务器-->创建云服务器，进入基本信息页
        # (1)云服务器输入框弱提示验证
        service01 = self.text(data1['by'], data1['locator'], attr=data1['attr'])
        # (2)云服务器输入框输入为空验证
        service02 = self.steps(data2)
        # (3)云服务器输入框输入特殊字符验证
        service03 = self.steps(data3)
        # (4)云服务器输入框输入大于32位字符验证
        service04 = self.steps(data4)
        # (5)云服务器输入框输入正确字符验证
        self.steps(data5)
        return service01, service02, service03, service04









    #1.2.3.2 迁入云服务器
    #1.2.3.3 导入云服务器


    #（14）添加云服务器

    #(1)集群目录新增组功能验证
    def add_group(self):
        return self.steps(r'/TopHC/data/page_data/calculate_module_data/cserver_module/serverdata.yaml')

    #(6)集群目录组名称重命名功能验证
    def update_group(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_updategroup.yaml')










#模板页面
class MouldPage(BasePage):
    def search_clustersUI21(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_cluster21.yaml')


#规格页面
class SpecsPage(BasePage):
    pass


#备份页面
class BackupPage(BasePage):
    pass

#策略页面
class StrategyPage(BasePage):
    pass


