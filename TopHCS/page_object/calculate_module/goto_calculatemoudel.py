from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




from TopHCS.base.basepage import BasePage

# 云服务器模块入口
# 从首页进入计算模块的首页-->云服务器模块
class CserviceMoudelFile(BasePage):
    url1 = 'http://10.30.100.26:8080/#/pages/overview'

    def goto_cserver(self):
        self.visit(url=self.url1)
        self.move_mouse(By.ID, 'navBar_item_计算_content')
        self.move_and_click(By.ID, 'navBar_item_计算_content_云服务器')

    def goto_cserverpage(self):    #云服务器子模块首页入口
        self.click(By.XPATH, '//*[@id="tab-vmlist"]')

    def goto_mouldpage(self):
        self.click(By.ID, 'tab-template')  #云服务器子模块模版页面入口

    def goto_specspage(self):
        self.click(By.ID, 'tab-specife')  #云服务器子模块规格页面入口

    def goto_backup(self):
        self.click(By.ID, 'tab-backup')  #云服务器子模块备份页面入口

    def goto_strategy(self):
        self.click(By.ID, 'tab-strategy')  #云服务器子模块策略页面入口


# 云容器模块入口
# 从首页进入计算模块的首页-->云容器模块
class CcontainerMoudelFile(BasePage):
    def goto_ccontainer(self):
        self.move_mouse(By.ID, 'navBar_item_计算_content')
        self.move_and_click(By.ID, 'navBar_item_计算_content_云容器')

    def goto_containerpage(self):    #云容器子模块首页入口：云容器页面
        self.click(By.XPATH, '//*[@id="tab-container"]')

    def goto_cipherpage(self):    #云容器子模块密钥页面入口
        self.click(By.XPATH, '//*[@id="tab-secret"]')

    def goto_disposepage(self):    #云容器子模块配置页面入口
        self.click(By.XPATH, '//*[@id="tab-image"]')