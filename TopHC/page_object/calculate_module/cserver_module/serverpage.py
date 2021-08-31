from TopHC.base.basepage import BasePage


class ServicePage(BasePage):
    # 1.云服务器模块UI信息检查
    # 1-1.集群目录结构信息校验
    # (1)检查每个集群下目录信息
    def search_clustersUI(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\page_object\calculate_module\cserver_module\cal_cserver_cluster1.yaml')


    # （2）云服务器状态展示框
    def search_text1(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\page_object\calculate_module\cserver_module\cal_cserver_cluster1111.yaml')


