'''
    每个页面都是独立的对象，main用来实现页面对象的组合，即从一个页面跳转到另一个页面
'''
from time import sleep

from selenium import webdriver

from PMO.base.base_page import BasePage
from PMO.page_object.home_page import HomePage
from PMO.page_object.login_page import LoginPage


class Main(BasePage):
    #先登录
    driver = webdriver.Chrome()
    username = 'xh'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(username, password)
    _driver = driver


    #1.首页模块入口
    def goto_main_homepage(self):
        sleep(1)
        return HomePage(self._driver)

