import allure
import pytest
from selenium import webdriver

from TopHC.others.yamlexcelload import loadyaml
from TopHC.page_object.home_module.login_page import LoginPage

# 1.1.1.1登录功能验证
# 1-1-1.云服务器/集群信息导航栏信息校验
# (1)#使用不同权限用户登录测试
@allure.feature('登录测试')   #对模块功能进行标注
class TestLogin:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')  # 设置忽略ssl证书认证的错误，或者接收不信任的认证
        self.driver = webdriver.Chrome(chrome_options=options)

    def teardown_method(self, method):
        self.driver.quit()

    TEST_CASE_LINK = 'https://www.kdocs.cn/p/129592400066'
    @allure.testcase(TEST_CASE_LINK, '登录测试用例TH-CP-LOGIN-0001~0003')
    # --allure-link-pattern=issue:https://www.baidu.com/{}  #对应的TD链接
    @allure.issue('59561', '登录测试用例的对应的bug')  # bugID，传入上面的括号里
    @allure.title('登录信息校验')  # 对模块子功能进行标注
    @pytest.mark.parametrize("login_user, login_username, login_password", loadyaml(
        r'/TopHC/data/test_data/home_module_data/loginapi.yaml'))
    def test_01_login(self, login_user, login_username, login_password):
        #self.driver = webdriver.Chrome()  #使用谷歌登录
        lp = LoginPage(self.driver)
        lp.login(login_user, login_username, login_password)
        print('登录成功')

'''
    def test_login(self):
        _driver = self.driver
        login_user = 'system'
        login_username = 'xh'
        login_password = 'admin123.'
        lp = LoginPage(_driver)
        lp.login(login_user, login_username, login_password)
'''