from time import sleep

import pytest
from selenium import webdriver

from PMO.base.main import Main
from PMO.config.yamlload import loadyaml
from PMO.page_object.home_page import HomePage
from PMO.page_object.login_page import LoginPage


class TestHomeSearch:
    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = HomePage()

    def teardown_class(cls) -> None:
        sleep(2)
        cls.driver.quit()

    @pytest.mark.parametrize('udata', loadyaml('./data/login.yaml'))  #调用封装的loadyaml函数，拿到yaml文件中的数据
    def test_001_login(self, udata):
        self.lp.login(udata['username'], udata['password'])

    @pytest.mark.parametrize('utxt', loadyaml('./data/home_search.yaml'))
    def test_home_search(self, utxt):
        self.ip.search(utxt['txt'])

if __name__ == '__main__':
    pytest.main()

#
