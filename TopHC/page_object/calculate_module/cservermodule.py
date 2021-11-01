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
        data1 = self.data['TH-CP-VM-0038']['data1']   # 获取磁盘大小输入框输入为空后下方的提示信息元素
        self.steps(data1)
        sleep(7)
        data2 = self.data['TH-CP-VM-0038']['data2']   # 获取磁盘大小输入框输入为空后下方的提示信息元素
        service = self.steps(data2)
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
        data2 = self.data['TH-CP-VM1-0042']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM1-0042']['data3']  # 恢复默认选项scsi
        self.steps(data3)
        return service

    # <1-3-3存储池下拉框验证
    def creat_VM_page1331(self):
        data1 = self.data['TH-CP-VM-0043']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0043']['data2']
        service = self.input_text(data2['by'], data2['locator'])
        return service

    # <1-3-4卷名称输入框验证
    # (1)卷名称输入框默认值验证
    def creat_VM_page1341(self):
        data = self.data['TH-CP-VM-0044']
        service = self.input_text(data['by'], data['locator'])  #定位到卷名称输入框，获取默认值：test001-volume1
        return service

    # (2)卷名称输入框输入为空验证
    def creat_VM_page1342(self):
        data1 = self.data['TH-CP-VM-0045']['data1']  #输入框下方提示信息获取：“卷名称不能为空”
        service1 = self.steps(data1)
        data2 = self.data['TH-CP-VM-0045']['data2']  #输入框弱提示信息获取：“请输入卷名称”
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (3)卷名称输入框输入特殊字符验证
    def creat_VM_page1343(self):
        data = self.data['TH-CP-VM-0046']  #输入框下方提示信息获取：“卷名称不能含有特殊字符”
        service = self.steps(data)
        return service

    # (4)卷名称输入框输入大于32位字符验证
    def creat_VM_page1344(self):
        data = self.data['TH-CP-VM-0047']  #输入框下方提示信息获取：“卷名称由1~32位字符组成”
        service = self.steps(data)
        return service

    # <1-3-5副本数下拉框验证
    # (1)副本数默认值验证
    def creat_VM_page1351(self):
        data = self.data['TH-CP-VM-0048']  #副本数下拉框默认值验证
        service = self.input_text(data['by'], data['locator'])
        return service

    # (2)副本数选择值验证
    def creat_VM_page1352(self):
        data1 = self.data['TH-CP-VM1-0048']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0048']['data2']
        service = self.input_text(data2['by'], data2['locator'])
        return service

    # <1-3-6云盘类型下拉框验证
    # (1)云盘类型默认值验证：普通云盘1.0
    def creat_VM_page1361(self):
        data = self.data['TH-CP-VM-0049']  #云盘类型下拉框默认值验证
        service = self.input_text(data['by'], data['locator'])
        return service

    # (2)云盘类型选择值验证：高效云盘
    def creat_VM_page1362(self):
        data1 = self.data['TH-CP-VM1-0049']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0049']['data2']  #云盘类型选择值验证：高效云盘
        service = self.input_text(data2['by'], data2['locator'])
        return service

    # <1-3-7存储介质下拉框验证
    # (1)存储介质默认值验证：机械硬盘
    def creat_VM_page1371(self):
        data = self.data['TH-CP-VM-0050']  #存储介质下拉框默认值验证
        service = self.input_text(data['by'], data['locator'])
        return service

    # (2)存储介质选择值验证：固态硬盘
    def creat_VM_page1372(self):
        data1 = self.data['TH-CP-VM1-0050']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0050']['data2']  #存储介质选择值验证：固态硬盘
        service = self.input_text(data2['by'], data2['locator'])
        return service

    # <1-3-8链路冗余下拉框验证
    # (1)链路冗余默认值验证：1
    def creat_VM_page1381(self):
        data = self.data['TH-CP-VM-0051']  #存储介质下拉框默认值验证
        service = self.input_text(data['by'], data['locator'])
        return service

    # (2)链路冗余选择值验证：3
    def creat_VM_page1382(self):
        data1 = self.data['TH-CP-VM1-0051']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0051']['data2']  #存储介质选择值验证：固态硬盘
        service = self.input_text(data2['by'], data2['locator'])
        data3 = self.data['TH-CP-VM1-0051']['data3']
        self.steps(data3)
        return service

    #1-4 网卡信息页
    def creat_VM_page4(self):
        data1 = self.data['TH-CP-VM-0052']['data1']   #获取添加云服务器-->创建云服务器元素
        self.steps(data1)  # 依次点击添加云服务器-->创建云服务器，进入基本信息页
        data2 = self.data['TH-CP-VM-0052']['data2']  #获取进入到CPU、内存信息页的元素
        self.steps(data2)  # 进入CPU、内存信息页
        data3 = self.data['TH-CP-VM-0052']['data3'] #获取进入到存储信息页的元素
        self.steps(data3)  # 进入存储信息页
        data4 = self.data['TH-CP-VM-0052']['data4'] #获取进入到网卡信息页的元素
        self.steps(data4)  # 进入网卡信息页

    # <1-4-1新增网卡功能验证
    # (1)新增网卡验证
    def creat_VM_page1411(self):
        data = self.data['TH-CP-VM-0053']  #新增一个网卡成功后删除
        service = self.steps(data)
        return service

    # <1-4-2网卡信息折叠功能验证
    # (1)网卡信息折叠功能验证
    def creat_VM_page1421(self):
        data1 = self.data['TH-CP-VM-0054']["data1"]  #点击网卡折叠按钮
        self.steps(data1)
        sleep(2)
        data2 = self.data['TH-CP-VM-0054']["data2"]
        service1 = self.check_element_exist(data2['by'], data2['locator'])
        data3 = self.data['TH-CP-VM-0054']["data3"]
        self.steps(data3)       #再次点击网卡折叠按钮
        data4 = self.data['TH-CP-VM-0054']["data4"]
        service2 = self.check_element_exist(data4['by'], data4['locator'])
        return service1, service2

    # <1-4-3网卡下拉框验证
    # (1)网卡类型默认值验证：本地网络(存在虚拟交换机选项)
    def creat_VM_page1431(self):
        data = self.data['TH-CP-VM-0055'] #网卡下拉框验证
        service = self.steps(data)
        return service

    # (2)网卡类型选择值验证：VPC网络(存在VPC交换机选项)
    def creat_VM_page1432(self):
        data = self.data['TH-CP-VM1-0055']  # 网卡下拉框验证
        service = self.steps(data)
        return service

    # <1-4-4适配器下拉框验证
    # (1)适配器类型默认值验证：virtio
    def creat_VM_page1441(self):
        data = self.data['TH-CP-VM-0056']
        service = self.input_text(data['by'], data['locator'])
        return service

    # (2)适配器类型选择值验证：rtl8139
    def creat_VM_page1442(self):
        data1 = self.data['TH-CP-VM1-0056']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0056']['data2']  #存储介质选择值验证：固态硬盘
        service = self.input_text(data2['by'], data2['locator'])
        return service

    # <1-4-5多队列设置开关验证
    # (1)默认关闭状态验证(关闭状态下队列数输入框不存在)
    def creat_VM_page1451(self):
        data = self.data['TH-CP-VM-0057']
        service = self.check_element_exist(data['by'], data['locator'])  #默认关闭状态验证(关闭状态下队列数信息不存在,即返回Flase)
        return service

    # (2)开启状态验证(开启状态下队列数输入框存在)
    def creat_VM_page1452(self):
        data1 = self.data['TH-CP-VM1-0057']['data1']     #开启多队列
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0057']['data2']
        service = self.check_element_exist(data2['by'], data2['locator'])   #开启状态验证(开启状态下队列数信息存在,即返回True)
        data3 = self.data['TH-CP-VM1-0057']['data3']  # 关闭多队列
        self.steps(data3)
        return service

    # <1-4-6队列数输入框验证
    # (1)队列数输入框默认值验证
    def creat_VM_page1461(self):
        data1 = self.data['TH-CP-VM-0058']['data1']  #开启多队列
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0058']['data2']
        service = self.input_text(data2['by'], data2['locator'])  # 定位到队列数输入框，获取默认值：1
        return service

    # (2)队列数输入框输入为空验证
    def creat_VM_page1462(self):
        data1 = self.data['TH-CP-VM-0059']['data1']  # 输入框下方提示信息获取：“队列数不能为空”
        service1 = self.steps(data1)
        data2 = self.data['TH-CP-VM-0059']['data2']  # 输入框弱提示信息获取：“请输入队列数”
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (3)队列数输入框输入特殊字符验证
    def creat_VM_page1463(self):
        data = self.data['TH-CP-VM-0060']  # 输入框下方提示信息获取：“队列数为正整数”
        service = self.steps(data)
        return service

    # (4)队列数输入框输入大于2验证
    def creat_VM_page1464(self):
        data = self.data['TH-CP-VM-0061']  # 输入框下方提示信息获取：“队列数不能超过当前cpu数（当前cpu数为2）”
        service = self.steps(data)
        return service

    # (5)队列数输入框输入小于1验证
    def creat_VM_page1465(self):
        data = self.data['TH-CP-VM-0062']  # 输入框下方提示信息获取：“队列数为正整数”
        service = self.steps(data)
        return service

    # <1-4-7虚拟交换机下拉框验证（前置条件：存在创建好的虚拟交换机compute、manage；compute下存在端口“计算”、“计算98”）
    # <1-4-7虚拟交换机下拉框验证
    # (1)虚拟交换机默认值验证
    def creat_VM_page1471(self):
        data1 = self.data['TH-CP-VM-0063']['data1']  #虚拟交换机下拉框默认值验证
        service1 = self.input_text(data1['by'], data1['locator'])
        data2 = self.data['TH-CP-VM-0063']['data2']  #虚拟交换机端口下拉框默认值验证
        service2 = self.input_text(data2['by'], data2['locator'])
        return service1, service2

    # (2)虚拟交换机下拉框选择值验证
    def creat_VM_page1472(self):
        data1 = self.data['TH-CP-VM1-0063']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM1-0063']['data2']
        service = self.input_text(data2['by'], data2['locator'])
        return service

    # QOS设置
    # 发送
    # <1-4-8发送速率输入框验证
    #(1)发送速率输入框默认值验证
    def creat_VM_page1481(self):
        data = self.data['TH-CP-VM-0064']
        service = self.input_text(data['by'], data['locator'])  # 定位到速率输入框，获取默认值：0
        return service

    # (2)发送速率输入框输入为空验证
    def creat_VM_page1482(self):
        data1 = self.data['TH-CP-VM-0065']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0065']['data2']   #输入框弱提示信息获取：“请输入速率”
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    # (3)发送速率输入框输入特殊字符验证
    def creat_VM_page1483(self):
        data = self.data['TH-CP-VM-0066']   #输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    #(4)发送速率输入框输入大于4194303验证
    def creat_VM_page1484(self):
        data = self.data['TH-CP-VM-0067']  #输入框下方提示信息获取：“输入上限4194303”
        service = self.steps(data)
        return service

    #(5)发送速率输入框输入小于0验证
    def creat_VM_page1485(self):
        data = self.data['TH-CP-VM-0068']  #输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # <1-4-9发送峰值输入框验证
    # (1)发送峰值输入框默认值验证
    def creat_VM_page1491(self):
        data = self.data['TH-CP-VM-0069']
        service = self.input_text(data['by'], data['locator'])  # 定位到速率输入框，获取默认值：0
        return service

    #(2)发送峰值输入框输入为空验证
    def creat_VM_page1492(self):
        data1 = self.data['TH-CP-VM-0070']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0070']['data2']  #输入框弱提示信息获取：“请输入速率”
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    #(3)发送峰值输入框输入特殊字符验证
    def creat_VM_page1493(self):
        data = self.data['TH-CP-VM-0071']  #输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    #(4)发送峰值输入框输入大于4194303验证
    def creat_VM_page1494(self):
        data = self.data['TH-CP-VM-0072']  #输入框下方提示信息获取：“输入上限4194303”
        service = self.steps(data)
        return service

    #(5)发送峰值输入框输入小于0验证
    def creat_VM_page1495(self):
        data = self.data['TH-CP-VM-0073']  #输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # <1-4-10发送突发值输入框验证
    # (1)发送突发值输入框默认值验证
    def creat_VM_page14101(self):
        data = self.data['TH-CP-VM-0074']
        service = self.input_text(data['by'], data['locator'])  # 定位到速率输入框，获取默认值：0
        return service

    # (2)发送突发值输入框输入为空验证
    def creat_VM_page14102(self):
        data1 = self.data['TH-CP-VM-0075']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0075']['data2']  #输入框弱提示信息获取：“请输入突发值”
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    # (3)发送突发值输入框输入特殊字符验证
    def creat_VM_page14103(self):
        data = self.data['TH-CP-VM-0076']  #输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # (4)发送突发值输入框输入大于4194303验证
    def creat_VM_page14104(self):
        data = self.data['TH-CP-VM-0077']  # #输入框下方提示信息获取：“输入上限4194303”
        service = self.steps(data)
        return service

    # (5)发送突发值输入框输入小于0验证
    def creat_VM_page14105(self):
        data = self.data['TH-CP-VM-0078']  #输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # QOS设置
    # 接收
    # 切换到接收栏
    def creat_VM_page14110(self):
        data = self.data['TH-CP-VM-0079']
        self.steps(data)  #点击接收按钮

    # <1-4-11接收速率输入框验证
    # (1)接收速率输入框默认值验证
    def creat_VM_page14111(self):
        data = self.data['TH-CP-VM-0080']
        service = self.input_text(data['by'], data['locator'])  # 定位到速率输入框，获取默认值：0
        return service

    # (2)接收速率输入框输入为空验证
    def creat_VM_page14112(self):
        data1 = self.data['TH-CP-VM-0081']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0081']['data2']  # 输入框弱提示信息获取：“请输入速率”
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    # (3)接收速率输入框输入特殊字符验证
    def creat_VM_page14113(self):
        data = self.data['TH-CP-VM-0082']  # 输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # (4)接收速率输入框输入大于4194303验证
    def creat_VM_page14114(self):
        data = self.data['TH-CP-VM-0083']  # 输入框下方提示信息获取：“输入上限4194303”
        service = self.steps(data)
        return service

    # (5)接收速率输入框输入小于0验证
    def creat_VM_page14115(self):
        data = self.data['TH-CP-VM-0084']  # 输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # <1-4-12接收峰值输入框验证
    # (1)接收峰值输入框默认值验证
    def creat_VM_page14121(self):
        data = self.data['TH-CP-VM-0085']
        service = self.input_text(data['by'], data['locator'])  # 定位到速率输入框，获取默认值：0
        return service

    # (2)接收峰值输入框输入为空验证
    def creat_VM_page14122(self):
        data1 = self.data['TH-CP-VM-0086']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0086']['data2']  # 输入框弱提示信息获取：“请输入速率”
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    # (3)接收峰值输入框输入特殊字符验证
    def creat_VM_page14123(self):
        data = self.data['TH-CP-VM-0087']  # 输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # (4)接收峰值输入框输入大于4194303验证
    def creat_VM_page14124(self):
        data = self.data['TH-CP-VM-0088']  # 输入框下方提示信息获取：“输入上限4194303”
        service = self.steps(data)
        return service

    # (5)接收峰值输入框输入小于0验证
    def creat_VM_page14125(self):
        data = self.data['TH-CP-VM-0089']  # 输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # <1-4-13接收突发值输入框验证
    # (1)接收突发值输入框默认值验证
    def creat_VM_page14131(self):
        data = self.data['TH-CP-VM-0090']
        service = self.input_text(data['by'], data['locator'])  # 定位到速率输入框，获取默认值：0
        return service

    # (2)接收突发值输入框输入为空验证
    def creat_VM_page14132(self):
        data1 = self.data['TH-CP-VM-0091']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0091']['data2']  # 输入框弱提示信息获取：“请输入突发值”
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    # (3)接收突发值输入框输入特殊字符验证
    def creat_VM_page14133(self):
        data = self.data['TH-CP-VM-0092']  # 输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    # (4)接收突发值输入框输入大于4194303验证
    def creat_VM_page14134(self):
        data = self.data['TH-CP-VM-0093']  # #输入框下方提示信息获取：“输入上限4194303”
        service = self.steps(data)
        return service

    # (5)接收突发值输入框输入小于0验证
    def creat_VM_page14135(self):
        data = self.data['TH-CP-VM-0094']  # 输入框下方提示信息获取：“请输入0或者正整数”
        service = self.steps(data)
        return service

    #1-5 高级配置页
    def creat_VM_page5(self):
        data1 = self.data['TH-CP-VM-0095']['data1']   #获取添加云服务器-->创建云服务器元素
        self.steps(data1)  # 依次点击添加云服务器-->创建云服务器，进入基本信息页
        data2 = self.data['TH-CP-VM-0095']['data2']  #获取进入到CPU、内存信息页的元素
        self.steps(data2)  # 进入CPU、内存信息页
        data3 = self.data['TH-CP-VM-0095']['data3'] #获取进入到存储信息页的元素
        self.steps(data3)  # 进入存储信息页
        data4 = self.data['TH-CP-VM-0095']['data4'] #获取进入到网卡信息页的元素
        self.steps(data4)  # 进入网卡信息页
        data5 = self.data['TH-CP-VM-0095']['data5'] #获取进入到高级配置页的元素
        self.steps(data5)  # 进入高级配置页

    # <1-5-1光驱下拉框验证
    # (1)光驱下拉框默认为空验证
    def creat_VM_page1511(self):
        data1 = self.data['TH-CP-VM-0096']['data1']
        service1 = self.text(data1['by'], data1['locator'], attr=data1['attr'])   # 仓库下拉框弱提示信息获取：“请选择仓库地址”
        data2 = self.data['TH-CP-VM-0096']['data2']  # 光驱下拉框弱提示信息获取：“请选择光驱地址”
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (2)光驱下拉框选择值验证
    def creat_VM_page1512(self):
        data1 = self.data['TH-CP-VM-0097']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0097']['data2']
        service1 = self.input_text(data2['by'], data2['locator'])    # 仓库下拉框选择项信息获取： ”lakers“
        data3 = self.data['TH-CP-VM-0097']['data3']
        service2 = self.input_text(data3['by'], data3['locator'])    # 光驱下拉框选择项信息获取： ""
        return service1, service2

    # <1-5-2软驱下拉框验证
    # (1)软驱下拉框默认为空验证
    def creat_VM_page1521(self):
        data1 = self.data['TH-CP-VM-0098']['data1']
        service1 = self.text(data1['by'], data1['locator'], attr=data1['attr'])  # 仓库下拉框弱提示信息获取：“请选择仓库地址”
        data2 = self.data['TH-CP-VM-0098']['data2']  # 软驱下拉框弱提示信息获取：“请选择软驱地址”
        service2 = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service1, service2

    # (2)软驱下拉框选择值验证
    def creat_VM_page1522(self):
        data1 = self.data['TH-CP-VM-0099']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0099']['data2']
        service1 = self.input_text(data2['by'], data2['locator'])   # 仓库下拉框选择项信息获取： ”lakers“
        data3 = self.data['TH-CP-VM-0099']['data3']
        service2 = self.input_text(data3['by'], data3['locator'])   # 软驱下拉框选择项信息获取： ""
        return service1, service2

    # <1-5-3显示选择项验证
    # (1)默认选择VGA验证(tabindex="0")
    def creat_VM_page1531(self):
        data = self.data['TH-CP-VM-0100']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择vGPU验证(tabindex="0")
    def creat_VM_page1532(self):
        data1 = self.data['TH-CP-VM-0101']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0101']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0101']['data3']
        self.steps(data3)
        return service

    # <1-5-4高可用选择项验证
    # (1)默认选择ON验证(tabindex="0")
    def creat_VM_page1541(self):
        data = self.data['TH-CP-VM-0102']
        service = self.steps(data)
        return service

    # (2)选择OFF验证(tabindex="0")
    def creat_VM_page1542(self):
        data1 = self.data['TH-CP-VM-0103']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0103']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0103']['data3']
        self.steps(data3)
        return service

    # <1-5-5重要云服务器选择项验证
    # (1)默认选择中验证(tabindex="0")
    def creat_VM_page1551(self):
        data = self.data['TH-CP-VM-0104']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择高验证(tabindex="0")
    def creat_VM_page1552(self):
        data1 = self.data['TH-CP-VM-0105']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0105']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0105']['data3']
        self.steps(data3)
        return service

    # <1-5-6巨页内存选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page1561(self):
        data = self.data['TH-CP-VM-0106']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page1562(self):
        data1 = self.data['TH-CP-VM-0107']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0107']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0107']['data3']
        self.steps(data3)
        return service

    # <1-5-7启动选择项验证
    # (1)默认选择BIOS验证(tabindex="0")
    def creat_VM_page1571(self):
        data = self.data['TH-CP-VM-0108']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择UEFI验证(tabindex="0")
    def creat_VM_page1572(self):
        data1 = self.data['TH-CP-VM-0109']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0109']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0109']['data3']
        self.steps(data3)
        return service

    # <1-5-8异常检测选择项验证
    # (1)默认选择ON验证(tabindex="0")
    def creat_VM_page1581(self):
        data = self.data['TH-CP-VM-0110']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择UEFI验证(tabindex="0")
    def creat_VM_page1582(self):
        data1 = self.data['TH-CP-VM-0111']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0111']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0111']['data3']
        self.steps(data3)
        return service

    # <1-5-9VNC选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page1591(self):
        data = self.data['TH-CP-VM-0112']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page1592(self):
        data1 = self.data['TH-CP-VM-0113']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0113']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0113']['data3']
        self.steps(data3)
        return service

    # <1-5-10内存安全选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page15101(self):
        data = self.data['TH-CP-VM-0114']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page15102(self):
        data1 = self.data['TH-CP-VM-0115']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0115']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0115']['data3']
        self.steps(data3)
        return service

    # <1-5-11嵌套虚拟化选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page15111(self):
        data = self.data['TH-CP-VM-0116']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page15112(self):
        data1 = self.data['TH-CP-VM-0117']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0117']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0117']['data3']
        self.steps(data3)
        return service

    # <1-5-12数据本地化选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page15121(self):
        data = self.data['TH-CP-VM-0118']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page15122(self):
        data1 = self.data['TH-CP-VM-0119']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0119']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0119']['data3']
        self.steps(data3)
        return service

    # <1-5-13启用双活选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page15131(self):
        data = self.data['TH-CP-VM-0120']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page15132(self):
        data1 = self.data['TH-CP-VM-0121']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0121']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0121']['data3']
        self.steps(data3)
        return service

    # <1-5-14绑定主资源池选择项验证 （前置条件：存在两个资源池）
    # (1)默认选择OFF验证(tabindex="0")
    def creat_VM_page15141(self):
        data = self.data['TH-CP-VM-0122']
        service = self.text(data['by'], data['locator'], attr=data['attr'])
        return service

    # (2)选择ON验证(tabindex="0")
    def creat_VM_page15142(self):
        data1 = self.data['TH-CP-VM-0123']['data1']
        self.steps(data1)
        data2 = self.data['TH-CP-VM-0123']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        data3 = self.data['TH-CP-VM-0123']['data3']
        self.steps(data3)
        return service

    # <1-5-15启动配置选择项验证
    # (1)默认选择自动验证(tabindex="0")
    def creat_VM_page15151(self):
        data1 = self.data['TH-CP-VM-0125']['data1']
        self.steps(data1)
        self.keys_PageDown()
        data2 = self.data['TH-CP-VM-0124']['data2']
        service = self.text(data2['by'], data2['locator'], attr=data2['attr'])
        return service

    # (2)选择主机验证(出现主机列表，存在栏位：”宿主机“)
    def creat_VM_page15152(self):
        data1 = self.data['TH-CP-VM-0125']['data1']
        self.steps(data1)
        self.keys_PageDown()
        data2 = self.data['TH-CP-VM-0125']['data2']
        self.steps(data2)
        self.keys_PageDown()
        data3 = self.data['TH-CP-VM-0125']['data3']
        service = self.steps(data3)
        return service

    # (3)选择标签验证(出现主机列表，存在栏位：”标签名称“)
    def creat_VM_page15153(self):
        data1 = self.data['TH-CP-VM-0126']['data1']
        self.steps(data1)
        self.keys_PageDown()
        data2 = self.data['TH-CP-VM-0126']['data2']
        self.steps(data2)
        self.keys_PageDown()
        data3 = self.data['TH-CP-VM-0126']['data3']
        service = self.steps(data3)
        return service

    #1-6 完成页
    def creat_VM_page6(self):
        data1 = self.data['TH-CP-VM-0127']['data1']   #获取添加云服务器-->创建云服务器元素
        self.steps(data1)  # 依次点击添加云服务器-->创建云服务器，进入基本信息页
        data2 = self.data['TH-CP-VM-0127']['data2']  #获取进入到CPU、内存信息页的元素
        self.steps(data2)  # 进入CPU、内存信息页
        data3 = self.data['TH-CP-VM-0127']['data3'] #获取进入到存储信息页的元素
        self.steps(data3)  # 进入存储信息页
        data4 = self.data['TH-CP-VM-0127']['data4'] #获取进入到网卡信息页的元素
        self.steps(data4)  # 进入网卡信息页
        data5 = self.data['TH-CP-VM-0127']['data5'] #获取进入到高级配置页的元素
        self.steps(data5)  # 进入高级配置页
        data6 = self.data['TH-CP-VM-0127']['data6'] #获取进入到高级配置页的元素
        self.steps(data6)  # 进入完成页



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


