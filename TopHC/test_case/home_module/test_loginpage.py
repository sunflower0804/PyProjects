import pytest
from selenium import webdriver


#使用不同权限用户登录测试
from TopHC.config.yamlload import loadyaml
from TopHC.page_object.home_module.login_page import LoginPage


class TestLogin:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')  # 设置忽略ssl证书认证的错误，或者接收不信任的认证
        self.driver = webdriver.Chrome(chrome_options=options)

    def teardown_method(self, method):
        self.driver.quit()


    @pytest.mark.parametrize("login_user, login_username, login_password", loadyaml(r'D:\WorkTools\PyProjects\TopHC\\test_case\home_module\\test_login.yaml'))
    def test_01_login(self, login_user, login_username, login_password):
        #self.driver = webdriver.Chrome()  #使用谷歌登录
        lp = LoginPage(self.driver)
        lp.login(login_user, login_username, login_password)

'''
    def test_login(self):
        _driver = self.driver
        login_user = 'system'
        login_username = 'xh'
        login_password = 'admin123.'
        lp = LoginPage(_driver)
        lp.login(login_user, login_username, login_password)
'''