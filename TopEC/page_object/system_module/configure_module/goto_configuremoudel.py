from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from TopEC.base.basepage import BasePage

# 从首页进入计算模块的首页-->云服务器页面
class ConfigureHome(BasePage):
    def goto_configure(self):
        self.move_mouse(By.ID, 'navBar_item_系统_content')
        self.move_and_click(By.ID, 'navBar_item_系统_content_配置')


    def goto_configurehome(self):    #云服务器子模块首页人口
        self.click(By.XPATH, '//*[@id="panel-c-scroll"]/div[1]/section/section/div[1]/div[1]/h3')



