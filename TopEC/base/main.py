'''
    每个页面都是独立的对象，main用来实现页面对象的组合，即从一个页面跳转到另一个页面
'''


from time import sleep

from TopEC.base.basepage import BasePage

from TopEC.page_object.calculate_module.ccontainermodule import BackupPage
from TopEC.page_object.calculate_module.containercmodule import SpecsPage
from TopEC.page_object.calculate_module.cservermodule import ServicePage, MouldPage
from TopEC.page_object.calculate_module.desktopmoudel import StrategyPage
from TopEC.page_object.calculate_module.goto_calculatemoudel import CserviceHome
from TopEC.page_object.home_module.homemoudel import HomePage
from TopEC.page_object.system_module.configure_module.configuremodule import ConfigurePage
from TopEC.page_object.system_module.configure_module.goto_configuremoudel import ConfigureHome


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
    # 2.1.1云服务器页面入口
    def goto_cserver(self):
        CserviceHome(self._driver).goto_cserver()
        return CserviceHome(self._driver).goto_cserverhome() # 先调用入口方法进入云服务器模块

    def goto_serverpage(self):    #进入云服务器模块云服务器页面的实现类
        return ServicePage(self._driver)

    #2.1.2云服务器模板页面入口
    def goto_cmouldpage(self):
        self.goto_cservermould()  #先调云服务器页面入口
        return MouldPage(self._driver)

    # 2.1.3云服务规格页面入口
    def goto_cspecs(self):
        self.goto_cmouldpage()  # #先调云服务器页面入口
        sleep(1)
        return SpecsPage(self._driver)


    # 2.1.4云服务备份页面入口
    def goto_cbackup(self):
        self.goto_serverpage()  # #先调云服务器页面入口
        sleep(1)
        return BackupPage(self._driver)

    # 2.1.5云服务策略页面入口
    def goto_strategy(self):
        self.goto_serverpage()  # #先调云服务器页面入口
        sleep(1)
        return StrategyPage(self._driver)



    # 10.系统模块
    # 2.1配置子模块入口路径
    # 2.1.1配置页面入口
    def goto_configure(self):
        ConfigureHome(self._driver).goto_configure()
        return ConfigureHome(self._driver).goto_configurehome() # 先调用入口方法进入配置模块

    def goto_configurepage(self):    #进入云服务器模块云服务器页面的实现类
        return ConfigurePage(self._driver)