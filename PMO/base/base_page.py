'''
    BasePage类是POM中的基类，主要用于提供常用的函数，为页面对象类进行服务
'''
from selenium import webdriver

class BasePage:
    #虚构driver对象
    #driver = webdriver.Chrome()

    #构造函数
    def __init__(self, driver):
        self.driver = driver

    #访问url
    #def visit(self,url):     #这里直接调用，不用传参数（因为每个页面登录的URL都是固定的，不存在变化）
        #self.driver.get(url)

    def visit(self):
        self.driver.get(self.url)  #直接传入每次调用它的页面的url

    #元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    #输入
    def send(self, loc, txt):
        self.locator(loc).send_keys(txt)

    #点击
    def click(self, loc):
        self.locator(loc).click()

