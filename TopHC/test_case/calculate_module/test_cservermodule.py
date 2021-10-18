import allure
import pytest
from selenium.webdriver.common.by import By

from TopHC.base.main import Main
from TopHC.others.filepath import readFilepath
from TopHC.others.yamlexcelload import loadyaml



@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('云服务器子模块--云服务器页面')  ##对模块子功能进行标注
class TestServicePage:
    def setup_class(self):
        self.main = Main(driver=None)

    filepath = readFilepath.ServerTestDataPath
    data = loadyaml(filepath)

    # 1.云服务器模块
    # 1.1云服务器页面
    @allure.title('云服务器页面入口校验')  # 对模块子功能进行标注
    def test_cservice(self):
        self.main.goto_cserver()
    # 1.1.1云服务器页面/集群信息导航栏信息校验
    # (1)集群目录信息校验
    TEST_CASE_LINK = 'https://www.kdocs.cn/p/129592400066'
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0001')
    # --allure-link-pattern=issue:https://www.baidu.com/{}  #对应的TD链接
    #@allure.issue('59561', '测试用例对应的bugID')  # bugID，传入上面的括号里
    @allure.title('集群目录信息校验')  #对模块子功能进行标注
    #@pytest.mark.parametrize("items", loadyaml(filepath))
    def test_search_clusterUI1(self):
        testdata = self.data['TH-CP-CLUSTER-0001']  #获取集群名称断言数据
        pagedata = self.main.goto_serverpage().search_clustersUI1()  #调用集群名称测试方法
        assert testdata['cluster1'] == pagedata[0]  #集群1名称断言
        assert testdata['cluster2'] == pagedata[1]  #集群2名称断言


    # （2）集群云服务器信息校验
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0002')
    @allure.title('集群云服务器信息校验')  #对模块子功能进行标注
    def test_search_clusterUI2(self):
        testdata = self.data['TH-CP-CLUSTER-0002']
        pagedata = self.main.goto_serverpage().search_clustersUI2()
        assert testdata['vm1-name'] == pagedata[0]


    #（3）集群目录结构信息校验
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0003')
    @allure.title('集群目录结构信息校验')  #对模块子功能进行标注
    def test_search_clusterUI3(self):
        testdata = self.data['TH-CP-CLUSTER-0003']
        pagedata = self.main.goto_serverpage().search_clustersUI3()
        assert testdata['group-name'] == pagedata[0]


    #（4）集群目录服务器信息校验
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0004')
    @allure.title('集群目录服务器信息校验')  #对模块子功能进行标注
    def test_search_clusterUI4(self):
        testdata = self.data['TH-CP-CLUSTER-0004']
        pagedata = self.main.goto_serverpage().search_clustersUI4()
        assert testdata['vm1-name'] == pagedata[0]


    # 1.1.2.云服务器页面/集群信息导航栏功能校验
    # (5)集群目录新增组功能验证/正常场景
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0005')
    @allure.title('集群目录新增组功能验证/正常场景')  #对模块子功能进行标注
    def test_search_clusterUI5(self):
        #testdata = self.data['TH-CP-CLUSTER-0005']
        self.main.goto_serverpage().search_clustersUI5()
        #assert testdata['vm1-name'] == pagedata[0]

    @pytest.mark.skip()
    # (6)集群目录新增组功能验证/异常场景
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0006')
    @allure.title('集群目录新增组功能验证/异常场景')  #对模块子功能进行标注
    def test_search_clustersUI6(self):
        pass

    @pytest.mark.skip()
    # (7)集群目录组名称重命名功能验证/正常场景
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0007')
    @allure.title('集群目录组名称重命名功能验证/正常场景')  # 对模块子功能进行标注
    def test_search_clustersUI7(self):
        pass

    @pytest.mark.skip()
    #（8）集群目录组名称重命名功能验证/异常场景
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0008')
    @allure.title('集群目录组名称重命名功能验证/异常场景')  #对模块子功能进行标注
    def test_search_clustersUI8(self):
        pass

    @pytest.mark.skip()
    #（9）集群目录组添加云服务器入口验证
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0009')
    @allure.title('集群目录组添加云服务器入口验证')  #对模块子功能进行标注
    def test_search_clustersUI9(self):
        pass

    @pytest.mark.skip()
    #（10）集群目录组移动验证
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0010')
    @allure.title('集群目录组移动验证')  #对模块子功能进行标注
    def test_search_clustersUI10(self):
        pass

    @pytest.mark.skip()
    #（11）集群目录组删除验证
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0011')
    @allure.title('集群目录组删除验证')  #对模块子功能进行标注
    def test_search_clustersUI11(self):
        pass


    # 1.2.1.云服务器页面/菜单栏功能校验/搜索
    #(1) 功能入口参数校验/弱提示
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0001')
    @allure.title('菜单栏功能校验/搜索功能/弱提示信息校验')  #对模块子功能进行标注
    def test_search__VM1(self):
        testdata = self.data['TH-CP-VM-0001']
        pagedata = self.main.goto_serverpage().search_VM1()
        assert testdata['text'] == pagedata
        #print(testdata['text'])
        #print(pagedata)


    # (2) 搜索功能验证/正常场景
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0002')
    @allure.title('菜单栏功能校验/搜索功能验证/正常场景')  #对模块子功能进行标注
    def test_search__VM2(self):
        testdata = self.data['TH-CP-VM-0002']
        pagedata = self.main.goto_serverpage().search_VM2()
        assert testdata['vm_name'] == pagedata[0]


    # (3) 搜索功能验证/异常场景
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0003')
    @allure.title('菜单栏功能校验/搜索功能验证/异常场景')  #对模块子功能进行标注
    def test_search__VM3(self):
        testdata = self.data['TH-CP-VM-0003']
        pagedata = self.main.goto_serverpage().search_VM3()
        assert testdata['vm_name'] == pagedata[0]

    # 1.2.2.云服务器页面/菜单栏功能校验/虚拟机批量操作

    # 1.2.3.云服务器页面/菜单栏功能校验/添加云服务器
    # 1.2.3.1 创建云服务器
    # <1 自定义
    # <1-1 基本信息页参数校验
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0004~0007')
    @allure.title('添加云服务器/基本信息页参数校验')  #对模块子功能进行标注
    def test_creat_VM_page1(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()

    # <1-1-1云服务器输入框验证
    # (1)云服务器输入框弱提示验证7
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框弱提示验证')  # 对模块子功能进行标注
    def test_creat_VM_page1111(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1111()
        testdata01 = self.data['TH-CP-VM-0004']  # 云服务器输入框弱提示信息
        print(pagedata)
        assert testdata01['cservice_name'] == pagedata

    # (2)云服务器输入框输入为空验证
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1112(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1112()
        testdata = self.data['TH-CP-VM-0005']  # 云服务器输入框输入为空提示信息
        assert testdata['title_name'] == pagedata[0]

    # (3)云服务器输入框输入特殊字符验证
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1113(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1113()
        print(pagedata[0])
        testdata = self.data['TH-CP-VM-0006']  # 云服务器输入框输入特殊字符提示信息
        assert testdata['title_name'] == pagedata[0]

    # (4)云服务器输入框输入大于32位字符验证
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框输入大于32位字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1114(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1114()
        testdata04 = self.data['TH-CP-VM-0007']  # 云服务器输入框输入大于32位字符提示信息
        assert testdata04['title3_name'] == pagedata[0]

    # <1-1-2操作系统下拉框验证
    # (1)操作系统下拉框选择 FreeBSD
    @allure.title('<1-1-2操作系统下拉框验证/操作系统下拉框选择验证')  # 对模块子功能进行标注
    def test_creat_VM_page1121(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1121()
        testdata = self.data['TH-CP-VM-0008']  # 操作系统下拉框选项
        assert testdata['system_name'] == pagedata[0]

    # <1-1-3创建个数输入框验证
    # (1)创建个数输入默认值验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1131(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1131()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0009']  # 创建个数输入框默认值
        assert testdata['server_num'] == pagedata

    # (2)创建个数输入框输入为空验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1132(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1132()
        testdata = self.data['TH-CP-VM-0010']  # 创建个数输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)创建个数输入框输入特殊字符验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1133(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1133()
        testdata = self.data['TH-CP-VM-0011']  # 创建个数输入框输入特殊字符
        assert testdata['title_name'] == pagedata[0]

    # (4)创建个数输入框输入大于100验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入大于100验证')  # 对模块子功能进行标注
    def test_creat_VM_page1134(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1134()
        testdata = self.data['TH-CP-VM-0012']  # 创建个数输入框输入大于100
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)创建个数输入框输入小于1验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1135(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1135()
        testdata = self.data['TH-CP-VM-0013']  # 创建个数输入框输入小于1
        assert testdata['title_name'] == pagedata[0]


    # <1 自定义
    # <1-2 CPU、内存信息页参数校验
    @allure.title('添加云服务器/CPU、内存信息页参数校验')  #对模块子功能进行标注
    def test_creat_VM_page2(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()

    # <1-2-1处理器输入框验证
    # (1)处理器输入默认值验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1211(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1211()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0014']  # 创建个数输入框默认值
        assert testdata['server_num'] == pagedata[0]

    # (2)处理器输入框输入为空验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1212(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1212()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0015']  # 创建个数输入框输入为空
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)处理器输入框输入特殊字符验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1213(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1213()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0016']  # 创建个数输入框输入特殊字符
        assert testdata['title_name'] == pagedata[0]

    # (4)处理器输入框输入大于2验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1214(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1214()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0017']  # 创建个数输入框输入大于2
        assert testdata['title_name'] == pagedata[0]

    # (5)处理器输入框输入小于1验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1215(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1215()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0018']  # 创建个数输入框输入小于1
        assert testdata['title_name'] == pagedata[0]

    # <1-2-2插槽数输入框验证
    # (1)插槽数输入默认值验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1221(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1221()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0019']  # 插槽数输入框默认值
        assert testdata['server_num'] == pagedata[0]

    # (2)插槽数输入框输入为空验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1222(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1222()
        testdata = self.data['TH-CP-VM-0020']  # 插槽数输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)插槽数输入框输入特殊字符验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1223(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1223()
        testdata = self.data['TH-CP-VM-0021']  # 插槽数输入框输入特殊字符
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (4)插槽数输入框输入大于4验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入大于4验证')  # 对模块子功能进行标注
    def test_creat_VM_page1224(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1224()
        testdata = self.data['TH-CP-VM-0022']  # 插槽数输入框输入大于2
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)插槽数输入框输入小于1验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1225(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1225()
        testdata = self.data['TH-CP-VM-0023']  # 插槽数输入框输入小于1
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # <1-2-3插槽核数输入框验证
    # (1)插槽核数输入默认值验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1231(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1231()
        testdata = self.data['TH-CP-VM-0024']  # 插槽核数输入框默认值
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)插槽核数输入框输入为空验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1232(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1232()
        testdata = self.data['TH-CP-VM-0025']  # 插槽核数输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]


    # (3)插槽核数输入框输入特殊字符验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1233(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1233()
        testdata = self.data['TH-CP-VM-0026']  # 插槽核数输入框输入特殊字符
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (4)插槽核数输入框输入大于24验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入大于24验证')  # 对模块子功能进行标注
    def test_creat_VM_page1234(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1234()
        testdata = self.data['TH-CP-VM-0027']  # 插槽核数输入框输入大于24
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)插槽核数输入框输入小于1验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1235(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1235()
        testdata = self.data['TH-CP-VM-0028']  # 插槽核数输入框输入小于1
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # <1-2-4内存大小输入框验证
    # (1)内存大小输入默认值验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1241(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1241()
        testdata = self.data['TH-CP-VM-0029']  # 内存大小输入框默认值
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)内存大小输入框输入为空验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1242(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1242()
        testdata = self.data['TH-CP-VM-0030']  # 内存大小输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)内存大小输入框输入特殊字符验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1243(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1243()
        testdata = self.data['TH-CP-VM-0031']  # 内存大小输入框输入特殊字符
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (4)内存大小输入框输入大于256验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入大于256验证')  # 对模块子功能进行标注
    def test_creat_VM_page1244(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1244()
        testdata = self.data['TH-CP-VM-0032']  # 内存大小输入框输入大于256
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)内存大小输入框输入小于1验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1245(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1245()
        testdata = self.data['TH-CP-VM-0033']  # 内存大小输入框输入小于0.5
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # <1-2-5基准类型下拉框验证
    # (1)基准类型下拉框选择 arm/Phytium/Tengyun-S2500
    @allure.title('<1-2-5基准类型下拉框验证/基准类型下拉框选择 arm/Phytium/Tengyun-S2500')  # 对模块子功能进行标注
    def test_creat_VM_page1251(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1251()
        testdata = self.data['TH-CP-VM-0034']  # 操作系统下拉框选项
        print(pagedata)
        assert testdata['system_name'] == pagedata[0]

    # <1 自定义
    # <1-3 存储信息页参数校验
    #云硬盘/自定义
    @allure.title('存储信息页参数校验')  # 对模块子功能进行标注
    def test_creat_VM_page3(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()

    # <1-3-1磁盘大小输入框验证
    # (1)磁盘大小默认为空时弱提示验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小默认为空时弱提示验证')  # 对模块子功能进行标注
    def test_creat_VM_page1311(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1311()
        testdata = self.data['TH-CP-VM-0035']  # 磁盘大小输入框默认为空时弱提示
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)磁盘大小输入框输入为空验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1312(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1312()
        testdata = self.data['TH-CP-VM-0036']  # 磁盘大小输入框输入为空
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (3)磁盘大小输入框输入特殊字符验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1313(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1313()
        testdata = self.data['TH-CP-VM-0037']  # 磁盘大小输入框输入特殊字符
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)磁盘大小输入框输入大于256T验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入大于256T验证')  # 对模块子功能进行标注
    def test_creat_VM_page1314(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1314()
        testdata04 = self.data['TH-CP-VM-0038']  # 磁盘大小输入框输入大于256T
        print(pagedata)
        assert testdata04['server1_num'] == pagedata[0]
        assert testdata04['server2_num'] == pagedata[1]

    # (5)内存大小输入框输入小于0.5验证
    @allure.title('<1-3-1磁盘大小输入框验证/内存大小输入框输入小于0.5验证')  # 对模块子功能进行标注
    def test_creat_VM_page1315(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1315()
        testdata = self.data['TH-CP-VM-0039']  # 内存大小输入框输入小于0.5
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-3-2驱动类型选择项验证
    # (1)默认选择scsi验证(tabindex="0")
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入大于256T验证')  # 对模块子功能进行标注
    def test_creat_VM_page1321(self):
        self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1315()
        testdata06 = self.data['TH-CP-VM-0040']
        assert testdata06['server1_num'] == pagedata[5]
        assert testdata06['server2_num'] == pagedata[6]

        # <1-3-3存储池下拉框验证
        testdata07 = self.data['TH-CP-VM-0041']
        assert testdata07['server_num'] == pagedata[7][0]

        # <1-3-4卷名称输入框验证
        # (1)卷名称输入框默认值验证
        testdata08 = self.data['TH-CP-VM-0042']
        assert testdata08['server_num'] == pagedata[8]
        # (2)卷名称输入框输入为空验证
        testdata09 = self.data['TH-CP-VM-0043']
        assert testdata09['server1_num'] == pagedata[9][0]
        assert testdata09['server2_num'] == pagedata[10]
        # (3)卷名称输入框输入特殊字符验证
        testdata10 = self.data['TH-CP-VM-0044']
        assert testdata10['server_num'] == pagedata[11][0]

        # (4)卷名称输入框输入大于32位字符验证
        testdata11 = self.data['TH-CP-VM-0045']
        assert testdata11['server_num'] == pagedata[12][0]

        # <1-3-5副本数下拉框验证
        testdata12 = self.data['TH-CP-VM-0046']
        assert testdata12['server1_num'] == pagedata[13]
        assert testdata12['server2_num'] == pagedata[14]

        # <1-3-6云盘类型下拉框验证
        testdata13 = self.data['TH-CP-VM-0047']
        assert testdata13['server1_num'] == pagedata[15]
        assert testdata13['server2_num'] == pagedata[16]

        # <1-3-7存储介质下拉框验证
        testdata14 = self.data['TH-CP-VM-0048']
        assert testdata14['server1_num'] == pagedata[17]
        assert testdata14['server2_num'] == pagedata[18]

        # <1-3-8链路冗余下拉框验证
        testdata15 = self.data['TH-CP-VM-0049']
        assert testdata15['server1_num'] == pagedata[19]
        assert testdata15['server2_num'] == pagedata[20]

    # <1 自定义
    # <1-4 网卡信息页参数校验
    @allure.title('网卡信息页参数校验')  # 对模块子功能进行标注
    def test_creat_VM_page4(self):
        self.main.goto_cserver()
        pagedata = self.main.goto_serverpage().creat_VM_page4()
        print(pagedata)

        # # <1-4-1添加网卡功能验证
        # testdata01 = self.data['TH-CP-VM-0050']
        # assert testdata01['server_num'] == pagedata[0][0]

        # # <1-4-2网卡信息折叠功能验证
        # testdata02 = self.data['TH-CP-VM-0051']
        # assert testdata02['server_num'] == pagedata[1]

        # # <1-4-3网卡下拉框验证
        # testdata14 = self.data['TH-CP-VM-0052']
        # assert testdata14['server1_num'] == pagedata[2]
        # assert testdata14['server2_num'] == pagedata[3]

        # #<1-4-4适配器下拉框验证
        # testdata15 = self.data['TH-CP-VM-0053']
        # assert testdata15['server1_num'] == pagedata[4]
        # assert testdata15['server2_num'] == pagedata[5]

        # #<1-4-5多队列设置开关验证
        # testdata15 = self.data['TH-CP-VM-0054']
        # assert testdata15['server1_num'] == pagedata[6]
        # assert testdata15['server2_num'] == pagedata[7]

        # <1-4-6队列数输入框验证
        #(1)队列数输入框默认值验证
        # testdata16 = self.data['TH-CP-VM-0055']
        # assert testdata16['server_num'] == pagedata[8]
        # #(2)队列数输入框输入为空验证
        # testdata09 = self.data['TH-CP-VM-0056']
        # assert testdata09['server1_num'] == pagedata[9][0]
        # assert testdata09['server2_num'] == pagedata[10]
        # # (3)队列数输入框输入特殊字符验证
        # testdata10 = self.data['TH-CP-VM-0057']
        # assert testdata10['server_num'] == pagedata[11][0]
        # #(4)队列数输入框输入大于2验证
        # testdata11 = self.data['TH-CP-VM-0058']
        # assert testdata11['server_num'] == pagedata[12][0]
        # #(5)队列数输入框输入小于1验证
        # testdata11 = self.data['TH-CP-VM-0059']
        # assert testdata11['server_num'] == pagedata[13][0]

        # <1-4-7虚拟交换机下拉框验证
        # testdata12 = self.data['TH-CP-VM-0060']
        # assert testdata12['server1_num'] == pagedata[14]
        # assert testdata13['server2_num'] == pagedata[15]







        # # 2.1.2 模板模块功能验证
    # def test_search_clusterUI21(self):
    #     self.main.goto_cmouldpage().search_clustersUI21()

'''
    #(2)集群云服务器信息校验
    @pytest.mark.parametrize("items", YamlUtil.loadyaml(r'D:\WorkTools\PyProjects\TopHC\data\test_data\calculate_module_data\cserver_module\cal_cserver_cluster2.yaml'))
    def test_search_clusterUI2(self, items):
        tt = self.main.goto_serverpage().search_clustersUI2()
        assert items['uuid1'] == tt[3]


    #(3)集群目录结构信息校验
    @pytest.mark.parametrize("items", YamlUtil.loadyaml(r"D:\WorkTools\PyProjects\TopHC\data\test_data\calculate_module_data\cserver_module\cal_cserver_cluster3.yaml"))
    def test_search_clusterUI3(self, items):
        tt = self.main.goto_serverpage().search_clustersUI3()
        assert items['zu'] == tt[1]

    # (4)集群目录下服务器信息校验
    @pytest.mark.parametrize("items", YamlUtil.loadyaml(r"D:\WorkTools\PyProjects\TopHC\data\test_data\calculate_module_data\cserver_module\cal_cserver_cluster4.yaml"))
    def test_search_clusterUI3(self, items):
        tt = self.main.goto_serverpage().search_clustersUI3()
        assert items['uuid1'] == tt[3]

    # 1-1-2.集群信息导航栏功能校验
    #(5)集群目录新增组功能验证(正常/异常场景)
    @pytest.mark.parametrize("items", YamlUtil.loadyaml(r"D:\WorkTools\PyProjects\TopHC\data\test_data\calculate_module_data\cserver_module\cal_cserver_addgroup.yaml"))
    def test_add_group(self, items):
        tt = self.main.goto_serverpage().add_group()
        assert items['uuid1'] == tt[3]

    #(6)集群目录组名称重命名功能验证(正常/异常场景)
    @pytest.mark.parametrize("items", YamlUtil.loadyaml(r"D:\WorkTools\PyProjects\TopHC\data\test_data\calculate_module_data\cserver_module\cal_cserver_updategroup.yaml"))
    def test_update_group(self, items):
        tt = self.main.goto_serverpage().update_group()
        assert items['uuid1'] == tt[3]


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




