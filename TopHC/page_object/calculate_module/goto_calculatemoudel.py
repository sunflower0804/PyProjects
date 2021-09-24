from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from TopHC.base.basepage import BasePage

# 从首页进入计算模块的首页-->云服务器页面
class CserviceHome(BasePage):
    def goto_cserver(self):
        self.move_mouse(By.ID, 'navBar_item_计算_content')
        self.move_and_click(By.ID, 'navBar_item_计算_content_云服务器')


    def goto_cserverhome(self):    #云服务器子模块首页人口
        self.click(By.XPATH, '//*[@id="tab-vmlist"]')


    def goto_cservermoudel(self):
        self.click(By.ID, 'tab-template')  #云服务器子模块模版页面入口