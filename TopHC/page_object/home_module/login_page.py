from time import sleep

from selenium.webdriver.common.by import By

from TopHC.base.login_basepage import BasePage


class LoginPage(BasePage):
    ##核心元素
    tenant = (By.ID, "login_user")
    username = (By.ID, 'login_username')
    password = (By.ID, 'login_password')
    submit = (By.ID, 'login_confirm')   #登录按钮
    url = 'https://10.30.33.25/'

    ## 核心业务:登录流程
    # def login(self):
    # self.visit(self.url)  #这里直接写死

    def login(self, tenant, username, password):  #传递输入框输入的值
        # 加载页面地址
        self.visit()
        self.click(self.tenant)
        self.send(self.tenant, tenant)
        sleep(1)
        self.click(self.username)
        self.send(self.username, username)
        sleep(1)
        self.click(self.password)
        self.send(self.password, password)
        sleep(1)
        self.click(self.submit)
        sleep(2)

#调试代码
'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    tenant = 'system'
    username = 'xh'
    password = 'admin123.'
    lp = LoginPage(driver)
    lp.login(tenant, username, password)
'''