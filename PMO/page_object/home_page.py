'''
    home_page页面对象，实现页面中关于商品搜索的流程
'''
from selenium.webdriver.common.by import By

from PMO.base.base_page import BasePage


class HomePage(BasePage):
    #核心元素
    #url = 'http://39.98.138.157/shopxo/index.php'  #针对该系统，不登陆就可以访问的情况

    search_input =  (By.NAME, 'wd')  #输入框
    search_button =  (By.ID, 'ai-topsearch')

    #核心业务（基于元素实现的业务流：都是基于当前页面访问的情况下，才可以继续后面的操作）
    #def login(self):
        #self.visit(self.url)  #这里直接写死
    def search(self, txt):
        #在登录后的首页中进行搜索操作
        self.send(self.search_input, txt)
        self.click(self.search_button)

#调试代码
'''
if __name__ == '__main__':
    self.main.goto_main_homepage('手机')
    txt = '手机'
    lp = HomePage()
    lp.search(txt)
'''