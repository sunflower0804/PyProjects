from time import sleep

import pytest
from selenium.webdriver.common.by import By
from TopHCS.base.basepage import BasePage
from TopHCS.others.yamlexcelload import loadyaml
from TopHCS.others.filepath import readFilepath

#云服务器模块
# 1.云服务器页面
class ServicePage(BasePage):
    filepath = readFilepath.ServerDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析
    # 1.1新建云服务器
    # 111创建云服务器
    # 111-1自定义
    # (1)存储类型1（云硬盘scsi+云盘2.0）
    def create_VM1(self):
        data1 = self.data['TH-CP-VM-0001']['data1']    #依次点击添加云服务器-->创建云服务器-->进入基本信息页-->#进入CPU、内存信息页-->进入存储信息页
        data2 = self.data['TH-CP-VM-0001']['data2']
        data3 = self.data['TH-CP-VM-0001']['data3']
        self.steps(data1)
        self.steps(data2)
        self.steps(data3)
        data4 = self.data['TH-CP-VM-0001']['data4']   #设置磁盘信息
        self.steps(data4)
        data5 = self.data['TH-CP-VM-0001']['data5']
        data6 = self.data['TH-CP-VM-0001']['data6']
        self.steps(data5)
        self.steps(data6)
        data7 = self.data['TH-CP-VM-0001']['data7']
        return self.steps(data7)  #获取创建成功提示信息并返回

    #（2）存储类型2（云硬盘iscsi+高效云盘）
    def create_VM2(self):
        data1 = self.data['TH-CP-VM-0002']['data1']    #依次点击添加云服务器-->创建云服务器-->进入基本信息页-->#进入CPU、内存信息页-->进入存储信息页
        data2 = self.data['TH-CP-VM-0002']['data2']
        data3 = self.data['TH-CP-VM-0002']['data3']
        self.steps(data1)
        self.steps(data2)
        self.steps(data3)
        data4 = self.data['TH-CP-VM-0002']['data4']   #设置磁盘信息
        self.steps(data4)
        data5 = self.data['TH-CP-VM-0002']['data5']
        data6 = self.data['TH-CP-VM-0002']['data6']
        self.steps(data5)
        self.steps(data6)
        data7 = self.data['TH-CP-VM-0002']['data7']
        return self.steps(data7)  #获取创建成功提示信息并返回

    #(3)存储类型3（共享存储+云盘1.0）
    def create_VM3(self):
        data1 = self.data['TH-CP-VM-0003']['data1']  # 依次点击添加云服务器-->创建云服务器-->进入基本信息页-->#进入CPU、内存信息页-->进入存储信息页
        data2 = self.data['TH-CP-VM-0003']['data2']
        data3 = self.data['TH-CP-VM-0003']['data3']
        self.steps(data1)
        self.steps(data2)
        self.steps(data3)
        data4 = self.data['TH-CP-VM-0003']['data4']  # 设置磁盘信息
        self.steps(data4)
        data5 = self.data['TH-CP-VM-0003']['data5']
        data6 = self.data['TH-CP-VM-0003']['data6']
        self.steps(data5)
        self.steps(data6)
        data7 = self.data['TH-CP-VM-0003']['data7']
        return self.steps(data7)  # 获取创建成功提示信息并返回

    # 111-2创建云服务器/来源于模板
    # (1)创建模板0000
    def create_VMML(self):
        data = self.data['TH-CP-VMML-0004']
        return self.steps(data)

    # (2)创建云服务器/来源于模板
    def create_VM4(self):
        data1 = self.data['TH-CP-VM-0004']['data1']  # 依次点击添加云服务器-->创建云服务器-->进入基本信息页-->#进入CPU、内存信息页-->进入存储信息页
        data2 = self.data['TH-CP-VM-0004']['data2']
        data3 = self.data['TH-CP-VM-0004']['data3']
        self.steps(data1)
        self.steps(data2)
        self.steps(data3)
        data4 = self.data['TH-CP-VM-0004']['data4']  # 设置磁盘信息
        self.steps(data4)
        data5 = self.data['TH-CP-VM-0004']['data5']
        data6 = self.data['TH-CP-VM-0004']['data6']
        self.steps(data5)
        self.steps(data6)
        data7 = self.data['TH-CP-VM-0004']['data7']
        return self.steps(data7)  # 获取创建成功提示信息并返回

    # (3)创建云服务器/来源于规格
    def create_VM5(self):
        data1 = self.data['TH-CP-VM-0005']['data1']  # 依次点击添加云服务器-->创建云服务器-->进入基本信息页-->#进入CPU、内存信息页-->进入存储信息页
        data2 = self.data['TH-CP-VM-0005']['data2']
        data3 = self.data['TH-CP-VM-0005']['data3']
        self.steps(data1)
        self.steps(data2)
        self.steps(data3)
        data4 = self.data['TH-CP-VM-0005']['data4']  # 设置磁盘信息
        self.steps(data4)
        data5 = self.data['TH-CP-VM-0005']['data5']
        data6 = self.data['TH-CP-VM-0005']['data6']
        self.steps(data5)
        self.steps(data6)
        data7 = self.data['TH-CP-VM-0005']['data7']
        return self.steps(data7)  # 获取创建成功提示信息并返回

    # 1.2 编辑云服务器 0000
    # 121添加设备
    def edit_VM1(self):
        # data1 = self.data['TH-CP-EDIT_VM-0000']['data1']   #搜索框中搜索虚拟机0000并进入详情页面
        # self.steps(data1)
        # data2 = self.data['TH-CP-EDIT_VM-0000']['data2']   #鼠标移至虚拟机编辑按钮，出现虚拟机编辑列选项
        # self.move_mouse(data2['by'], data2['locator'])
        # data3 = self.data['TH-CP-EDIT_VM-0000']['data3']    #点击虚拟机的编辑/添加设备选项
        # self.move_and_click(data3['by'], data3['locator'])
        # data4 = self.data['TH-CP-EDIT_VM-0000']['data4']   #出现编辑设备弹窗，点击添加硬件按钮
        # self.steps(data4)
        # data5 = self.data['TH-CP-EDIT_VM-0000']['data5']   # 鼠标移至添加网卡选项并点击
        # self.move_and_click(data5['by'], data5['locator'])
        # data6 = self.data['TH-CP-EDIT_VM-0000']['data6']   #默认配置点击确认，获取添加网卡设备成功的提示信息
        # result = self.steps(data6)
        # data7 = self.data['TH-CP-EDIT_VM-0000']['data7']
        # self.steps(data7)
        # return result
        data = self.data['TH-CP-EDIT_VM-0000']
        return self.steps(data)

    #222测试设备
    def ttt_vm(self):
        data = self.data['TceCP-TEST_VM-0000']
        return self.steps(data)

    # 121删除设备
    def edit_VM2(self):
        # data1 = self.data['TH-CP-EDIT_VM-0001']['data1']  # 搜索框中搜索虚拟机0000并进入详情页面
        # self.steps(data1)
        # data2 = self.data['TH-CP-EDIT_VM-0001']['data2']  # 鼠标移至虚拟机编辑按钮，出现虚拟机编辑列选项
        # self.move_mouse(data2['by'], data2['locator'])
        # data3 = self.data['TH-CP-EDIT_VM-0001']['data3']  # 点击虚拟机的编辑/添加设备选项
        # self.move_and_click(data3['by'], data3['locator'])
        # data4 = self.data['TH-CP-EDIT_VM-0001']['data4']   #出现编辑设备弹窗，点击网卡按钮，点击第二张网卡的删除按钮，点击确认
        # self.steps(data4)
        # data5 = self.data['TH-CP-EDIT_VM-0001']['data5']  #捕获卸载成功的提示信息
        # result = self.steps(data5)
        # data6 = self.data['TH-CP-EDIT_VM-0001']['data6']  #关闭编辑窗口
        # self.steps(data6)
        # return result
        data = self.data['TH-CP-EDIT_VM-0001']
        return self.steps(data)

    # 1.3 删除云服务器
    # 131彻底删除
    def detel_VM1(self):
        # data1 = self.data['TH-CP-DETEL_VM-0001']['data1']  #搜索框中搜索虚拟机0001
        # self.steps(data1)
        # data2 = self.data['TH-CP-DETEL_VM-0001']['data2']    #鼠标置于虚拟机0001的编辑按钮，出现编辑列表
        # self.move_mouse(data2['by'], data2['locator'])
        # data3 = self.data['TH-CP-DETEL_VM-0001']['data3']    #鼠标移至编辑列表中的删除选项，并点击
        # self.move_and_click(data3['by'], data3['locator'])
        # data4 = self.data['TH-CP-DETEL_VM-0001']['data4']  # 彻底删除虚拟机0001
        # return self.steps(data4)   #捕获删除成功的提示信息
        data = self.data['TH-CP-DETEL_VM-0001']
        return self.steps(data)

    # 132彻底删除+同步删除卷   0002
    def detel_VM2(self):
        # data1 = self.data['TH-CP-DETEL_VM-0002']['data1']  #搜索框中搜索虚拟机0001
        # self.steps(data1)
        # data2 = self.data['TH-CP-DETEL_VM-0002']['data2']    #鼠标置于虚拟机0001的编辑按钮，出现编辑列表
        # self.move_mouse(data2['by'], data2['locator'])
        # data3 = self.data['TH-CP-DETEL_VM-0002']['data3']    #鼠标移至编辑列表中的删除选项，并点击
        # self.move_and_click(data3['by'], data3['locator'])
        # data4 = self.data['TH-CP-DETEL_VM-0002']['data4']  # 同步删除卷+彻底删除虚拟机0001
        # return self.steps(data4)    #捕获删除成功的提示信息
        data = self.data['TH-CP-DETEL_VM-0002']
        return self.steps(data)

    # 133非彻底删除
    def detel_VM3(self):
        # data1 = self.data['TH-CP-DETEL_VM-0003']['data1']  #搜索框中搜索虚拟机0001
        # self.steps(data1)
        # data2 = self.data['TH-CP-DETEL_VM-0003']['data2']    #鼠标置于虚拟机0001的编辑按钮，出现编辑列表
        # self.move_mouse(data2['by'], data2['locator'])
        # data3 = self.data['TH-CP-DETEL_VM-0003']['data3']    #鼠标移至编辑列表中的删除选项，并点击
        # self.move_and_click(data3['by'], data3['locator'])
        # data4 = self.data['TH-CP-DETEL_VM-0003']['data4']  # 非彻底删除虚拟机0001
        # return self.steps(data4)    #捕获删除成功的提示信息
        data = self.data['TH-CP-DETEL_VM-0003']
        return self.steps(data)

    # 1.1.2 迁入虚拟机(前置条件：存在已开启converter的虚拟机，且满足迁移条件)
    def immigrate_VM1(self):
        data = self.data['TH-CP-IMMIGRATE_VM-0001']
        return self.steps(data) #捕获创建成功的提示信息

    # 1.1.3 导入云服务器(前置条件：镜像仓库中存在ova/tva模板)
    # 1.1.3-1镜像仓库导入
    # (1)ova导入
    def export_VM1(self):
        data = self.data['TH-CP-EXPORT_VM-0001']
        return self.steps(data) #捕获创建成功的提示信息

    # (2)tva导入
    def export_VM2(self):
        data = self.data['TH-CP-EXPORT_VM-0002']
        return self.steps(data) #捕获创建成功的提示信息

    # 1.1.3-2存储介质导入
    # (1)ova导入
    def export_VM3(self):
        data = self.data['TH-CP-EXPORT_VM-0003']
        return self.steps(data)  #捕获创建成功的提示信息

    # (2)tva导入
    def export_VM4(self):
        data = self.data['TH-CP-EXPORT_VM-0004']
        return self.steps(data)  #捕获创建成功的提示信息

    # 1.4 云服务器的操作  0000
    # 141开机
    def operate_VM1(self):
        data = self.data['TH-CP-OPERATE_VM-0001']
        return self.steps(data)  #捕获开机成功的提示信息

    # 142重启
    def operate_VM2(self):
        data1 = self.data['TH-CP-OPERATE_VM-0002']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-OPERATE_VM-0002']['data2']
        return self.steps(data2)  #捕获重启成功的提示信息

    # 143挂起
    def operate_VM3(self):
        data = self.data['TH-CP-OPERATE_VM-0003']
        return self.steps(data)  #捕获挂起成功的提示信息

    # 144恢复
    def operate_VM4(self):
        data = self.data['TH-CP-OPERATE_VM-0004']
        return self.steps(data)  #捕获恢复成功的提示信息

    # 145休眠
    def operate_VM5(self):
        data = self.data['TH-CP-OPERATE_VM-0005']
        return self.steps(data)  #捕获休眠成功的提示信息

    # 146唤醒
    def operate_VM6(self):
        data = self.data['TH-CP-OPERATE_VM-0006']
        return self.steps(data)  #捕获唤醒成功的提示信息

    # 147导出PDF
    def operate_VM7(self):
        data = self.data['TH-CP-OPERATE_VM-0007']
        return self.steps(data)  #捕获导出PDF成功的提示信息

    # 148关机
    def operate_VM8(self):
        data1 = self.data['TH-CP-OPERATE_VM-0008']['data1']
        self.steps(data1)
        sleep(10)   #关机较慢，手动添加等待时间
        data2 = self.data['TH-CP-OPERATE_VM-0008']['data2']
        return self.steps(data2)  #捕获关机成功的提示信息

    # 149分配
    def operate_VM9(self):
        data = self.data['TH-CP-OPERATE_VM-0009']
        return self.steps(data)  #捕获分配成功的提示信息

    # 1410移动
    def operate_VM10(self):
        data = self.data['TH-CP-OPERATE_VM-0010']
        return self.steps(data)  #捕获移动成功的提示信息

    # 1411启动顺序
    def operate_VM11(self):
        data = self.data['TH-CP-OPERATE_VM-0011']
        return self.steps(data)  #捕获移动成功的提示信息

    #1412迁移
    #1412-1集群内迁移
    def migrate_VM1(self):
        data0 = self.data['TH-CP-MIGRATE_VM-0001']['data0']
        self.steps(data0)  #跳转到云服务器迁移弹窗
        data1 = self.data['TH-CP-MIGRATE_VM-0001']['data1']
        return self.steps(data1)  #捕获迁移成功的提示信息

    #1412-2跨集群迁移（存在目的集群）  ###还未写完
    def migrate_VM2(self):
        data0 = self.data['TH-CP-MIGRATE_VM-0002']['data0']
        self.steps(data0)  #跳转到云服务器迁移弹窗
        data1 = self.data['TH-CP-MIGRATE_VM-0002']['data1']
        return self.steps(data1)  #捕获迁移成功的提示信息

    #1412-3迁移到vsphere（存在目的集群） ###还未写完
    def migrate_VM3(self):
        data0 = self.data['TH-CP-MIGRATE_VM-0003']['data0']
        self.steps(data0)  #跳转到云服务器迁移弹窗
        data1 = self.data['TH-CP-MIGRATE_VM-0003']['data1']
        return self.steps(data1)  #捕获迁移成功的提示信息

    # 1413克隆
    # 1413-1全量克隆
    #（1）不基于快照
    def clone_VM1(self):
        data0 = self.data['TH-CP-CLONE_VM-0001']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0001']['data1']
        result1 = self.steps(data1)
        data2 = self.data['TH-CP-CLONE_VM-0001']['data2']
        result2 = self.steps(data2)
        return result1, result2  #捕获全量克隆成功的提示信息

    #（2）基于快照
    def clone_VM2(self):
        data0 = self.data['TH-CP-CLONE_VM-0002']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0002']['data1']
        self.steps(data1)  #添加快照
        sleep(2)
        data2 = self.data['TH-CP-CLONE_VM-0002']['data2']
        result1 = self.steps(data2)
        data3 = self.data['TH-CP-CLONE_VM-0002']['data3']
        result2 = self.steps(data3)
        return result1, result2  #捕获全量克隆成功的提示信息

    # 1413-2链接克隆
    def clone_VM3(self):
        data0 = self.data['TH-CP-CLONE_VM-0003']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0003']['data1']
        result1 = self.steps(data1)
        data2 = self.data['TH-CP-CLONE_VM-0003']['data2']
        result2 = self.steps(data2)
        return result1, result2  #捕获链接克隆成功的提示信息

    # 1413-3跨租户克隆  #报错：(//span[@class="el-switch__core"])[2]元素未找到
    def clone_VM4(self):
        data0 = self.data['TH-CP-CLONE_VM-0004']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0004']['data1']
        self.steps(data1)  #开启跨租户开关
        sleep(3)
        data2 = self.data['TH-CP-CLONE_VM-0004']['data2']
        self.steps(data2)
        return self.steps(data1)  #捕获跨租户克隆成功的提示信息

    #1414导入
    #1414-1镜像仓库导入
    def import_DISK1(self):
        data0 = self.data['TH-CP-IMPORT_VM-0001']['data0']
        self.steps(data0)  #关闭虚拟机
        sleep(30)
        data1 = self.data['TH-CP-IMPORT_VM-0001']['data1']
        self.steps(data1)  #跳转到云服务器磁盘导入弹窗
        data2 = self.data['TH-CP-IMPORT_VM-0001']['data2']
        result = self.steps(data2)
        data3 = self.data['TH-CP-IMPORT_VM-0001']['data2']
        self.steps(data3)
        return result      #捕获云服务器磁盘成功的提示信息

    #1414-2ISCSI导入
    def import_DISK2(self):
        data0 = self.data['TH-CP-IMPORT_VM-0002']['data0']
        self.steps(data0)  #跳转到云服务器ISCSI导入弹窗
        data1 = self.data['TH-CP-IMPORT_VM-0002']['data1']
        result = self.steps(data1)
        data2 = self.data['TH-CP-IMPORT_VM-0002']['data2']
        self.steps(data2)
        return result  # 捕获云服务器磁盘成功的提示信息

    #1415导出
    # 1415-1磁盘导出
    def exports_DISK1(self):
        data0 = self.data['TH-CP-EXPORTS_VM-0001']['data0']
        self.steps(data0)  #跳转到云服务器磁盘导出弹窗
        data1 = self.data['TH-CP-EXPORTS_VM-0001']['data1']
        return self.steps(data1)  #捕获云服务器磁盘导出成功的提示信息


    #1415-2云服务器导出
    #（1）导出到镜像仓库  0007
    def exports_VM1(self):
        data0 = self.data['TH-CP-EXPORTS_VM-0002']['data0']
        self.steps(data0)  #跳转到云服务器导出弹窗
        data1 = self.data['TH-CP-EXPORTS_VM-0002']['data1']
        result = self.steps(data1)
        sleep(2)
        data2 = self.data['TH-CP-EXPORTS_VM-0002']['data2']
        self.steps(data2)
        return result  # 捕获云服务器导出成功的提示信息


    #（2）导出到存储介质   0008
    def exports_VM2(self):
        data0 = self.data['TH-CP-EXPORTS_VM-0003']['data0']
        self.steps(data0)  #跳转到云服务器导出弹窗
        data1 = self.data['TH-CP-EXPORTS_VM-0003']['data1']
        result = self.steps(data1)
        sleep(2)
        data2 = self.data['TH-CP-EXPORTS_VM-0003']['data2']
        self.steps(data2)
        return result  # 捕获云服务器导出成功的提示信息

    #1.5云服务器基本信息页
    # 151 云服务器cpu操作
    # 151-1 关机状态下添加/减小cpu、修改基准类型
    def basic_ADDCPU1(self):
        data0 = self.data['TH-CP-BASIC_CPU-0001']['data0']
        self.steps(data0)  #跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_CPU-0001']['data1']
        self.steps(data1)  #关机状态下修改cpu
        sleep(15)
        data2 = self.data['TH-CP-BASIC_CPU-0001']['data2']
        result1 = self.steps(data2)  # 捕获云服务器插槽核数修改成功的提示信息
        data3 = self.data['TH-CP-BASIC_CPU-0001']['data3']
        result2 = self.steps(data3)  # 捕获云服务器插槽数修改成功的提示信息
        data4 = self.data['TH-CP-BASIC_CPU-0001']['data4']
        result3 = self.steps(data4)  # 捕获云服务器核数修改成功的提示信息
        data5 = self.data['TH-CP-BASIC_CPU-0001']['data5']
        result4 = self.steps(data5)  # 捕获云服务基准类型修改成功的提示信息
        data6 = self.data['TH-CP-BASIC_CPU-0001']['data6']
        self.steps(data6)  # 关闭虚拟机基本信息页
        return result1, result2, result3, result4

    # 151-2 开机状态下添加/减小cpu开机添加cpu
    def basic_ADDCPU2(self):
        data0 = self.data['TH-CP-BASIC_CPU-0002']['data0']
        self.steps(data0)  #跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_CPU-0002']['data1']
        return self.steps(data1)  #获取云服务器核数修改后的值

    # 151-3 开启/关闭预留cpu、cpu自动扩展
    def basic_EDITCPU3(self):
        data0 = self.data['TH-CP-BASIC_CPU-0003']['data0']
        self.steps(data0)  #跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_CPU-0003']['data1']
        result1 = self.steps(data1)  #开启预留cpu并获取提示信息
        sleep(3)
        self.keys_PageDown()  # 增加一个下翻页动作
        data2 = self.data['TH-CP-BASIC_CPU-0003']['data2']
        result2 = self.steps(data2)  #开启NUMA亲和性并获取提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_CPU-0003']['data3']
        result3 = self.steps(data3)  #开启cpu自动扩展并获取提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_CPU-0003']['data4']
        self.steps(data4)  #恢复原状
        return result1, result2, result3

    # 152云服务器内存操作
    # 152-1 关机状态下添加/减小内存、预留内存、内存自动扩展
    def basic_ADDMEM1(self):
        data0 = self.data['TH-CP-BASIC_MEM-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_MEM-0001']['data1']
        self.steps(data1)  # 关机状态下修改内存
        sleep(13)
        data2 = self.data['TH-CP-BASIC_MEM-0001']['data2']
        result1 = self.steps(data2)  # 捕获内存数修改成功的提示信息
        sleep(2)
        data3 = self.data['TH-CP-BASIC_MEM-0001']['data3']
        result2 = self.steps(data3)  # 捕获开启预留内存成功的提示信息
        sleep(2)
        data4 = self.data['TH-CP-BASIC_MEM-0001']['data4']
        result3 = self.steps(data4)  # 捕获开启内存自动扩展成功的提示信息
        sleep(2)
        data5 = self.data['TH-CP-BASIC_MEM-0001']['data5']
        result4 = self.steps(data5)  # 捕获预留内存扩展值修改成功的提示信息
        data6 = self.data['TH-CP-BASIC_MEM-0001']['data6']
        self.steps(data6)  # 关闭虚拟机基本信息页
        return result1, result2, result3, result4

    # 152-2开机状态下添加/减小内存
    def basic_ADDMEM2(self):
        data0 = self.data['TH-CP-BASIC_MEM-0002']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_MEM-0002']['data1']
        result1 = self.steps(data1)  # 捕获减小内存数修改失败的提示信息
        data2 = self.data['TH-CP-BASIC_MEM-0002']['data2']
        result2 = self.steps(data2)  # 捕获内存增加数修改成功的提示信息
        return result1, result2

    #153 高可用
    #153-1 关闭/开启
    def basic_EDITHUSE(self):
        data0 = self.data['TH-CP-BASIC_HUSE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_HUSE-0001']['data1']
        result1 = self.steps(data1)  # 捕获关闭高可用成功的提示信息
        data2 = self.data['TH-CP-BASIC_HUSE-0001']['data2']
        result2 = self.steps(data2)  # 捕获开启高可用成功的提示信息
        return result1, result2

    # 154 重要云服务器（开启高可用）
    # 154-1 高/低/中
    def basic_EDITIMPORTANT(self):
        data0 = self.data['TH-CP-BASIC_IMPORTANT-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_IMPORTANT-0001']['data1']
        result1 = self.steps(data1)  # 获取重要云服务器选择高成功的提示信息
        sleep(3)
        data2 = self.data['TH-CP-BASIC_IMPORTANT-0001']['data2']
        result2 = self.steps(data2)  # 获取重要云服务器选择低成功的提示信息
        return result1, result2

    # 155 内存巨页
    # 155-1 开启/关闭
    def basic_EDITMEMHUGE(self):
        data0 = self.data['TH-CP-BASIC_MEMHUGE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_MEMHUGE-0001']['data1']
        self.steps(data1)  # 关闭虚拟机
        sleep(13)
        data2 = self.data['TH-CP-BASIC_MEMHUGE-0001']['data2']
        result1 = self.steps(data2)  # 获取开启内存巨页成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_MEMHUGE-0001']['data3']
        result2 = self.steps(data3)  # 获取关闭内存巨页成功的提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_MEMHUGE-0001']['data4']
        self.steps(data4)  # 开启虚拟机
        return result1, result2

    # 156 启动
    # 156-1 开启/关闭
    def basic_EDITSTART(self):
        data0 = self.data['TH-CP-BASIC_START-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_START-0001']['data1']
        self.steps(data1)  # 关闭虚拟机
        sleep(13)
        data2 = self.data['TH-CP-BASIC_START-0001']['data2']
        result1 = self.steps(data2)  # 获取开启uefi启动成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_START-0001']['data3']
        result2 = self.steps(data3)  # 获取开启bios启动成功的提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_START-0001']['data4']
        self.steps(data4)  # 开启虚拟机
        return result1, result2

    # 157 嵌套虚拟化
    # 157-1 开启/关闭
    def basic_EDITNEST(self):
        data0 = self.data['TH-CP-BASIC_NEST-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_NEST-0001']['data1']
        self.steps(data1)  # 关闭虚拟机
        sleep(13)
        data2 = self.data['TH-CP-BASIC_NEST-0001']['data2']
        result1 = self.steps(data2)  # 捕获关闭嵌套虚拟化成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_NEST-0001']['data3']
        result2 = self.steps(data3)  # 捕获开启嵌套虚拟化成功的提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_NEST-0001']['data4']
        self.steps(data4)  # 恢复默认
        return result1, result2

    #158 数据本地化
    # 158-1 开启/关闭
    def basic_EDITDATALOCAL(self):
        data0 = self.data['TH-CP-BASIC_DATALOCAL-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_DATALOCAL-0001']['data1']
        result1 = self.steps(data1)  # 获取开启数据本地化成功的提示信息
        sleep(3)
        data2 = self.data['TH-CP-BASIC_DATALOCAL-0001']['data2']
        result2 = self.steps(data2)  # 获取关闭数据本地化成功的提示信息
        return result1, result2

    #159 内存安全
    # 159-1 开启/关闭
    def basic_EDITMEMSAFE(self):
        data0 = self.data['TH-CP-BASIC_MEMSAFE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_MEMSAFE-0001']['data1']
        result1 = self.steps(data1)  # 获取开启内存安全成功的提示信息
        sleep(3)
        data2 = self.data['TH-CP-BASIC_MEMSAFE-0001']['data2']
        result2 = self.steps(data2)  # 获取关闭内存安全成功的提示信息
        return result1, result2

    #1510 启用双活
    # 1510-1 开启/关闭
    def basic_EDITDLIVE(self):
        data0 = self.data['TH-CP-BASIC_DLIVE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_DLIVE-0001']['data1']
        self.steps(data1)  # 关闭虚拟机
        sleep(13)
        data2 = self.data['TH-CP-BASIC_DLIVE-0001']['data2']
        result1 = self.steps(data2)  # 获取开启启用双活成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_DLIVE-0001']['data3']
        result2 = self.steps(data3)  # 获取关闭启用双活成功的提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_DLIVE-0001']['data4']
        self.steps(data4)  # 恢复默认
        return result1, result2

    #1512 绑定主资源池（前置条件：启用双活）
    # 1512-1 开启/关闭
    def basic_EDITBIND(self):
        data0 = self.data['TH-CP-BASIC_BIND-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_BIND-0001']['data1']
        self.steps(data1)  # 开启启用双活
        sleep(3)
        data2 = self.data['TH-CP-BASIC_BIND-0001']['data2']
        result1 = self.steps(data2)  # 获取开启绑定主资源池成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_BIND-0001']['data3']
        result2 = self.steps(data3)  # 获取关闭绑定主资源池成功的提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_BIND-0001']['data4']
        self.steps(data4)  # 恢复默认
        return result1, result2

    #1513 VNC
    # 1513-1 关机状态下开启
    def basic_EDITVNC1(self):
        data0 = self.data['TH-CP-BASIC_VNC-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_VNC-0001']['data1']
        self.steps(data1)  # 关闭虚拟机
        sleep(13)
        data2 = self.data['TH-CP-BASIC_VNC-0001']['data2']
        result1 = self.steps(data2)  # 获取开启VNC成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_VNC-0001']['data3']
        self.steps(data3)  # 恢复默认
        return result1

    # 1513-2 开机状态下检查VNC配置信息
    def basic_EDITVNC2(self):
        data0 = self.data['TH-CP-BASIC_VNC-0002']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_VNC-0002']['data1']
        self.steps(data1)
        self.keys_PageDown() # 滑动滚动条，防止元素被遮挡
        sleep(3)
        data2 = self.data['TH-CP-BASIC_VNC-0002']['data2']
        result1 = self.steps(data2)  # 检查开启VNC后的展示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_VNC-0002']['data3']
        self.steps(data3)  # 恢复默认
        return result1

    #1514 Spice
    # 1514-1 开机状态下检查Spice配置信息
    def basic_EDITSPICE1(self):
        data0 = self.data['TH-CP-BASIC_SPICE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_SPICE-0001']['data1']
        self.steps(data1)
        self.keys_PageDown()  # 滑动滚动条，防止元素被遮挡
        sleep(3)
        data2 = self.data['TH-CP-BASIC_SPICE-0001']['data2']
        result1 = self.steps(data2)  # 检查开机状态开启Spice的展示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_SPICE-0001']['data3']
        self.steps(data3)  # 恢复默认
        return result1

    # 1514-2 关机状态下检查Spice配置信息
    def basic_EDITSPICE2(self):
        data0 = self.data['TH-CP-BASIC_SPICE-0002']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_SPICE-0002']['data1']
        self.steps(data1)  #关闭虚拟机
        sleep(15)
        data2 = self.data['TH-CP-BASIC_SPICE-0002']['data2']
        self.steps(data2)
        self.keys_PageDown()  # 滑动滚动条，防止元素被遮挡
        sleep(3)
        data3 = self.data['TH-CP-BASIC_SPICE-0002']['data3']
        result1 = self.steps(data3)  # 检查关机状态开启Spice的展示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_SPICE-0002']['data4']
        self.steps(data4)  # 恢复默认
        return result1

    #1515异常检测
    #1515-1 开启/关闭
    def basic_EDITUNUSUAL(self):
        data0 = self.data['TH-CP-BASIC_UNUSUAL-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_UNUSUAL-0001']['data1']
        self.steps(data1)
        self.keys_PageDown()  # 滑动滚动条，防止元素被遮挡
        sleep(3)
        data2 = self.data['TH-CP-BASIC_UNUSUAL-0001']['data2']
        result1 = self.steps(data2)  #获取关闭异常检测成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_UNUSUAL-0001']['data3']
        result2 = self.steps(data3)  #获取开启异常检测成功的提示信息
        sleep(3)
        data4 = self.data['TH-CP-BASIC_UNUSUAL-0001']['data4']
        self.steps(data4)  # 恢复默认
        return result1, result2

    # 1516自动配置
    # 1516-1选择主机
    def basic_EDITDISPOSE1(self):
        data0 = self.data['TH-CP-BASIC_DISPOSE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_DISPOSE-0001']['data1']
        self.steps(data1)
        self.keys_PageDown()  # 滑动滚动条，防止元素被遮挡
        sleep(3)
        data2 = self.data['TH-CP-BASIC_DISPOSE-0001']['data2']
        result1 = self.steps(data2)  #获取选择主机启动操作成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_DISPOSE-0001']['data3']
        self.steps(data3)  # 恢复默认
        return result1

    # 1516-2选择标签
    def basic_EDITDISPOSE2(self):
        data0 = self.data['TH-CP-BASIC_DISPOSE-0002']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_DISPOSE-0002']['data1']
        self.steps(data1)
        self.keys_PageDown()  # 滑动滚动条，防止元素被遮挡
        sleep(3)
        data2 = self.data['TH-CP-BASIC_DISPOSE-0002']['data2']
        result1 = self.steps(data2)  #获取选择标签启动操作成功的提示信息
        sleep(3)
        data3 = self.data['TH-CP-BASIC_DISPOSE-0002']['data3']
        self.steps(data3)  # 恢复默认
        return result1

    ########

    # 1.6 云服务器快照信息页面
    # 161普通快照
    # 161-1添加快照
    def snap_ADD1(self):
        data0 = self.data['TH-CP-COM_SNAP_ADD-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机快照信息页
        data1 = self.data['TH-CP-COM_SNAP_ADD-0001']['data1']
        result1 = self.steps(data1)  # 捕获创建普通快照成功的提示信息
        return result1

    # 161-2回滚快照(需关机)
    def snap_ROLLBACK1(self):
        data0 = self.data['TH-CP-COM_SNAP_ROLLBACK-0001']['data0']
        self.steps(data0)  # 跳转到基本信息页
        data1 = self.data['TH-CP-COM_SNAP_ROLLBACK-0001']['data1']
        self.steps(data1)  #关闭虚拟机，进入到虚拟机快照信息页
        sleep(13)
        data2 = self.data['TH-CP-COM_SNAP_ROLLBACK-0001']['data2']
        self.steps(data2)  # 创建普通快照002
        sleep(5)
        data3 = self.data['TH-CP-COM_SNAP_ROLLBACK-0001']['data3']
        result1 = self.steps(data3)  # 回滚至普通快照001，捕获回滚普通快照成功的提示信息
        data4 = self.data['TH-CP-COM_SNAP_ROLLBACK-0001']['data4']
        self.steps(data4)  # 恢复原状
        return result1

    #161-3删除快照
    def snap_DEL1(self):
        data0 = self.data['TH-CP-COM_SNAP_DEL-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机快照信息页
        data1 = self.data['TH-CP-COM_SNAP_DEL-0001']['data1']
        result1 = self.steps(data1)  #捕获删除普通快照2成功的提示信息；关闭虚拟机快照信息页
        sleep(1.5)
        data2 = self.data['TH-CP-COM_SNAP_DEL-0001']['data2']
        result2 = self.steps(data2)  # 捕获删除普通快照1成功的提示信息；关闭虚拟机快照信息页
        return result1, result2

    # 162内存快照（租户绑定的资源池已开启内存快照空间，虚拟机处于开机状态）
    # 162-1添加内存快照
    def snap_ADD2(self):
        data0 = self.data['TH-CP-MEM_SNAP_ADD-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机快照信息页
        data1 = self.data['TH-CP-MEM_SNAP_ADD-0001']['data1']
        result1 = self.steps(data1)  # 捕获创建内存快照成功的提示信息
        return result1

    # 161-2回滚快照(需关机)
    def snap_ROLLBACK2(self):
        data0 = self.data['TH-CP-MEM_SNAP_ROLLBACK-0001']['data0']
        self.steps(data0)  # 跳转到基本信息页
        sleep(1)
        data1 = self.data['TH-CP-MEM_SNAP_ROLLBACK-0001']['data1']
        self.steps(data1)  # 创建内存快照002
        sleep(2)
        data2 = self.data['TH-CP-MEM_SNAP_ROLLBACK-0001']['data2']
        self.steps(data2)  #关闭虚拟机，进入到虚拟机快照信息页
        sleep(13)
        data3 = self.data['TH-CP-MEM_SNAP_ROLLBACK-0001']['data3']
        result1 = self.steps(data3)  # 回滚至内存快照001，捕获回滚内存快照成功的提示信息
        data4 = self.data['TH-CP-MEM_SNAP_ROLLBACK-0001']['data4']
        self.steps(data4)  # 恢复原状
        return result1

    #162-3删除快照
    def snap_DEL2(self):
        data0 = self.data['TH-CP-MEM_SNAP_DEL-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机快照信息页
        sleep(3)
        data1 = self.data['TH-CP-MEM_SNAP_DEL-0001']['data1']
        result1 = self.steps(data1)  #捕获删除内存快照2成功的提示信息；关闭虚拟机快照信息页
        sleep(3)
        data2 = self.data['TH-CP-MEM_SNAP_DEL-0001']['data2']
        result2 = self.steps(data2)  # 捕获删除内存快照1成功的提示信息；关闭虚拟机快照信息页
        return result1, result2

    #1.7云服务器监控信息页面
    # 171 cgt安装
    def basic_CGT_ADD1(self):
        data0 = self.data['TH-CP-BASIC_CGT-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机基本信息页
        data1 = self.data['TH-CP-BASIC_CGT-0001']['data1']
        result1 = self.steps(data1)  #捕获云服务器设置Guest-Agent-Tools成功的提示信息
        sleep(1.5)
        data2 = self.data['TH-CP-BASIC_CGT-0001']['data2']
        result2 = self.steps(data2)  # 关闭虚拟机基本信息页
        return result1, result2

    # 172 cgt监控
    def basic_CGT_SEARCH1(self):
        data0 = self.data['TH-CP-MONITOR_CGT-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机监控信息页
        data1 = self.data['TH-CP-MONITOR_CGT-0001']['data1']
        return self.steps(data1)  #获取云服务器监控信息页面信息

    #1.8云服务器备份信息页面（已存在备份点：ptbf-001）
    # 181添加备份
    # 181-1单卷添加备份
    def backup_SINGEL_ADD1(self):
        data0 = self.data['TH-CP-BACKUP_SINGLE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机备份信息页
        sleep(6)
        data1 = self.data['TH-CP-BACKUP_SINGLE-0001']['data1']
        return self.steps(data1)  #捕获创建备份成功的提示信息

    # 181-2多卷添加备份
    def backup_MULTI_ADD1(self):
        data0 = self.data['TH-CP-BACKUP_MULTI-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机备份信息页
        data1 = self.data['TH-CP-BACKUP_MULTI-0001']['data1']
        self.steps(data1)  #添加磁盘
        sleep(6)
        data2 = self.data['TH-CP-BACKUP_MULTI-0001']['data2']
        return self.steps(data2)  #捕获创建备份成功的提示信息

    # 182备份恢复
    # 182-1单卷备份恢复
    def backup_RECOVERY_SINGEL1(self):
        data0 = self.data['TH-CP-REBACKUP_SINGLE-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机备份信息页
        data1 = self.data['TH-CP-REBACKUP_SINGLE-0001']['data1']
        return self.steps(data1)  #捕获创建备份恢复成功的提示信息

    # 182-2多卷备份恢复
    def backup_RECOVERY_MULTI1(self):
        data0 = self.data['TH-CP-REBACKUP_MULTI-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机备份信息页
        data1 = self.data['TH-CP-REBACKUP_MULTI-0001']['data1']
        return self.steps(data1)  #捕获创建备份恢复成功的提示信息

    # 183删除备份
    def backup_DEL1(self):
        data0 = self.data['TH-CP-BACKUP_DEL-0001']['data0']
        self.steps(data0)  # 跳转到虚拟机备份信息页
        data1 = self.data['TH-CP-BACKUP_DEL-0001']['data1']
        return self.steps(data1)  #捕获删除备份成功的提示信息

# 2.模板页面
class MouldPage(BasePage):
    filepath = readFilepath.MouldDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    #2.1模板转换 --pass

    #2.2基于模板创建虚拟机
    def mould_VM1(self):
        data = self.data['TH-CP-MOULD_VM-0001']
        return self.steps(data)  #捕获模板创建虚拟机成功的提示信息

    #2.3模板恢复
    def mould_VM2(self):
        data = self.data['TH-CP-MOULD_VM-0002']
        return self.steps(data)  #捕获虚拟机模板转化成功的提示信息



# 3.规格页面
class SpecsPage(BasePage):
    filepath = readFilepath.SpecsDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    # 3.1添加规格
    def creat_specs1(self):
        data = self.data['TH-CP-SPECS-0001']
        return self.steps(data)  #捕获创建规格成功的提示信息

    # 3.2删除规格
    def delete_specs2(self):
        data = self.data['TH-CP-SPECS-0002']
        return self.steps(data)  #捕获创建规格成功的提示信息

# 4.备份页面
class BackupPage(BasePage):
    filepath = readFilepath.BackupDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    # 4.1远端导入备份
    def remote_backup1(self):
        data = self.data['TH-CP-BACKUP-0001']
        return self.steps(data)  #捕获远端导入备份成功的提示信息

    # 4.2远端备份恢复
    def remote_backup2(self):
        data = self.data['TH-CP-BACKUP-0002']
        return self.steps(data)  #捕获远端导入备份恢复成功的提示信息


# 5.策略页面
class StrategyPage(BasePage):
    filepath = readFilepath.StrategyDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    # 5.1 开关机策略
    # （1）创建开关机策略
    def creat_strategy11(self):
        data = self.data['TH-CP-STRATEGY-0001']
        return self.steps(data)  #捕获创建开关机策略成功的提示信息

    # （2）开启/关闭开关机策略
    def updown_strategy11(self):
        data0 = self.data['TH-CP-STRATEGY-0002']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0002']['data1']
        result1 = self.steps(data1)  #捕获停止开关机策略成功的提示信息
        sleep(2)
        data2 = self.data['TH-CP-STRATEGY-0002']['data2']
        result2 = self.steps(data2)  # 捕获开启开关机策略成功的提示信息
        return result1, result2

    # （3）编辑开关机策略
    def edit_strategy11(self):
        data0 = self.data['TH-CP-STRATEGY-0003']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0003']['data1']
        return self.steps(data1)  #捕获编辑开关机策略成功的提示信息

    # （4）删除开关机策略
    def del_strategy11(self):
        data0 = self.data['TH-CP-STRATEGY-0004']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0004']['data1']
        return self.steps(data1)  #捕获删除开关机策略成功的提示信息


    # 5.2 创建快照策略
    # （1）创建快照策略
    def creat_strategy21(self):
        data = self.data['TH-CP-STRATEGY-0005']
        return self.steps(data)  #捕获创建快照策略成功的提示信息

    # （2）开启/关闭快照策略
    def updown_strategy21(self):
        data0 = self.data['TH-CP-STRATEGY-0006']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0006']['data1']
        result1 = self.steps(data1)  # 捕获停止快照策略成功的提示信息
        sleep(2)
        data2 = self.data['TH-CP-STRATEGY-0006']['data2']
        result2 = self.steps(data2)  # 捕获开启快照策略成功的提示信息
        return result1, result2

    # （3）编辑快照策略
    def edit_strategy21(self):
        data0 = self.data['TH-CP-STRATEGY-0007']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0007']['data1']
        return self.steps(data1)  # 捕获编辑快照策略成功的提示信息

    # （4）删除快照策略
    def del_strategy21(self):
        data0 = self.data['TH-CP-STRATEGY-0008']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0008']['data1']
        return self.steps(data1)  # 捕获删除快照策略成功的提示信息

    # 5.3 创建备份策略
    # （1）创建备份策略
    def creat_strategy31(self):
        data = self.data['TH-CP-STRATEGY-0009']
        return self.steps(data)  #捕获创建备份策略成功的提示信息

    # （2）开启/关闭备份策略
    def updown_strategy31(self):
        data0 = self.data['TH-CP-STRATEGY-0010']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0010']['data1']
        result1 = self.steps(data1)  # 捕获停止备份策略成功的提示信息
        sleep(2)
        data2 = self.data['TH-CP-STRATEGY-0010']['data2']
        result2 = self.steps(data2)  # 捕获开启备份策略成功的提示信息
        return result1, result2

    # （3）编辑备份策略
    def edit_strategy31(self):
        data0 = self.data['TH-CP-STRATEGY-0011']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0011']['data1']
        return self.steps(data1)  # 捕获编辑备份策略成功的提示信息

    # （4）删除备份策略
    def del_strategy31(self):
        data0 = self.data['TH-CP-STRATEGY-0012']['data0']
        self.steps(data0)
        data1 = self.data['TH-CP-STRATEGY-0012']['data1']
        return self.steps(data1)  # 捕获删除备份策略成功的提示信息