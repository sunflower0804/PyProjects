from time import sleep

from selenium.webdriver.common.by import By

from TopHC.base.basepage import BasePage


# 对首页(概览)页面内容进行检查
class HomePage(BasePage):
    #1.1概览页面UI信息检查
    #（1）“集群状态”展示框
    def search_text1(self):
        sleep(2)
        return self.find(By.XPATH,'//*[@id="panel-c-scroll"]/div[1]/section/section/div/div[1]/section[1]/div/div[1]/div/div[1]/h4').text
        #return self.steps(r"D:\WorkTools\PyProjects\TopHC\data\home_module\homeapi.yaml")

    #D:/WorkTools/PyProjects/TopHC/page_object/home_module


    #（2）“集群负载”展示框



    #1.2.1首页功能1验证：创建云容器入口
    def add_cloud_container(self):
        return self.steps(r"/TopHC/page_object/home_module/home_add_cloud_container1.yaml")
        #sleep(1)
        #self.steps(r"D:/WorkTools/PyProjects/TopHC/page_object/home_module/home_add_cloud_container2.yaml")

    #1.2.2首页功能2验证：创建云服务器入口
    def add_cloud_service(self):
        pass
        return text

    # 1.2.3首页功能3验证：创建云硬盘入口
    def add_cloud_disk(self):
        pass
        return True

    # 1.2.4首页功能4验证：创建网络拓扑入口
    def add_network_topo(self):
        pass
        return True
#import  os

#def test_tt():
    #print(os.getcwd())