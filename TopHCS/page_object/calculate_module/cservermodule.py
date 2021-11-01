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
        sleep(20)   #关机较慢，手动添加等待时间
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
        result1 = self.steps(data1)
        data2 = self.data['TH-CP-CLONE_VM-0002']['data2']
        result2 = self.steps(data2)
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

    # 1413-3跨租户克隆  #报错
    def clone_VM4(self):
        data0 = self.data['TH-CP-CLONE_VM-0004']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0004']['data1']
        self.steps(data1)
        return self.steps(data1)  #捕获跨租户克隆成功的提示信息



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
    filepath = readFilepath.ServerDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    # 4.1远端导入备份
    def remote_backup1(self):
        data0 = self.data['TH-CP-BACKUP-0001']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0004']['data1']
        self.steps(data1)
        return self.steps(data1)  #捕获跨租户克隆成功的提示信息

    # 4.2远端备份恢复
    def remote_backup2(self):
        data0 = self.data['TH-CP-CLONE_VM-0004']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0004']['data1']
        self.steps(data1)
        return self.steps(data1)  #捕获跨租户克隆成功的提示信息

# 5.策略页面
class StrategyPage(BasePage):
    filepath = readFilepath.ServerDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析

    # 1413-3跨租户克隆  #报错
    def clone_VMwww(self):
        data0 = self.data['TH-CP-CLONE_VM-0004']['data0']
        self.steps(data0)  #跳转到云服务器克隆弹窗
        data1 = self.data['TH-CP-CLONE_VM-0004']['data1']
        self.steps(data1)
        return self.steps(data1)  #捕获跨租户克隆成功的提示信息