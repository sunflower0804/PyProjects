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

    # # filepath = readFilepath.CcontainerTestDataPath
    # # data = loadyaml(filepath)
    #
    # @allure.title('云容器页面入口校验')  # 对模块子功能进行标注
    # def test_ccontainer(self):
    #     self.main.goto_ccontainer()
    #
    # # 1.1新建云容器（前置条件：已存在私有镜像仓库）
    # # 111单个创建
    # @allure.title('1.1新建云容器/111单个创建')
    # def test_add_Ccontainer1(self):
    #     self.main.goto_ccontainer()
    #     pagedata = self.main.goto_containerpage().add_Ccontainer1()
    #     print(pagedata)
    #     assert '创建云容器1个成功！' == pagedata[0]
    #
    # # 112批量创建
    # @allure.title('1.1新建云容器/112批量创建')
    # def test_add_Ccontainer2(self):
    #     self.main.goto_ccontainer()
    #     pagedata = self.main.goto_containerpage().add_Ccontainer2()
    #     print(pagedata)
    #     assert '创建云容器3个成功！' == pagedata[0]
    #
    # # 1.2云容器操作
    # # 1.2.1云容器开机操作
    # # 121-1单个开启
    # @allure.title('1.2云容器操作/1.2.1云容器开机操作/121-1单个开启')
    # def test_start_Ccontainer1(self):
    #     self.main.goto_ccontainer()
    #     pagedata = self.main.goto_containerpage().start_Ccontainer1()
    #     print(pagedata)
    #     assert '启动云容器1个成功！' == pagedata[0]
    #
    # # 121-2批量开启
    # @allure.title('1.2云容器操作/1.2.1云容器开机操作/121-2批量开启')
    # def test_start_Ccontainer2(self):
    #     self.main.goto_ccontainer()
    #     pagedata = self.main.goto_containerpage().start_Ccontainer2()
    #     print(pagedata)
    #     assert '启动云容器3个成功！' == pagedata[0]
    #
    #
    # # 122挂起
    # @allure.title('1.2云容器操作/122挂起')
    # def test_hang_Ccontainer2(self):
    #     self.main.goto_ccontainer()
    #     pagedata = self.main.goto_containerpage().hang_Ccontainer()
    #     print(pagedata)
    #     assert '挂起云容器1个成功！' == pagedata[0]
    #
    # # 123恢复
    # @allure.title('1.2云容器操作/123恢复')
    # def test_recover_Ccontainer(self):
    #     self.main.goto_ccontainer()
    #     pagedata = self.main.goto_containerpage().recover_Ccontainer()
    #     print(pagedata)
    #     assert '恢复云容器1个成功！' == pagedata[0]

    # 124分配
    @allure.title('1.2云容器操作/124分配')
    def test_allot_Ccontainer(self):
        self.main.goto_ccontainer()
        pagedata = self.main.goto_containerpage().allot_Ccontainer()
        print(pagedata)
        assert '云容器0000分配用户成功！' == pagedata[0]

#     # 1.3编辑云容器
#     # 131开机编辑
#     @allure.title('1.3编辑云容器/131开机编辑')
#     def test_edit_Ccontainer1(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_containerpage().edit_Ccontainer1()
#         print(pagedata)
#         # assert '提示: 添加磁盘仅支持停止、退出状态可支持操作！' == pagedata[0][0]
#         # assert '云容器开启高可用不支持【添加主机映射】' == pagedata[1][0]
#         # assert '云容器0000添加网卡成功！' == pagedata[2][0]
#
#
#     # 132关机编辑
#     @allure.title('1.3编辑云容器/132关机编辑')
#     def test_edit_Ccontainer2(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_containerpage().edit_Ccontainer2()
#         print(pagedata)
#         # assert '云容器0000添加磁盘成功！' == pagedata[0][0]
#         # assert '云容器主机映射添加成功' == pagedata[1][0]
#         # assert '提示: 运行状态才支持此操作！' == pagedata[2][0]
#         # assert '云容器端口映射添加成功' == pagedata[3][0]
#
#
# #2.密钥页面
# class TestCipherPage:
#     def setup(self):
#         self.main = Main(driver=None)
#
#     # filepath = readFilepath.CcontainerTestDataPath
#     # data = loadyaml(filepath)
#
#     #密钥页面入口校验
#     @allure.title('密钥页面入口校验')  # 对模块子功能进行标注
#     def test_ciper(self):
#         self.main.goto_ccontainer()
#         self.main.goto_ciperpage()
#
#     #2.1新建密钥
#     @allure.title('2.1新建密钥')
#     def test_add_Cipher(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_ciperpage().add_Cipher()
#         print(pagedata)
#         assert '创建密钥成功！' == pagedata[0]
#
#     # 2.2编辑密钥
#     @allure.title('#2.2编辑密钥')
#     def test_edit_Cipher(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_ciperpage().edit_Cipher()
#         print(pagedata)
#         assert '编辑密钥成功！' == pagedata[0]
#
#     #2.3删除密钥
#     @allure.title('#2.3删除密钥')
#     def test_del_Cipher(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_ciperpage().del_Cipher()
#         print(pagedata)
#         assert '删除成功！' == pagedata[0]
#
# #3.配置页面
# class TestDisposePage:
#     def setup(self):
#         self.main = Main(driver=None)
#
#     # filepath = readFilepath.CcontainerTestDataPath
#     # data = loadyaml(filepath)
#
#     #配置页面入口校验
#     @allure.title('密钥页面入口校验')  # 对模块子功能进行标注
#     def test_ciper(self):
#         self.main.goto_ccontainer()
#         self.main.goto_disposepage()
#
#     # 3.1添加镜像
#     # 311添加第三方镜像加速器
#     @allure.title('3.1添加镜像/311添加第三方镜像加速器')
#     def test_add_Cipher(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_disposepage().add_Image1()
#         print(pagedata)
#         assert '云容器镜像设置成功！' == pagedata[0]
#
#     # 312添加私有镜像源
#     @allure.title('3.1添加镜像/312添加私有镜像源')
#     def test_add_Cipher(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_disposepage().add_Image2()
#         print(pagedata)
#         assert '云容器镜像设置成功！' == pagedata[0]
#
#     #3.2删除镜像
#     @allure.title('3.2删除镜像')
#     def test_del_Cipher(self):
#         self.main.goto_ccontainer()
#         pagedata = self.main.goto_disposepage().del_Image()
#         print(pagedata)
#         assert '云容器镜像删除成功！' == pagedata[0]