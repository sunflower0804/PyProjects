from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from TopHC.base.basepage import BasePage

# 从首页进入计算模块的首页-->云服务器页面
class CserviceHome(BasePage):
    def goto_cserverhome(self):
        self.move_mouse(By.ID, 'navBar_item_计算_content')
        self.move_and_click(By.ID, 'navBar_item_计算_content_云服务器')


    def goto_cservermoudel(self):
        self.click(By.ID, 'tab-template')