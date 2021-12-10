from time import sleep

import pytest
from selenium.webdriver.common.by import By
from TopEC.base.basepage import BasePage
from TopEC.others.yamlexcelload import loadyaml
from TopEC.others.filepath import readFilepath

#1.配置模块
# 1.1配置页面
class ConfigurePage(BasePage):
    filepath = readFilepath.ConfigureDataPath
    data = loadyaml(filepath)
    # 1.1.1 配置页面/基础配置栏信息校验
    # (1)系统发送和邮件配置参数校验
    def update_mail(self):
        data0 = self.data['TH-SY-MAIL-0001']     #获取系统发送和邮件配置-->进入系统发送和邮件配置弹窗页面
        data1 = self.data['TH-SY-MAIL-0002']     #获取云服务器输入框输入为特殊字符后的提示信息元素
        # data2 = self.data['TH-CP-VM-0005']     #获取云服务器输入框输入为空后的提示信息元素
        # data3 = self.data['TH-CP-VM-0006']     #获取云服务器提示框输入为特殊字符后的提示信息元素
        # data4 = self.data['TH-CP-VM-0007']     #获取云服务器提示框输入为大于32位字符后的提示信息元素
        # data5 = self.data['TH-CP-VM-0008']  # 获取云服务器提示框输入为大于32位字符后的提示信息元素
        self.steps(data0)      #依次点击系统发送和邮件配置，系统发送和邮件配置弹窗页面
        # (1)云服务器输入特殊字符提示验证
        service01 = self.steps(data1)
        # # (2)云服务器输入框输入为空验证
        # service02 = self.steps(data2)
        # # (3)云服务器输入框输入特殊字符验证
        # service03 = self.steps(data3)
        # # (4)云服务器输入框输入大于32位字符验证
        # service04 = self.steps(data4)
        # # (5)云服务器输入框输入正确字符验证
        # self.steps(data5)
        return service01









    #1.2.3.2 迁入云服务器
    #1.2.3.3 导入云服务器


    #（14）添加云服务器

    #(1)集群目录新增组功能验证
    def add_group(self):
        return self.steps(r'/TopEC/data/page_data/calculate_module_data/cserver_module/serverdata.yaml')

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


