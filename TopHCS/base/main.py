'''
    每个页面都是独立的对象，main用来实现页面对象的组合，即从一个页面跳转到另一个页面
'''
from time import sleep

from TopHCS.base.basepage import BasePage
from TopHCS.page_object.calculate_module.ccontainermodule import CcontainerPage, CipherPage, DisposePage
from TopHCS.page_object.calculate_module.cservermodule import ServicePage, MouldPage, SpecsPage, BackupPage, StrategyPage
from TopHCS.page_object.calculate_module.goto_calculatemoudel import CserviceMoudelFile, CcontainerMoudelFile
from TopHCS.page_object.home_module.homemoudel import HomePage
from TopHCS.page_object.login_module.loginpage import LoginPage
from TopHCS.page_object.operation_module.cost_module import SpeciPage
from TopHCS.page_object.operation_module.goto_operationmoudel import CostMoudelFile

from TopHCS.page_object.system_module.configure_module.configuremodule import ConfigurePage
from TopHCS.page_object.system_module.configure_module.goto_configuremoudel import ConfigureHome


class Main(BasePage):
    # 登录页面（用户名登录的步骤）
    url = 'http://10.30.100.26:8080/#/login'

    def goto_logins(self):
        return LoginPage(self.driver)

    # 1.首页-->概览模块
    # 1.1首页页面入口
    def goto_homepage(self):
        return HomePage(self.driver)   #跳转至首页功能实现的流程方法类

    # 2.计算模块
    # 2.1云服务器子模块入口路径
    def goto_cserver(self):
        CserviceMoudelFile(self.driver).goto_cserver()
        return CserviceMoudelFile(self.driver).goto_cserverpage()  #先调用入口方法进入云服务器模块/云服务器页面

    # 2.1.1云服务器页面入口
    def goto_serverpage(self):
        # CserviceMoudelFile(self._driver).goto_cserverpage()  #先调云服务器云服务器页面入口
        return ServicePage(self.driver)  #跳转至云服务器模块/云服务器页面方法

    #2.1.2云服务器模板页面入口
    def goto_mouldpage(self):
        CserviceMoudelFile(self.driver).goto_mouldpage()  #先调云服务器模板页面入口
        return MouldPage(self.driver)   #跳转至云服务器模块/云服务器模板页面方法

    # 2.1.3云服务规格页面入口
    def goto_specs(self):
        CserviceMoudelFile(self.driver).goto_specspage()  #先调云服务器规格页面入口
        return SpecsPage(self.driver)   #跳转至云服务器模块/云服务器规格页面方法


    # 2.1.4云服务备份页面入口
    def goto_backup(self):
        CserviceMoudelFile(self.driver).goto_backup()   #先调云服务器备份页面入口
        return BackupPage(self.driver)  #跳转至云服务器模块/云服务器备份页面方法

    # 2.1.5云服务策略页面入口
    def goto_strategy(self):
        CserviceMoudelFile(self.driver).goto_strategy()  #先调云服务器策略页面入口
        return StrategyPage(self.driver) #跳转至云服务器模块/云服务器策略页面方法

    #2.2云容器模块
    def goto_ccontainer(self):
        CcontainerMoudelFile(self.driver).goto_ccontainer()
        return CcontainerMoudelFile(self.driver).goto_containerpage() # 先调用入口方法进入云容器模块/云容器页面

    # 2.2.1云容器页面入口
    def goto_containerpage(self):
        # CcontainerMoudelFile(self._driver).goto_containerpage()  #先调云容器页面入口
        return CcontainerPage(self.driver)  # 跳转至云容器模块/云容器页面方法

    # 2.2.2密钥页面入口
    def goto_ciperpage(self):
        CcontainerMoudelFile(self.driver).goto_cipherpage()  # 先调云容器页面入口
        return CipherPage(self.driver)  # 跳转至云器器模块/云容器密钥页面方法

    # 2.2.3配置页面入口
    def goto_disposepage(self):
        CcontainerMoudelFile(self.driver).goto_disposepage()  # 先调云容器配置页面入口
        return DisposePage(self.driver)  # 跳转至云器器模块/云容器配置页面方法

    # 8.运营模块
    # 8.1租户子模块入口路径
    #####

    # 8.1计费子模块入口路径
    def goto_cost(self):
        CostMoudelFile(self.driver).goto_cost()
        return CostMoudelFile(self.driver).goto_billpage()  #先调用入口方法进入计费模块/账单页面

    # 8.2.1账单页面入口
    # def goto_billpage(self):
    #     # CostMoudelFile(self.driver).goto_billpage() #先调计费账单页面入口
    #     return BillPage(self.driver)  #跳转至云服务器模块/云服务器页面方法

    # 8.2.2规格页面入口
    def goto_specipage(self):
        CostMoudelFile(self.driver).goto_specipage() #先调计费账单页面入口
        return SpeciPage(self.driver)  #跳转至云服务器模块/云服务器页面方法

    # 10.系统模块
    # 2.1配置子模块入口路径
    # 2.1.1配置页面入口
    def goto_configure(self):
        ConfigureHome(self.driver).goto_configure()
        return ConfigureHome(self.driver).goto_configurehome() # 先调用入口方法进入配置模块

    def goto_configurepage(self):    #进入云服务器模块云服务器页面的实现类
        return ConfigurePage(self.driver)