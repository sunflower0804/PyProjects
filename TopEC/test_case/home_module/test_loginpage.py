import allure
import pytest
from selenium import webdriver

from TopEC.others.yamlexcelload import loadyaml
from TopEC.page_object.home_module.login_page import LoginPage

# 1.1.1.1登录功能验证
# 1-1-1.云服务器/集群信息导航栏信息校验
# (1)#使用不同权限用户登录测试
from TopHCS.page_object.login_module.loginpage import LoginPage


@allure.feature('登录测试')   #对模块功能进行标注
class TestLogin:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')  # 设置忽略ssl证书认证的错误，或者接收不信任的认证
        self.driver = webdriver.Chrome(chrome_options=options)

    # def teardown_method(self, method):
    #     self.driver.quit()


    @allure.title('登录信息校验')  # 对模块子功能进行标注
    def test_01_login(self):
        #self.driver = webdriver.Chrome()  #使用谷歌登录
        LoginPage(self.driver).login()




    # def test_login(self):
    #     _driver = self.driver
    #     login_user = 'system'
    #     login_username = 'xh'
    #     login_password = 'admin123.'
    #     lp = LoginPage1(_driver)
    #     lp.login1(login_user, login_username, login_password)
