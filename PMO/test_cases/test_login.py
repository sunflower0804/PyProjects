import pytest
import yaml
from selenium import webdriver

#测试用例的设计
from PMO.page_object.login_page import LoginPage


class Test_Login():
    '''
    def test_login(self):
        driver = webdriver.Chrome()
        username = 'xh'
        password = '123456'
        lp = LoginPage(driver)
        lp.login(username, password)
    '''

    @pytest.mark.parametrize("username, password", yaml.safe_load(open(r'D:\WorkTools\PyProjects\PMO\data\login.yaml')))
    def test_login(self, username, password):
        driver = webdriver.Chrome()
        lp = LoginPage(driver)
        lp.login(username, password)



if __name__ == '__main__':
    pytest.main()