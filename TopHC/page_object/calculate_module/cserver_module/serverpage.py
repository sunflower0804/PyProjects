from TopHC.base.basepage import BasePage


class ServicePage(BasePage):
    # 1.云服务器模块UI信息检查
    # 1-1-1.集群信息导航栏信息校验
    # (1)集群目录信息校验
    def search_clustersUI1(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_cluster1.yaml')


    #（2）集群云服务器信息校验
    def search_clustersUI2(self):
        return self.move_code(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_cluster2.yaml')


    #(3)集群目录结构信息校验
    def search_clustersUI3(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_cluster3.yaml')

    #(4)集群目录下服务器信息校验
    def search_clustersUI4(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_cluster4.yaml')

    # 1-1-2.集群信息导航栏功能校验
    #(5)集群目录新增组功能验证
    def add_group(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_addgroup.yaml')

    #(6)集群目录组名称重命名功能验证
    def update_group(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_updategroup.yaml')
