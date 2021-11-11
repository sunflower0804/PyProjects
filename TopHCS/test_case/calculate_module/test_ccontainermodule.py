import allure
import pytest
import yaml

from TopHCS.base.main import Main
from TopHCS.others.filepath import readFilepath
from TopHCS.others.yamlexcelload import loadyaml


#1.云容器页面
class TestCcontainerPage:
    def setup(self):
        self.main = Main(driver=None)

    # filepath = readFilepath.CcontainerTestDataPath
    # data = loadyaml(filepath)

    @allure.title('云容器页面入口校验')  # 对模块子功能进行标注
    def test_ccontainer(self):
        self.main.goto_ccontainer()

    # 1.1新建云容器（前置条件：已存在私有镜像仓库）
    # 111单个创建
    @allure.title('1.1新建云容器/111单个创建')
    def test_add_Ccontainer1(self):
        self.main.goto_ccontainer()
        pagedata = self.main.goto_containerpage().add_Ccontainer1()
        print(pagedata)
        assert '创建云容器1个成功！' == pagedata[0]

    # 112批量创建
    @allure.title('1.1新建云容器/112批量创建')
    def test_add_Ccontainer2(self):
        self.main.goto_ccontainer()
        pagedata = self.main.goto_containerpage().add_Ccontainer2()
        print(pagedata)
        assert '创建云容器3个成功！' == pagedata[0]

    # 1.2编辑云容器
    # 1.2.1云容器开机操作
    # 121-1单个开启
    @allure.title('1.2编辑云容器/1.2.1云容器开机操作/121-1单个开启')
    def test_start_Ccontainer1(self):
        self.main.goto_ccontainer()
        pagedata = self.main.goto_containerpage().start_Ccontainer1()
        print(pagedata)
        assert '启动云容器1个成功！' == pagedata[0]

    # 121-2批量开启
    @allure.title('1.2编辑云容器/1.2.1云容器开机操作/121-2批量开启')
    def test_start_Ccontainer2(self):
        self.main.goto_ccontainer()
        pagedata = self.main.goto_containerpage().start_Ccontainer2()
        print(pagedata)
        assert '启动云容器3个成功！' == pagedata[0]


    # 122挂起
    # 123恢复
    # 124分配