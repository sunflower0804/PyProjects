'''
    LoginPage类，专门用于实现登录页面的对象文件
    主体内容包含：
        1.核心的页面元素：
            账号、密码、登录按钮
        2.核心业务流：
            用户登录行为
'''

from selenium.webdriver.common.by import By

from PMO.base.base_page import BasePage


class LoginPage(BasePage):
    #核心元素
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    user = (By.NAME, 'accounts')
    password = (By.NAME, 'pwd')
    login_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    #核心业务
    #def login(self):
        #self.visit(self.url)  #这里直接写死
    def login(self, username, password):
        self.visit()
        self.send(self.user, username)
        self.send(self.password, password)
        self.click(self.login_button)

#调试代码
'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = 'xh'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(username, password)
'''