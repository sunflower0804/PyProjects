'''
    每个页面都是独立的对象，main用来实现页面对象的组合，即从一个页面跳转到另一个页面
'''


from time import sleep

from TopHCS.base.basepage import BasePage
from TopHCS.page_object.calculate_module.cservermodule import ServicePage, MouldPage, SpecsPage, BackupPage, StrategyPage
from TopHCS.page_object.calculate_module.goto_calculatemoudel import CserviceMoudelFile
from TopHCS.page_object.home_module.homemoudel import HomePage
from TopHCS.page_object.system_module.configure_module.configuremodule import ConfigurePage
from TopHCS.page_object.system_module.configure_module.goto_configuremoudel import ConfigureHome


class Main(BasePage):
    # 进入首页（用户名登录的步骤通过basepage模块中复用已登录过账号）
    _base_url = 'http://10.30.100.26:8080/#/pages/overview'

    # 1.首页-->概览模块
    # 1.1首页页面入口
    def goto_homepage(self):
        sleep(1)
        return HomePage(self._driver)   #跳转至首页功能实现的流程方法类

    # 2.计算模块
    # 2.1云服务器子模块入口路径
    def goto_cserver(self):
        CserviceMoudelFile(self._driver).goto_cserver()
        return CserviceMoudelFile(self._driver).goto_cserverpage()  #先调用入口方法进入云服务器模块/云服务器页面

    # 2.1.1云服务器页面入口
    def goto_serverpage(self):
        # CserviceMoudelFile(self._driver).goto_cserverpage()  #先调云服务器云服务器页面入口
        return ServicePage(self._driver)  #跳转至云服务器模块/云服务器页面方法

    #2.1.2云服务器模板页面入口
    def goto_mouldpage(self):
        CserviceMoudelFile(self._driver).goto_mouldpage()  #先调云服务器模板页面入口
        return MouldPage(self._driver)   #跳转至云服务器模块/云服务器模板页面方法

    # 2.1.3云服务规格页面入口
    def goto_specs(self):
        CserviceMoudelFile(self._driver).goto_specspage()  #先调云服务器规格页面入口
        return SpecsPage(self._driver)   #跳转至云服务器模块/云服务器规格页面方法


    # 2.1.4云服务备份页面入口
    def goto_backup(self):
        CserviceMoudelFile(self._driver).goto_backup()   #先调云服务器备份页面入口
        return BackupPage(self._driver)  #跳转至云服务器模块/云服务器备份页面方法

    # 2.1.5云服务策略页面入口
    def goto_strategy(self):
        CserviceMoudelFile(self._driver).goto_strategy()  #先调云服务器策略页面入口
        return StrategyPage(self._driver) #跳转至云服务器模块/云服务器策略页面方法




    # 10.系统模块
    # 2.1配置子模块入口路径
    # 2.1.1配置页面入口
    def goto_configure(self):
        ConfigureHome(self._driver).goto_configure()
        return ConfigureHome(self._driver).goto_configurehome() # 先调用入口方法进入配置模块

    def goto_configurepage(self):    #进入云服务器模块云服务器页面的实现类
        return ConfigurePage(self._driver)