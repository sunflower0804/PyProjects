from time import sleep

import pytest
from selenium.webdriver.common.by import By
from TopHC.base.basepage import BasePage
from TopHC.others.yamlexcelload import loadyaml
from TopHC.others.filepath import readFilepath

#1.云服务器模块
# 1.1云服务器页面
class ServicePage(BasePage):
    filepath = readFilepath.ServerDataPath
    data = loadyaml(filepath)      #获取测试驱动数据文件，并解析
    # 1.1.1 云服务器页面/集群信息导航栏信息校验
    # (1)集群目录信息校验
    def search_clustersUI1(self):
        data1 = self.data['TH-CP-CLUSTER-0001'] #验证集群名称的驱动数据
        return self.steps(data1) #获取集群名称信息并返回


    #（2）集群云服务器信息校验
    def search_clustersUI2(self):
        data2 = self.data['TH-CP-CLUSTER-0002'] #验证集群下的某个云服务器名称的驱动数据
        return self.steps(data2) #获取集群下的某个云服务器名称信息并返回

    #(3)集群目录结构信息校验
    def search_clustersUI3(self):
        data3 = self.data['TH-CP-CLUSTER-0003']['data01']+self.data['TH-CP-CLUSTER-0003']['data02']+self.data['TH-CP-CLUSTER-0003']['data03']   #验证集群目录下某个组名称的驱动数据
        return self.steps(data3) #获取集群目录下某个组名称信息并返回

    #(4)集群目录组下服务器信息校验
    def search_clustersUI4(self):
        data4 = self.data['TH-CP-CLUSTER-0004']['data01']+self.data['TH-CP-CLUSTER-0004']['data02']+self.data['TH-CP-CLUSTER-0004']['data03']  #验证集群目录某个组下云服务器名称的驱动数据
        return self.steps(data4) #获取集群目录某个组下云服务器名称信息并返回

    # 1.1.2.云服务器页面/集群信息导航栏功能校验
    # (5)集群目录新增组功能验证/正常场景
    def search_clustersUI5(self):
        data51 = self.data['TH-CP-CLUSTER-0005']['data01']  #获取
        self.steps(data51)
        data52 = self.data['TH-CP-CLUSTER-0005']['data02']
        self.move_mouse(data52['by'], data52['locator'])
        sleep(2)
        data53 = self.data['TH-CP-CLUSTER-0005']['data03']
        # self.move_and_click(data53['by'], data53['locator'])
        self.move_mouse(data53['by'], data53['locator'])
        self.click(data53['by'], data53['locator'])

    # (6)集群目录新增组功能验证/异常场景
    def search_clustersUI6(self):
        pass

    # (7)集群目录组名称重命名功能验证/正常场景
    def search_clustersUI7(self):
        pass

    #（8）集群目录组名称重命名功能验证/异常场景
    def search_clustersUI8(self):
        pass

    #（9）集群目录组添加云服务器入口验证
    def search_clustersUI9(self):
        pass

    #（10）集群目录组移动验证
    def search_clustersUI10(self):
        pass

    #（11）集群目录组删除验证
    def search_clustersUI11(self):
        pass

    # 1.2.1.云服务器页面/菜单栏功能校验/搜索
    #（1）虚拟机搜索/功能入口参数校验
    def search_VM1(self):
        data12 = self.data['TH-CP-VM-0001']
        return self.text(data12['by'], data12['locator'], attr = data12['attr'])

    # (2) 搜索功能验证/正常场景
    def search_VM2(self):
        data13 = self.data['TH-CP-VM-0002']
        return self.steps(data13)

    # (3) 搜索功能验证/正常场景
    def search_VM3(self):
        data14 = self.data['TH-CP-VM-0003']
        return self.steps(data14)

    # 1.2.2.云服务器页面/菜单栏功能校验/虚拟机批量操作



    # 1.2.3.云服务器页面/菜单栏功能校验/添加云服务器
    #1.2.3.1 创建云服务器
    # <1 自定义
    # <1-1 基本信息页参数校验
    def creat_VM_page1(self):
        data0 = self.data['TH-CP-VM-000']['data01']  #获取添加云服务器-->创建云服务器元素
        self.steps(data0)      #依次点击添加云服务器-->创建云服务器，进入基本信息页

    # <1-1-1云服务器输入框验证
    # (1)云服务器输入框弱提示验证
    def creat_VM_page1111(self):
        data = self.data['TH-CP-VM-0004']  # 云服务器提示框，获取弱提示属性
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)云服务器输入框输入为空验证
    def creat_VM_page1112(self):
        data = self.data['TH-CP-VM-0005']  # 获取云服务器输入框输入为空后的提示信息元素
        service = self.steps(data)
        return service

    # (3)云服务器输入框输入特殊字符验证
    def creat_VM_page1113(self):
        data = self.data['TH-CP-VM-0006']  # 获取云服务器提示框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)云服务器输入框输入大于32位字符验证
    def creat_VM_page1114(self):
        data = self.data['TH-CP-VM-0007']  # 获取云服务器提示框输入为大于32位字符后的提示信息元素
        service = self.steps(data)
        return service

    # <1-1-2操作系统下拉框验证
    def creat_VM_page1121(self):
        data = self.data['TH-CP-VM-0008']
        service = self.steps(data)  #点击操作系统下拉框;移动鼠标，选择下拉框中的others;移动鼠标，选择下拉框中的FreeBSD，并点击
        return service

    # <1-1-3创建个数输入框验证
    # (1)创建个数输入框默认值验证
    def creat_VM_page1131(self):
        data = self.data['TH-CP-VM-0009']  # 获取创建个数输入框默认值
        service = self.input_text(data['by'], data['locator'])  #获取输入框默认值
        return service

    # (2)创建个数输入框输入为空验证
    def creat_VM_page1132(self):
        data1 = self.data['TH-CP-VM-0010']['data1']   #获取创建个数输入框输入为空后下方的提示信息元素
        service0 = self.steps(data1)
        data2 = self.data['TH-CP-VM-0010']['data2']     #获取创建个数输入框输入为空后的弱提示信息元素
        service1 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0010']['data3']
        self.steps(data3)
        return service0, service1

    # (3)创建个数输入框输入特殊字符验证
    def creat_VM_page1133(self):
        data = self.data['TH-CP-VM-0011']  # 获取创建个数输入框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)创建个数输入框输入大于100数字验证
    def creat_VM_page1134(self):
        data = self.data['TH-CP-VM-0012']     #获取创建个数输入框输入为大于100的数字后的提示信息元素
        service = self.steps(data)
        return service

    # (5)创建个数输入框输入小于1位字符验证
    def creat_VM_page1135(self):
        data = self.data['TH-CP-VM-0013']     # 获取创建个数输入框输入为小于1的数字后的提示信息元素
        service = self.steps(data)
        return service

    # <1-2 CPU、内存信息页参数校验
    def creat_VM_page2(self):
        data1 = self.data['TH-CP-VM-0014']['data1']   #获取添加云服务器-->创建云服务器元素
        self.steps(data1)  # 依次点击添加云服务器-->创建云服务器，进入基本信息页
        data2 = self.data['TH-CP-VM-0014']['data2']  #获取进入到CPU、内存信息页的元素
        self.steps(data2)  # 进入CPU、内存信息页

    # <1-2-1处理器输入框验证
    # (1)创建个数输入框默认值验证
    def creat_VM_page1211(self):
        data = self.data['TH-CP-VM-0015']    #获取处理器输入框默认值
        service = self.input_text(data['by'], data['locator'])  #获取输入框默认值
        return service

    # (2)创建个数输入框输入为空验证
    def creat_VM_page1212(self):
        data1 = self.data['TH-CP-VM-0016']['data1']     #获取处理器输入框输入为空后下方的提示信息元素
        service1 = self.steps(data1)
        data2 = self.data['TH-CP-VM-0016']['data2']     #获取处理器输入框输入为空后的弱提示信息元素
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (3)创建个数输入框输入特殊字符验证
    def creat_VM_page1213(self):
        data = self.data['TH-CP-VM-0017']     #获取处理器输入框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)创建个数输入框输入大于2数字验证
    def creat_VM_page1214(self):
        data = self.data['TH-CP-VM-0018']     #获取处理器输入框输入为大于2的数字后的提示信息元素
        service = self.steps(data)
        return service

    # (5)创建个数输入框输入小于1位字符验证
    def creat_VM_page1215(self):
        data = self.data['TH-CP-VM-0019']     #获取处理器输入框输入为小于1的数字后的提示信息元素
        service = self.steps(data)
        return service

    # <1-2-2处理器输入框验证
    # (1)处理器输入框默认值验证
    def creat_VM_page1221(self):
        data = self.data['TH-CP-VM-0020']  # 获取处理器输入框默认值
        service = self.input_text(data['by'], data['locator'])  # 获取输入框默认值
        return service

    # (2)处理器输入框输入为空验证
    def creat_VM_page1222(self):
        data11 = self.data['TH-CP-VM-0021']['data1']  # 获取处理器输入框输入为空后下方的提示信息元素
        service1 = self.steps(data11)
        data = self.data['TH-CP-VM-0021']['data2']  # 获取处理器输入框输入为空后的弱提示信息元素
        service2 = self.text(data['by'], data['locator'], attr=data['attr'])
        return service1, service2

    # (3)处理器输入框输入特殊字符验证
    def creat_VM_page1223(self):
        data = self.data['TH-CP-VM-0022']  # 获取处理器输入框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)处理器输入框输入大于2数字验证
    def creat_VM_page1224(self):
        data = self.data['TH-CP-VM-0023']  # 获取处理器输入框输入为大于2的数字后的提示信息元素
        service = self.steps(data)
        return service

    # (5)处理器输入框输入小于1位字符验证
    def creat_VM_page1225(self):
        data = self.data['TH-CP-VM-0024']  # 获取处理器输入框输入为小于1的数字后的提示信息元素
        service = self.steps(data)
        return service

    # <1-2-3插槽核数输入框验证
    # (1)插槽核数输入框默认值验证
    def creat_VM_page1231(self):
        data = self.data['TH-CP-VM-0025']  # 获取插槽核数输入框默认值
        service = self.input_text(data['by'], data['locator'])  # 获取输入框默认值
        return service

    # (2)插槽核数输入框输入为空验证
    def creat_VM_page1232(self):
        data1 = self.data['TH-CP-VM-0026']['data1']  # 获取插槽核数输入框输入为空后下方的提示信息元素
        service1 = self.steps(data1)
        data2 = self.data['TH-CP-VM-0026']['data2']  # 获取插槽核数输入框输入为空后的弱提示信息元素
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (3)插槽核数输入框输入特殊字符验证
    def creat_VM_page1233(self):
        data = self.data['TH-CP-VM-0027']  # 获取插槽核数输入框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)插槽核数输入框输入大于24数字验证
    def creat_VM_page1234(self):
        data = self.data['TH-CP-VM-0028']  # 获取插槽核数输入框输入为大于24的数字后的提示信息元素
        service = self.steps(data)
        return service

    # (5)插槽核数输入框输入小于1位字符验证
    def creat_VM_page1235(self):
        data = self.data['TH-CP-VM-0029']  # 获取插槽核数输入框输入为小于1的数字后的提示信息元素
        service = self.steps(data)
        return service

    # <1-2-4内存大小输入框验证
    # (1)内存大小输入框默认值验证
    def creat_VM_page1241(self):
        data = self.data['TH-CP-VM-0030']  # 获取内存大小输入框默认值
        service = self.input_text(data['by'], data['locator'])  # 获取输入框默认值
        return service

    # (2)内存大小输入框输入为空验证
    def creat_VM_page1242(self):
        data1 = self.data['TH-CP-VM-0031']['data1']  # 获取内存大小输入框输入为空后下方的提示信息元素
        service1 = self.steps(data1)
        data2 = self.data['TH-CP-VM-0031']['data2']  # 获取内存大小输入框输入为空后的弱提示信息元素
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (3)内存大小输入框输入特殊字符验证
    def creat_VM_page1243(self):
        data = self.data['TH-CP-VM-0032']  # 获取内存大小输入框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)内存大小输入框输入大于256验证
    def creat_VM_page1244(self):
        data = self.data['TH-CP-VM-0033']  # 获取内存大小输入框输入为大于256后的提示信息元素
        service = self.steps(data)
        return service

    # (5)内存大小输入框输入小于0.5验证
    def creat_VM_page1245(self):
        data = self.data['TH-CP-VM-0034']  # 获取内存大小输入框输入为小于1的数字后的提示信息元素
        service = self.steps(data)
        return service

    # <1-2-5基准类型下拉框验证
    def creat_VM_page1251(self):
        data = self.data['TH-CP-VM-0035']
        service = self.steps(data)  # 点击基准类型下拉框;移动鼠标，选择一级下拉框中的arm;移动鼠标，选择二级下拉框中的Phytium，并点击；选择选择一级下拉框中的Tengyun-S2500，并点击
        return service

    def creat_VM_page3(self):
        data1 = self.data['TH-CP-VM-0036']['data1']   #获取添加云服务器-->创建云服务器元素
        self.steps(data1)  # 依次点击添加云服务器-->创建云服务器，进入基本信息页
        data2 = self.data['TH-CP-VM-0036']['data2']  #获取进入到CPU、内存信息页的元素
        self.steps(data2)  # 进入CPU、内存信息页
        data3 = self.data['TH-CP-VM-0036']['data3'] #获取进入到存储信息页的元素
        self.steps(data3)  # 进入存储信息页

    # <1-3-1磁盘大小输入框验证
    # (1)磁盘大小输入框默认为空时弱提示验证
    def creat_VM_page1311(self):
        data = self.data['TH-CP-VM-0037']  # 获取磁盘大小输入框默认值
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)磁盘大小输入框输入为空验证
    def creat_VM_page1312(self):
        data = self.data['TH-CP-VM-0038']  # 获取磁盘大小输入框输入为空后下方的提示信息元素
        service = self.steps(data)
        return service

    # (3)磁盘大小输入框输入特殊字符验证
    def creat_VM_page1313(self):
        data = self.data['TH-CP-VM-0039']  # 获取磁盘大小输入框输入为特殊字符后的提示信息元素
        service = self.steps(data)
        return service

    # (4)磁盘大小输入框输入大于256T验证：1111111
    def creat_VM_page1314(self):
        data = self.data['TH-CP-VM-0040']  # 获取磁盘大小输入框输入为大于256T后的提示信息元素
        service = self.steps(data)
        return service

    # (5)磁盘大小输入框输入小于0.5验证
    def creat_VM_page1315(self):
        data = self.data['TH-CP-VM-0041']  # 获取磁盘大小输入框输入为小于0.5的数字后的提示信息元素
        service = self.steps(data)
        return service

    # <1-3-2驱动类型选择项验证
    # (1)默认选择scsi验证(tabindex="0")
    def creat_VM_page1321(self):
        data = self.data['TH-CP-VM-0042']  # 获取驱动类型默认选择项元素属性tabindex="0"
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ide验证(tabindex="0")
    def creat_VM_page1322(self):
        data1 = self.data['TH-CP-VM1-0042']['data1']  #选择ide验证(tabindex="0")
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0042']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0042']['data3']  # 恢复默认选项scsi
        self.steps(data3)
        return service

    # <1-3-3存储池下拉框验证
    def creat_VM_page1331(self):
        data = self.data['TH-CP-VM-0043']
        service = self.steps(data)
        return service

    # <1-3-4卷名称输入框验证
    # (1)卷名称输入框默认值验证
    def creat_VM_page1341(self):
        data14 = self.data['TH-CP-VM-0044']['data1']
        service09 = self.input_text(data14['by'], data14['locator'])  #定位到卷名称输入框，获取默认值：test001-volume1
        data15 = self.data['TH-CP-VM-0044']['data2']  #清除默认值
        self.steps(data15)
        # (2)卷名称输入框输入为空验证
        data16 = self.data['TH-CP-VM-0045']['data1']  #输入框下方提示信息获取：“卷名称不能为空”
        service10 = self.steps(data16)
        data17 = self.data['TH-CP-VM-0045']['data2']  #输入框弱提示信息获取：“请输入卷名称”
        service11 = self.text(data17['by'], data17['locator'], attr=data17['attr'])
        # (3)卷名称输入框输入特殊字符验证
        data18 = self.data['TH-CP-VM-0046']  #输入框下方提示信息获取：“卷名称不能含有特殊字符”
        service12 = self.steps(data18)
        # (4)卷名称输入框输入大于32位字符验证
        data19 = self.data['TH-CP-VM-0047']  #输入框下方提示信息获取：“卷名称由1~32位字符组成”
        service13 = self.steps(data19)

        # <1-3-5副本数下拉框验证
        data20 = self.data['TH-CP-VM-0048']['data1']  #副本数下拉框默认值验证
        service14 = self.input_text(data20['by'], data20['locator'])
        data21 = self.data['TH-CP-VM-0048']['data2']
        self.steps(data21)
        data22 = self.data['TH-CP-VM-0048']['data3']
        service15 = self.input_text(data22['by'], data22['locator'])

        # <1-3-6云盘类型下拉框验证
        data23 = self.data['TH-CP-VM-0049']['data1']  #云盘类型下拉框默认值验证
        service16 = self.input_text(data23['by'], data23['locator'])
        data24 = self.data['TH-CP-VM-0049']['data2']
        self.steps(data24)
        data25 = self.data['TH-CP-VM-0049']['data3']  #云盘类型选择值验证：高效云盘
        service17 = self.input_text(data25['by'], data25['locator'])

        # <1-3-7存储介质下拉框验证
        data26 = self.data['TH-CP-VM-0050']['data1']  #存储介质下拉框默认值验证
        service18 = self.input_text(data26['by'], data26['locator'])
        data27 = self.data['TH-CP-VM-0050']['data2']
        self.steps(data27)
        data28 = self.data['TH-CP-VM-0050']['data3']  #存储介质选择值验证：固态硬盘
        service19 = self.input_text(data28['by'], data28['locator'])

        # <1-3-8链路冗余下拉框验证
        data29 = self.data['TH-CP-VM-0051']['data1']  #存储介质下拉框默认值验证
        service20 = self.input_text(data29['by'], data29['locator'])
        data30 = self.data['TH-CP-VM-0051']['data2']
        self.steps(data30)
        data31 = self.data['TH-CP-VM-0051']['data3']  #存储介质选择值验证：固态硬盘
        service21 = self.input_text(data31['by'], data31['locator'])
        data32 = self.data['TH-CP-VM-0051']['data4']
        self.steps(data32)
        return service01, service02, service03, service04, service05, \
               service06, service07, \
               service08, \
               service10, service11, service12, service13, \
               service14, service15,\
               service16, service17,\
               service18, service19, \
               service20, service21,


    def creat_VM_page4(self):
        data0 = self.data['TH-CP-VM-0052']['data01']   #获取添加云服务器-->创建云服务器元素
        self.steps(data0)  # 依次点击添加云服务器-->创建云服务器，进入基本信息页
        data01 = self.data['TH-CP-VM-0052']['data02']  #获取进入到CPU、内存信息页的元素
        self.steps(data01)  # 进入CPU、内存信息页
        data02 = self.data['TH-CP-VM-0052']['data03'] #获取进入到存储信息页的元素
        self.steps(data02)  # 进入存储信息页
        data03 = self.data['TH-CP-VM-0052']['data04'] #获取进入到网卡信息页的元素
        self.steps(data03)  # 进入网卡信息页

        # # <1-4-1新增网卡功能验证
        # # (1)新增网卡验证
        # data04 = self.data['TH-CP-VM-0053']  #新增一个网卡成功后删除
        # service01 = self.steps(data04)

        # <1-4-2网卡信息折叠功能验证
        # (1)网卡信息折叠功能验证
        data05 = self.data['TH-CP-VM-0054']  #点击网卡折叠按钮
        service02 = self.steps(data05)

        # # <1-4-3网卡下拉框验证
        # data06 = self.data['TH-CP-VM-0055'] #网卡下拉框验证
        # service03 = self.steps(data06)

        # # <1-4-4适配器下拉框验证
        # data07 = self.data['TH-CP-VM-0056']['data1']  #存储介质下拉框默认值验证
        # service04 = self.input_text(data07['by'], data07['locator'])
        # data08 = self.data['TH-CP-VM-0056']['data2']
        # self.steps(data08)
        # data09 = self.data['TH-CP-VM-0056']['data3']  #存储介质选择值验证：固态硬盘
        # service05 = self.input_text(data09['by'], data09['locator'])

        ## <1-4-5多队列设置开关验证
        # data10 = self.data['TH-CP-VM-0057']['data1']
        # service06 = self.check_element_exist(data10['by'], data10['locator'])  #默认关闭状态验证(关闭状态下队列数信息不存在,即返回Flase)
        # data11 = self.data['TH-CP-VM-0057']['data2']     #开启多队列
        # self.steps(data11)
        # data12 = self.data['TH-CP-VM-0057']['data3']
        # service07 = self.check_element_exist(data12['by'], data12['locator'])   #开启状态验证(开启状态下队列数信息存在,即返回True)

        # # <1-4-6队列数输入框验证
        # # (1)队列数输入框默认值验证
        # data15 = self.data['TH-CP-VM-0058']['data1']
        # service09 = self.input_text(data15['by'], data15['locator'])  # 定位到队列数输入框，获取默认值：1
        # data16 = self.data['TH-CP-VM-0058']['data2']  # 清除默认值
        # self.steps(data16)
        # # (2)队列数输入框输入为空验证
        # data17 = self.data['TH-CP-VM-0059']['data1']  # 输入框下方提示信息获取：“队列数不能为空”
        # service10 = self.steps(data17)
        # data18 = self.data['TH-CP-VM-0059']['data2']  # 输入框弱提示信息获取：“请输入队列数”
        # service11 = self.text(data18['by'], data18['locator'], attr=data18['attr'])
        # # (3)队列数输入框输入特殊字符验证
        # data19 = self.data['TH-CP-VM-0060']  # 输入框下方提示信息获取：“队列数为正整数”
        # service12 = self.steps(data19)
        # # (4)队列数输入框输入大于2验证
        # data20 = self.data['TH-CP-VM-0061']  # 输入框下方提示信息获取：“队列数不能超过当前cpu数（当前cpu数为2）”
        # service13 = self.steps(data20)
        # # (5)队列数输入框输入小于1验证
        # data21 = self.data['TH-CP-VM-0062']  # 输入框下方提示信息获取：“队列数为正整数”
        # service14 = self.steps(data21)

        # <1-4-7虚拟交换机下拉框验证（前置条件：存在创建好的虚拟交换机compute、manage；compute下存在端口“计算”、“计算98”）
        # # <1-4-3虚拟交换机下拉框验证
        # data22 = self.data['TH-CP-VM-0063']['data1']  #虚拟交换机下拉框默认值验证
        # service15 = self.input_text(data22['by'], data22['locator'])
        # data23 = self.data['TH-CP-VM-0063']['data2']  #虚拟交换机端口下拉框默认值验证
        # service16 = self.input_text(data23['by'], data23['locator'])
        # data24 = self.data['TH-CP-VM-0063']['data3']
        # self.steps(data24)

        # # <1-4-8速率输入框验证
        # (1)速率输入框默认值验证
        data25 = self.data['TH-CP-VM-0064']['data1']
        service17 = self.input_text(data25['by'], data25['locator'])  # 定位到速率输入框，获取默认值：0
        data26 = self.data['TH-CP-VM-0064']['data2']  # 清除默认值
        self.steps(data26)
        # (2)速率输入框输入为空验证
        data27 = self.data['TH-CP-VM-0065']['data1']
        service18 = self.steps(data27)
        data28 = self.data['TH-CP-VM-0065']['data2']  # 输入框弱提示信息获取：“请输入队列数”
        service19 = self.text(data28['by'], data28['locator'], attr=data28['attr'])
        # (3)速率输入框输入特殊字符验证
        data29 = self.data['TH-CP-VM-0060']  # 输入框下方提示信息获取：“队列数为正整数”
        service20 = self.steps(data29)
        # (4)速率输入框输入大于2验证
        data30 = self.data['TH-CP-VM-0061']  # 输入框下方提示信息获取：“队列数不能超过当前cpu数（当前cpu数为2）”
        service21 = self.steps(data30)
        # (5)速率输入框输入小于0验证
        data31 = self.data['TH-CP-VM-0062']  # 输入框下方提示信息获取：“队列数为正整数”
        service22 = self.steps(data31)


        # return service01, \
        #        service02, \
        #        service03, \
        #        service04, service05, \
        #        service06, service07, \
        #        service09, service10, service11, service12, service13, service14, \
        #        service15,service16, \
        return












    #1.2.3.2 迁入云服务器

    #1.2.3.3 导入云服务器


    #（14）添加云服务器

    #(1)集群目录新增组功能验证
    def add_group(self):
        return self.steps(r'/TopHC/data/page_data/calculate_module_data/cserver_module/serverdata.yaml')

    #(6)集群目录组名称重命名功能验证
    def update_group(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_updategroup.yaml')










#模板页面
class MouldPage(BasePage):
    def search_clustersUI21(self):
        return self.steps(r'D:\WorkTools\PyProjects\TopHC\data\page_data\calculate_module_data\cserver_module\cal_cserver_cluster21.yaml')


#规格页面
class SpecsPage(BasePage):
    pass


#备份页面
class BackupPage(BasePage):
    pass

#策略页面
class StrategyPage(BasePage):
    pass


