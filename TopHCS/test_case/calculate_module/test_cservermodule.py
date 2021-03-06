from time import sleep

import allure
import pytest

from TopHCS.base.main import Main
from TopHCS.others.filepath import readFilepath
from TopHCS.others.yamlexcelload import loadyaml


@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('云服务器页面')  ##对模块子功能进行标注
class TestServicePage:
    # def setup_method(self):
    #     self.main = Main(driver=None)

    def setup_class(self):
        self.main = Main(driver=None)

    # filepath = readFilepath.ServerTestDataPath
    # data = loadyaml(filepath)

    @allure.title('云服务器页面入口校验')  # 对模块子功能进行标注
    def test_cservice(self):
        self.main.goto_cserver()

    # 1.1新建云服务器
    # 111创建云服务器
    # 111-1自定义
    #(1)存储类型1（云硬盘scsi+云盘2.0）0000
    @allure.title('111创建云服务器/111-1自定义/存储类型1（云硬盘scsi+云盘2.0）')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().create_VM1()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

    #(2)存储类型2（云硬盘iscsi+高效云盘）0001
    @allure.title('111创建云服务器/111-1自定义/存储类型2（云硬盘scsi+云盘2.0）')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().create_VM2()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

'''
    #(3)存储类型3（共享存储+云盘1.0） (前置条件：存在共享存储池) 0002
    @allure.title('111创建云服务器/111-1自定义/存储类型3（共享存储+云盘1.0）')
    # @pytest.mark.skipif(1 > 7, '不满足迁移条件跳过这条用例')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_VM3(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().create_VM3()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

    # 111-2创建云服务器/来源于模板
    # (1)创建模板  0000
    @allure.title('111-2创建云服务器/来源于模板/(1)创建模板')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_VMML(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().create_VMML()
        print(pagedata)
        assert '云服务器转换成模板0000成功!' == pagedata[0]

    # (2)模板创建云服务器  0000
    @allure.title('111-2创建云服务器/来源于模板/(2)模板创建云服务器器')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_VM4(self):
        sleep(5)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().create_VM4()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

    # 111-3创建云服务器/来源于规格 0003
    @allure.title('111-3创建云服务器/来源于规格/(1)规格创建云服务器')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_VM5(self):
        sleep(5)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().create_VM5()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

    # 1.2 编辑云服务器 0000
    # 121添加设备
    @allure.title('1.2编辑云服务器/121添加设备')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_edit_VM1(self):
        sleep(5)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().edit_VM1()
        print(pagedata)
        assert '云服务器0000添加网卡成功！' == pagedata[0]

    # 122删除设备
    @allure.title('1.2编辑云服务器/122删除设备')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_edit_VM2(self):
        sleep(5)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().edit_VM2()
        print(pagedata)
        str = pagedata[0]
        str1 = str[-5:-1]
        print(str1)
        assert '卸载成功' == str1

    # 1.3 删除云服务器
    # 131彻底删除   0001
    @allure.title('1.3 删除云服务器/131彻底删除')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_detel_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().detel_VM1()
        print(pagedata)
        assert '云服务器0001删除成功！' == pagedata[0]

    # 132彻底删除+同步删除卷   0002
    @allure.title('1.3 删除云服务器/132彻底删除+同步删除卷')
    # @pytest.mark.skipif(1 > 7, '不满足迁移条件跳过这条用例')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_detel_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().detel_VM2()
        print(pagedata)
        assert '云服务器0002删除成功！' == pagedata[0]

    # 133非彻底删除    0003
    @allure.title('1.3 删除云服务器/133非彻底删除')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_detel_VM3(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().detel_VM3()
        print(pagedata)
        assert '云服务器0003删除成功！' == pagedata[0]

    # 1.1.2 迁入虚拟机(前置条件：存在已开启converter的虚拟机，且满足迁移条件)  0004
    @allure.title('1.1.2 迁入虚拟机')
    # @pytest.mark.skipif(1 > 7, '不满足迁移条件跳过这条用例')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_immigrate_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().immigrate_VM1()
        print(pagedata)
        assert '创建云服务器 1个成功！' == pagedata[0]

    # 113 导入云服务器(前置条件：镜像仓库中存在ova/tva模板)  0005
    # 113-1镜像仓库导入/ova
    @allure.title('113 导入云服务器/113-1镜像仓库导入/(1)ova导入')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_export_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().export_VM1()
        print(pagedata)
        assert '创建云服务器 1 个成功！' == pagedata[0]

    # 113-1镜像仓库导入/tva   0006
    @allure.title('113 导入云服务器/113-1镜像仓库导入/(2)tva导入')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_export_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().export_VM2()
        print(pagedata)
        assert '创建云服务器 1 个成功！' == pagedata[0]

    # 1.1.3-2存储介质导入
    # (1)ova导入    0007
    @allure.title('113 导入云服务器/1.1.3-2存储介质导入/(1)ova导入')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    # @pytest.mark.skipif(1 > 7, '不满足条件跳过这条用例')
    def test_export_VM3(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().export_VM3()
        print(pagedata)
        assert '创建云服务器 1 个成功！' == pagedata[0]

    # (2)tva导入  0008
    @allure.title('113 导入云服务器/1.1.3-2存储介质导入/(2)tva导入')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    # @pytest.mark.skipif(1 > 7, '不满足条件跳过这条用例')
    def test_export_VM4(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().export_VM4()
        print(pagedata)
        assert '创建云服务器 1 个成功！' == pagedata[0]

    # 1.4 云服务器的操作  0000
    #141开机
    @allure.title('1.4 云服务器的操作/141开机')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM1()
        print(pagedata)
        assert '云服务器启动成功！' == pagedata[0]

    #142重启  0000
    @allure.title('1.4 云服务器的操作/142重启')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM2()
        print(pagedata)
        assert '云服务器0000重启成功！' == pagedata[0]

    #143挂起 0000
    @allure.title('1.4 云服务器的操作/143挂起')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM3(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM3()
        print(pagedata)
        assert '云服务器0000挂起成功！' == pagedata[0]

    #144恢复  0000
    @allure.title('1.4 云服务器的操作/144恢复')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM4(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM4()
        print(pagedata)
        assert '云服务器0000恢复成功！' == pagedata[0]

    #145休眠  0000
    @allure.title('1.4 云服务器的操作/145休眠')
    @pytest.mark.flaky(reruns=3, reruns_delay=2) #失败后两秒重试，重试3次
    def test_operate_VM5(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM5()
        print(pagedata)
        assert '云服务器0000休眠成功！' == pagedata[0]

    #146唤醒  0000
    @allure.title('1.4 云服务器的操作/146唤醒')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM6(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM6()
        print(pagedata)
        assert '云服务器0000唤醒成功！' == pagedata[0]

    #147导出PDF(开机状态)  0000
    @allure.title('1.4 云服务器的操作/147导出PDF')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM7(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM7()
        print(pagedata)
        assert '云服务器报表' == pagedata[0]

    #148关机  0000
    @allure.title('1.4 云服务器的操作/148关机')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM8(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM8()
        print(pagedata)
        assert '云服务器0000关闭成功！' == pagedata[0]

    #149分配  0000
    @allure.title('1.4 云服务器的操作/149分配')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM9(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM9()
        print(pagedata)
        assert '分配1台云服务器成功!' == pagedata[0]

    #1410移动 0000
    @allure.title('1.4 云服务器的操作/150移动')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM10(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM10()
        print(pagedata)
        assert '云服务器移动分组成功！' == pagedata[0]

    #1411启动顺序  0000
    @allure.title('1.4 云服务器的操作/151启动顺序')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_operate_VM11(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().operate_VM11()
        print(pagedata)
        assert '云服务器启动顺序设置成功！' == pagedata[0]

    #1412迁移  0000
    #1412-1集群内迁移
    @allure.title('1.4 云服务器的操作/1412迁移/1412-1集群内迁移')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_migrate_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().migrate_VM1()
        print(pagedata)
        assert '云服务器0000迁移请求已成功发送！' == pagedata[0]

    #1412-2跨集群迁移（存在目的集群）  ###还未写完
    @allure.title('1.4 云服务器的操作/1412迁移/1412-2跨集群迁移')
    # @pytest.mark.skipif(1 > 7, '不满足条件跳过这条用例')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_migrate_VM2(self):
        sleep(13)
        self.main.goto_cserver()
        # pagedata = self.main.goto_serverpage().migrate_VM2()
        # print(pagedata)
        # assert '云服务器0000迁移请求已成功发送！' == pagedata[0]

    #1412-3迁移到vsphere（存在目的集群） ###还未写完
    @allure.title('1.4 云服务器的操作/1412迁移/1412-3迁移到vsphere')
    @pytest.mark.skipif(1 > 7, '不满足条件跳过这条用例')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_migrate_VM3(self):
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().migrate_VM3()
        print(pagedata)
        assert '云服务器0000迁移请求已成功发送！' == pagedata[0]

    #1413克隆
    #1413-1全量克隆
    #（1）不基于快照  0000
    @allure.title('1.4 云服务器的操作/1413克隆/1413-1全量克隆/（1）不基于快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_clone_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().clone_VM1()
        print(pagedata)
        assert '云服务器成功发起1个克隆请求,云服务器正在克隆中,结果请稍后查看' == pagedata[0][0]
        assert '云服务器0000-clone1删除成功！' == pagedata[1][0]

    #（2）基于快照  0000
    @allure.title('1.4 云服务器的操作/1413克隆/1413-1全量克隆/（2）基于快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_clone_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().clone_VM2()
        print(pagedata)
        assert '云服务器成功发起1个克隆请求,云服务器正在克隆中,结果请稍后查看' == pagedata[0][0]
        assert '云服务器0000-kz-clone1删除成功！' == pagedata[1][0]

    # 1413-2链接克隆  0000
    @allure.title('1.4 云服务器的操作/1413克隆/1413-2链接克隆')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_clone_VM3(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().clone_VM3()
        print(pagedata)
        assert '云服务器成功发起1个克隆请求,云服务器正在克隆中,结果请稍后查看' == pagedata[0][1]
        assert '云服务器0000-lj-clone1删除成功！' == pagedata[1][0]

    # 1413-3跨租户克隆  #报错：(//span[@class='el-switch__core'])[2]元素未找到
    @allure.title('1.4 云服务器的操作/1413克隆/1413-3跨租户克隆')
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_clone_VM4(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().clone_VM4()
        print(pagedata)

    #1414导入
    #1414-1镜像仓库导入
    @allure.title('1.4 云服务器的操作/1414导入/1414-1镜像仓库导入')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_import_DISK1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().import_DISK1()
        print(pagedata)

    #1414-2ISCSI导入  0005
    @allure.title('1.4 云服务器的操作/1414导入/1414-2ISCSI导入')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_import_DISK2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().import_DISK2()
        print(pagedata)

    #1415导出
    # 1415-1磁盘导出 0006
    @allure.title('1.4 云服务器的操作/1415导出/1415-1磁盘导出')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_exports_DISK1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().exports_DISK1()
        print(pagedata)
        assert '云服务器导出中' == pagedata[0]

    # 1415-2云服务器导出
    # （1）导出到镜像仓库  0007
    @allure.title('1.4 云服务器的操作/1415导出/1415-2云服务器导出/（1）导出到镜像仓库')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_exports_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().exports_VM1()
        print(pagedata)
        assert '云服务器导出中' == pagedata[0]

    # （2）导出到存储介质  0008
    @allure.title('1.4 云服务器的操作/1415导出/1415-2云服务器导出/（2）导出到存储介质')
    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_exports_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().exports_VM2()
        print(pagedata)
        assert '云服务器导出中' == pagedata[0]

    #1.5云服务器基本信息页  0000
    # 151 云服务器cpu操作
    # 151-1 关机状态下添加/减小cpu、修改基准类型
    @allure.title('1.5云服务器基本信息页/151云服务器cpu操作/151-1 关机状态下添加/减小cpu、修改基准类型')
    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_basic_ADDCPU1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_ADDCPU1()
        print(pagedata)
        assert '云服务器插槽核数修改成功！' == pagedata[0][0]
        assert '云服务器插槽核数修改成功！' == pagedata[0][1]
        assert '云服务器插槽数修改成功！' == pagedata[1][0]
        assert '云服务器插槽数修改成功！' == pagedata[1][1]
        assert '云服务器处理器修改成功！' == pagedata[2][0]
        assert '云服务器处理器修改成功！' == pagedata[2][1]
        assert '修改基准类型成功' == pagedata[3][0]

    # 151-2 开机状态下添加/减小cpu开机添加cpu
    @allure.title('1.5云服务器基本信息页/151云服务器cpu操作/151-2 开机状态下添加/减小cpu开机添加cpu')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_ADDCPU2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_ADDCPU2()
        print(pagedata)
        assert '2' == pagedata[0]
        assert '在非关机状态下：不能减少处理器数量' == pagedata[1]

    # 151-3 开启/关闭预留cpu、cpu自动扩展
    @allure.title('1.5云服务器基本信息页/151云服务器cpu操作/151-3开启/关闭预留cpu、cpu自动扩展')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITCPU3(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITCPU3()
        print(pagedata)
        assert '云服务器预留CPU修改成功' == pagedata[0][0]
        assert '云服务器NUMA亲和性修改成功' == pagedata[1][0]
        assert '云服务器CPU自动扩展修改成功！' == pagedata[2][0]
        assert '云服务器CPU自动扩展值修改成功！' == pagedata[2][1]

    # 152云服务器内存操作
    # 152-1 关机状态下添加/减小内存、预留内存、内存自动扩展
    @allure.title('1.5云服务器基本信息页/152云服务器内存操作/152-1 关机状态下添加/减小内存、预留内存、内存自动扩展')
    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_basic_ADDMEM1(self):
        sleep(5)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_ADDMEM1()
        print(pagedata)
        assert '云服务器内存修改成功' == pagedata[0][0]
        assert '云服务器内存修改成功' == pagedata[0][1]
        assert '云服务器预留内存修改成功' == pagedata[1][0]
        assert '云服务器内存自动扩展修改成功！' == pagedata[2][0]
        assert '云服务器内存自动扩展值修改成功！' == pagedata[3][0]

    # 152-2开机状态下添加/减小内存
    @allure.title('1.5云服务器基本信息页/152云服务器内存操作/152-2开机状态下添加/减小内存')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_ADDMEM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_ADDMEM2()
        print(pagedata)
        assert '在非关机状态下：不能减少内存' == pagedata[0][0]
        assert '云服务器内存修改成功' == pagedata[1][0]

    # 153 高可用
    # 153-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/153高可用/153-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITHUSE(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITHUSE()
        print(pagedata)
        assert '云服务器高可用模式修改成功！' == pagedata[0][0]
        assert '云服务器高可用模式修改成功！' == pagedata[1][0]

    # 154 重要云服务器（开启高可用）
    # 154-1 高/低/中
    @allure.title('1.5云服务器基本信息页/154重要云服务器/154-1高/低/中')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITIMPORTANT(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITIMPORTANT()
        print(pagedata)
        assert '云服务器重要云服务器修改成功！' == pagedata[0][0]
        assert '云服务器重要云服务器修改成功！' == pagedata[1][0]

    # 155 内存巨页  (需关机)
    # 155-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/155内存巨页/155-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITMEMHUGE(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITMEMHUGE()
        print(pagedata)
        assert '云服务器内存巨页修改成功' == pagedata[0][0]
        assert '云服务器内存巨页修改成功' == pagedata[1][0]

    # 156 启动  (需关机)
    # 156-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/156启动/156-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITSTART(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITSTART()
        print(pagedata)
        assert '云服务器启动修改成功！' == pagedata[0][0]
        assert '云服务器启动修改成功！' == pagedata[1][0]

    # 157 嵌套虚拟化
    # 157-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/154嵌套虚拟化/154-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITNEST(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITNEST()
        print(pagedata)
        assert '云服务器嵌套虚拟化修改成功！' == pagedata[0][0]
        assert '云服务器嵌套虚拟化修改成功！' == pagedata[1][0]

    # 158 数据本地化
    # 158-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/158数据本地化/158-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITDATALOCAL(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITDATALOCAL()
        print(pagedata)
        assert '云服务器数据本地化设置成功！' == pagedata[0][0]
        assert '云服务器数据本地化设置成功！' == pagedata[1][0]

    # 159 内存安全
    # 159-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/159内存安全/159-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITMEMSAFE(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITMEMSAFE()
        print(pagedata)
        assert '云服务器修改安全内存成功！' == pagedata[0][0]
        assert '云服务器修改安全内存成功！' == pagedata[1][0]

    # 1510 启用双活（前置条件：需授权，存在两个资源池）
    # 1510-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/1510启用双活/1510-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITDLIVE(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITDLIVE()
        print(pagedata)
        assert '云服务器设置开启双活！' == pagedata[0][0]
        assert '云服务器设置关闭双活！' == pagedata[1][0]

    # 1512 绑定主资源池（前置条件：启用双活）
    # 1512-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/1512绑定主资源池/1512-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITBIND(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITBIND()
        print(pagedata)
        assert '云服务器设置开启主资源池绑定！' == pagedata[0][0]
        assert '云服务器设置关闭主资源池绑定！' == pagedata[1][0]

    # 1513 VNC
    # 1513-1 关机状态下开启
    @allure.title('1.5云服务器基本信息页/1513VNC/1513-1关机状态下开启')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITVNC1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITVNC1()
        print(pagedata)
        assert '云服务器VNC修改成功！' == pagedata[0][0]

    # 1513-2 开机状态下检查VNC配置信息
    @allure.title('1.5云服务器基本信息页/1513VNC/1513-2开机状态下检查VNC配置信息')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITVNC2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITVNC2()
        print(pagedata)
        assert '访问路径：' == pagedata[0][0]

    # 1514 Spice
    # 1514-1 开机状态下检查Spice配置信息
    @allure.title('1.5云服务器基本信息页/1514Spice/1514-1开机状态下检查Spice配置信息')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITSPICE1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITSPICE1()
        print(pagedata)
        assert ':' in pagedata[0]

    # 1514-2 关机状态下检查Spice配置信息
    @allure.title('1.5云服务器基本信息页/1514Spice/1514-2关机状态下检查Spice配置信息')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITSPICE2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITSPICE2()
        print(pagedata)
        assert ':' not in pagedata[0]

    #1515异常检测
    #1515-1 开启/关闭
    @allure.title('1.5云服务器基本信息页/1515异常检测/1515-1开启/关闭')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITUNUSUAL(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITUNUSUAL()
        print(pagedata)
        assert '云服务器异常检测修改成功！' == pagedata[0][0]
        assert '云服务器异常检测修改成功！' == pagedata[1][0]

    # 1516自动配置
    # 1516-1选择主机
    @allure.title('1.5云服务器基本信息页/1516自动配置/1516-1选择主机')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITDISPOSE1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITDISPOSE1()
        print(pagedata)
        assert '启动配置设置为主机启动！' == pagedata[0]

    # 1516-2选择标签
    @allure.title('1.5云服务器基本信息页/1516自动配置/1516-2选择标签')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_EDITDISPOSE2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_EDITDISPOSE2()
        print(pagedata)
        assert '设置为标签启动！' == pagedata[0]


    # 1.6 云服务器快照信息页面
    # 161普通快照
    # 161-1添加快照
    @allure.title('1.6 云服务器快照信息页面/161普通快照/161-1添加快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_snap_ADD1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().snap_ADD1()
        print(pagedata)
        assert '快照ptkz-001添加成功！' == pagedata[0]

    # 161-2回滚快照(需关机)
    @allure.title('1.6 云服务器快照信息页面/161普通快照/161-2回滚快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_snap_ROLLBACK1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().snap_ROLLBACK1()
        print(pagedata)
        assert '快照回滚成功!' == pagedata[0]

    # 161-3删除快照
    @allure.title('1.6 云服务器快照信息页面/161普通快照/161-3删除快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_snap_DEL1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().snap_DEL1()
        print(pagedata)
        assert '快照ptkz-002已成功删除！' == pagedata[0][0]
        assert '快照ptkz-001已成功删除！' == pagedata[1][0]

    # 162内存快照（租户绑定的资源池已开启内存快照空间，虚拟机处于开机状态）
    # 162-1添加内存快照
    @allure.title('1.6 云服务器快照信息页面/162内存快照/162-1添加内存快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_snap_ADD2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().snap_ADD2()
        print(pagedata)
        assert '快照nckz-001添加成功！' == pagedata[0]

    # 162-2回滚快照(需关机)
    @allure.title('1.6 云服务器快照信息页面/162内存快照/162-2回滚快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skipif(1 > 7, '不满足条件跳过这条用例')
    def test_snap_ROLLBACK2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().snap_ROLLBACK2()
        print(pagedata)
        assert '快照回滚成功!' == pagedata[0]

    # 162-3删除快照
    @allure.title('1.6 云服务器快照信息页面/162内存快照/162-3删除快照')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_snap_DEL2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().snap_DEL2()
        print(pagedata)
        assert '快照nckz-002已成功删除！' == pagedata[0][0]
        assert '快照nckz-001已成功删除！' == pagedata[1][0]

    #1.7 云服务器监控信息页面
    # 171 cgt安装
    @allure.title('1.7 云服务器监控信息页面/171 cgt安装')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_CGT_ADD1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().basic_CGT_ADD1()
        print(pagedata)
        assert '云服务器设置Guest-Agent-Tools成功！' == pagedata[0][0]
        assert '云服务器0000卸载光驱成功！' == pagedata[1][0]

    # 172 cgt监控
    @allure.title('1.7 云服务器监控信息页面/172 cgt监控')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_basic_CGT_SEARCH1(self):
        sleep(13)
        self.main.goto_cserver()
        # pagedata = self.main.goto_serverpage().basic_CGT_SEARCH1()
        # print(pagedata)
        # assert '磁盘监控' == pagedata[0]

    #1.8云服务器备份信息页面（已存在备份点：ptbf-001）
    # 181添加备份
    # 181-1单卷添加备份
    @allure.title('1.8云服务器备份信息页面/181添加备份/181-1单卷添加备份')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_backup_SINGEL_ADD1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().backup_SINGEL_ADD1()
        print(pagedata)
        assert '成功创建备份bf001' == pagedata[0]

    # 181-2多卷添加备份
    @allure.title('1.8云服务器备份信息页面/181添加备份/181-2多卷添加备份')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_backup_MULTI_ADD1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().backup_MULTI_ADD1()
        print(pagedata)
        assert '成功创建备份bf002' == pagedata[0]

    # 182备份恢复
    # 182-1单卷备份恢复
    @allure.title('1.8云服务器备份信息页面/182备份恢复/182-1单卷备份恢复')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_backup_RECOVERY_SINGEL1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().backup_RECOVERY_SINGEL1()
        print(pagedata)
        assert '备份bf001恢复请求发送成功!' == pagedata[0]

    # 182-2多卷备份恢复
    @allure.title('1.8云服务器备份信息页面/182备份恢复/182-2多卷备份恢复')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_backup_RECOVERY_MULTI1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().backup_RECOVERY_MULTI1()
        print(pagedata)
        assert '备份bf002恢复请求发送成功!' == pagedata[0]

    # 183删除备份
    @allure.title('1.8云服务器备份信息页面/183删除备份')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_backup_DEL1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().backup_DEL1()
        print(pagedata)
        assert '删除bf001成功!' == pagedata[0]

    #1.9云服务器CDP备份信息页面(放在运维模块写)
    # 191 创建CDP备份
    # 192 删除CDP备份
    # 193 CDP备份恢复
    # 194 CDP备份快照回滚

# 2模板页面
@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('模板页面')  ##对模块子功能进行标注
class TestMouldPage:
    def setup_class(self):
        self.main = Main(driver=None)

    # filepath = readFilepath.MouldTestPath
    # data = loadyaml(filepath)

    @allure.title('模板页面入口校验')  # 对模块子功能进行标注
    def test_cservice(self):
        self.main.goto_cserver()

    # 2.1模板转换 --pass

    # 2.2基于模板创建虚拟机
    @allure.title('1414模板/1414-2模板恢复')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_mould_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_mouldpage().mould_VM1()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

    # 2.3模板恢复
    @allure.title('1414模板/1414-2模板恢复')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_mould_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_mouldpage().mould_VM2()
        print(pagedata)
        assert '模板转换云服务器成功！' == pagedata[0]


# 3.规格页面
@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('规格页面')  ##对模块子功能进行标注
class TestSpecsPage:
    def setup_class(self):
        self.main = Main(driver=None)

    # filepath = readFilepath.SpecsTestPath
    # data = loadyaml(filepath)

    @allure.title('规格页面入口校验')  # 对模块子功能进行标注
    def test_cservice(self):
        self.main.goto_cserver()

    # 3.1添加规格
    @allure.title('3.1添加规格')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_specs_VM1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_specs().creat_specs1()
        print(pagedata)
        assert '创建云服务器1个成功！' == pagedata[0]

    # 3.2删除规格
    @allure.title('3.2删除规格')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_specs_VM2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_specs().delete_specs2()
        print(pagedata)
        assert '规格specs删除成功！' == pagedata[0]



# 4.备份页面
@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('备份页面')  ##对模块子功能进行标注
class TestBackupPage:
    def setup_class(self):
        self.main = Main(driver=None)

    # filepath = readFilepath.BackupTestPath
    # data = loadyaml(filepath)

    @allure.title('备份页面入口校验')  # 对模块子功能进行标注
    def test_cservice(self):
        self.main.goto_cserver()

    # 4.1远端导入备份
    @allure.title('4.1远端导入备份')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_remote_backup1(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_backup().remote_backup1()
        print(pagedata)
        assert '导入成功！' == pagedata[0]

    # 4.2远端备份恢复
    @allure.title('4.2远端备份恢复')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_remote_backup2(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_backup().remote_backup2()
        print(pagedata)
        # assert '备份恢复成功！' == pagedata[0]


# 5.策略页面
@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('备份页面')  ##对模块子功能进行标注
class TestStrategyPage:
    def setup_class(self):
        self.main = Main(driver=None)

    # filepath = readFilepath.StrategyTestPath
    # data = loadyaml(filepath)

    @allure.title('备份页面入口校验')  # 对模块子功能进行标注
    def test_cservice(self):
        self.main.goto_cserver()

    # 5.1 开关机策略
    #（1）创建开关机策略
    @allure.title('5.1 开关机策略/创建开关机策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_strategy11(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().creat_strategy11()
        print(pagedata)
        assert '提交开关机策略成功！' == pagedata[0]

    #（2）开启/关闭开关机策略
    @allure.title('5.1 开关机策略/(开启/关闭)开关机策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_updown_strategy11(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().updown_strategy11()
        print(pagedata)
        assert '停止策略成功！' == pagedata[0][0]
        assert '启动策略成功！' == pagedata[1][0]

    #（3）编辑开关机策略
    @allure.title('5.1 开关机策略/编辑开关机策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_edit_strategy11(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().edit_strategy11()
        print(pagedata)
        assert '编辑开关机策略成功！' == pagedata[0]

    #（4）删除开关机策略
    @allure.title('5.1 开关机策略/删除开关机策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_del_strategy11(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().del_strategy11()
        print(pagedata)
        assert '删除开关机策略成功！' == pagedata[0]

    # 5.2 快照策略
    #（1）创建快照策略
    @allure.title('5.2 快照策略/创建快照策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_strategy21(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().creat_strategy21()
        print(pagedata)
        assert '提交快照策略成功！' == pagedata[0]

    #（2）开启/关闭快照策略
    @allure.title('5.2 快照策略/(开启/关闭)快照策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_updown_strategy21(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().updown_strategy21()
        print(pagedata)
        assert '停止策略成功！' == pagedata[0][0]
        assert '启动策略成功！' == pagedata[1][0]

    #（3）编辑快照策略
    @allure.title('5.2 快照策略/编辑快照策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_edit_strategy21(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().edit_strategy21()
        print(pagedata)
        assert '编辑快照策略成功！' == pagedata[0]

    #（4）删除快照策略
    @allure.title('5.2 快照策略/删除快照策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_del_strategy21(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().del_strategy21()
        print(pagedata)
        assert '删除策略成功！' == pagedata[0]

    # 5.3 备份策略
    #（1）创建备份策略
    @allure.title('5.3 备份策略/备份快照策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_creat_strategy31(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().creat_strategy31()
        print(pagedata)
        assert '提交备份策略成功！' == pagedata[0]

    #（2）开启/关闭备份策略
    @allure.title('5.3 备份策略/(开启/关闭)备份策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_updown_strategy31(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().updown_strategy31()
        print(pagedata)
        assert '停止策略成功！' == pagedata[0][0]
        assert '启动策略成功！' == pagedata[1][0]

    #（3）编辑备份策略
    @allure.title('5.3 备份策略/编辑备份策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_edit_strategy31(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().edit_strategy31()
        print(pagedata)
        assert '编辑备份策略成功！' == pagedata[0]

    #（4）删除备份策略
    @allure.title('5.3 备份策略/删除备份策略')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败后两秒重试，重试3次
    def test_del_strategy31(self):
        sleep(3)
        self.main.goto_cserver()
        pagedata = self.main.goto_strategy().del_strategy31()
        print(pagedata)
        assert '删除策略成功！' == pagedata[0]
        '''
'''
allure常用特性
希望在报告中看到测试功能，子功能或场景，测试步骤，包括测试附加信息可以使用@feature,@story,@step,@attach

步骤：

import allure
功能上加@allure.feature("功能名称")
子功能上加@allure.story("子功能名称")
步骤上加@allure.step("步骤细节")
@allure.attach("具体文本信息")，需要附加的信息，可以是数据，文本，图片，视频，网页
如果只测试部分功能运行的时候可以加限制过滤：
pytest 文件名 --allure-features "需要运行的功能名称" 
allure特性—feature/story

@allure.feature与@allure.store的关系

feature相当于一个功能，一个大的模块，将case分类到某个feature中，报告中在behaviore中显示，相当于testsuite
story相当于对应这个功能或者模块下的不同场景，分支功能，属于feature之下的结构，报告在features中显示，相当于testcase
feature与story类似于父与子关系
step特性

测试过程中每个步骤，一般放在具体逻辑方法中
可以放在关键步骤中，在报告中显示
在app,web自动化测试中，建议每切换到一个新的页面当做一个step
用法：
@allure.step() 只能以装饰器的形式放在类或方法上面
with allure.step():  可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
运行：

　　在测试执行期间收集结果

　　pytest [测试文件] -s -q --alluredir=./result --clean-alluredir

--alluredir这个选项，用于指定存储测试结果的路径
--clean-alluredir 这个选项用来清除之前生成的结果
查看测试报告：

　　方法一：测试完成后查看实际报告，在线看报告，会直接打开默认浏览器展示当前报告

　　　　　　allure serve ./result 

　　方法二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤

　　　　　　生成报告：

　　　　　　　　　　allure generate ./result -o ./report --clean   (注意：--clean用来清除之前已生成的报告)

　　　　　　打开报告：

　　　　　　　　　　allure open -h 127.0.0.1 -p 8883 ./report   (该方法直接生成一个tomcat服务，可远程访问)

'''




