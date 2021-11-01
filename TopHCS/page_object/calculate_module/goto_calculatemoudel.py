from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




from TopHC.base.basepage import BasePage

# 云服务器模块入口
# 从首页进入计算模块的首页-->云服务器模块
class CserviceMoudelFile(BasePage):
    def goto_cserver(self):
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