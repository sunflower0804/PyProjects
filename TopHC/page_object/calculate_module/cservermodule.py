import pytest
from selenium.webdriver.common.by import By
from TopHC.base.basepage import BasePage
from TopHC.others.yamlexcelload import loadyaml
from TopHC.others.filepath import readFilepath

#云服务器模块
# 1.云服务器页面





class ServicePage(BasePage):
    aa = readFilepath.ServerDataPath
    # 1.1 集群信息导航栏信息校验
    # (1)集群目录信息校验
    def search_clustersUI1(self):
        data1 = self.aa
        data = loadyaml(data1)
        data1 = data['TH-CP-CLUSTER-0001']
        return self.steps(data1)


    #（2）集群云服务器信息校验
    def search_clustersUI2(self):
        return self.move_code(r'/TopHC/data/page_data/calculate_module_data/cserver_module/cal_cserver_cluster2.yaml')

    #(3)集群目录结构信息校验
    def search_clustersUI3(self):
        return self.steps(r'/TopHC/data/page_data/calculate_module_data/cserver_module/cal_cserver_cluster3.yaml')

    #(4)集群目录下服务器信息校验
    def search_clustersUI4(self):
        return self.steps(r'/TopHC/data/page_data/calculate_module_data/cserver_module/cal_cserver_cluster4.yaml')

    # 1.2 集群信息导航栏功能校验
    #（1）虚拟机批量操作

    #（2）虚拟机搜索

    #（3）添加云服务器

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


