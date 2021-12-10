import allure
import pytest
from selenium.webdriver.common.by import By

from TopEC.base.main import Main
from TopEC.others.filepath import readFilepath
from TopEC.others.yamlexcelload import loadyaml



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
    # # 1.1.1云服务器页面/集群信息导航栏信息校验
    # # (1)集群目录信息校验
    # TEST_CASE_LINK = 'https://www.kdocs.cn/p/129592400066'
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0001')
    # # --allure-link-pattern=issue:https://www.baidu.com/{}  #对应的TD链接
    # #@allure.issue('59561', '测试用例对应的bugID')  # bugID，传入上面的括号里
    # @allure.title('集群目录信息校验')  #对模块子功能进行标注
    # #@pytest.mark.parametrize("items", loadyaml(filepath))
    # def test_search_clusterUI1(self):
    #     testdata = self.data['TH-CP-CLUSTER-0001']  #获取集群名称断言数据
    #     pagedata = self.main.goto_serverpage().search_clustersUI1()  #调用集群名称测试方法
    #     assert testdata['cluster1'] == pagedata[0]  #集群1名称断言
    #     assert testdata['cluster2'] == pagedata[1]  #集群2名称断言
    #
    #
    # # （2）集群云服务器信息校验
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0002')
    # @allure.title('集群云服务器信息校验')  #对模块子功能进行标注
    # def test_search_clusterUI2(self):
    #     testdata = self.data['TH-CP-CLUSTER-0002']
    #     pagedata = self.main.goto_serverpage().search_clustersUI2()
    #     assert testdata['vm1-name'] == pagedata[0]
    #
    #
    # #（3）集群目录结构信息校验
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0003')
    # @allure.title('集群目录结构信息校验')  #对模块子功能进行标注
    # def test_search_clusterUI3(self):
    #     testdata = self.data['TH-CP-CLUSTER-0003']
    #     pagedata = self.main.goto_serverpage().search_clustersUI3()
    #     assert testdata['group-name'] == pagedata[0]
    #
    #
    # #（4）集群目录服务器信息校验
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0004')
    # @allure.title('集群目录服务器信息校验')  #对模块子功能进行标注
    # def test_search_clusterUI4(self):
    #     testdata = self.data['TH-CP-CLUSTER-0004']
    #     pagedata = self.main.goto_serverpage().search_clustersUI4()
    #     assert testdata['vm1-name'] == pagedata[0]
    #
    #
    # # 1.1.2.云服务器页面/集群信息导航栏功能校验
    # # (5)集群目录新增组功能验证/正常场景
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0005')
    # @allure.title('集群目录新增组功能验证/正常场景')  #对模块子功能进行标注
    # def test_search_clusterUI5(self):
    #     #testdata = self.data['TH-CP-CLUSTER-0005']
    #     self.main.goto_serverpage().search_clustersUI5()
    #     #assert testdata['vm1-name'] == pagedata[0]
    #
    # @pytest.mark.skip()
    # # (6)集群目录新增组功能验证/异常场景
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0006')
    # @allure.title('集群目录新增组功能验证/异常场景')  #对模块子功能进行标注
    # def test_search_clustersUI6(self):
    #     pass
    #
    # @pytest.mark.skip()
    # # (7)集群目录组名称重命名功能验证/正常场景
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0007')
    # @allure.title('集群目录组名称重命名功能验证/正常场景')  # 对模块子功能进行标注
    # def test_search_clustersUI7(self):
    #     pass
    #
    # @pytest.mark.skip()
    # #（8）集群目录组名称重命名功能验证/异常场景
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0008')
    # @allure.title('集群目录组名称重命名功能验证/异常场景')  #对模块子功能进行标注
    # def test_search_clustersUI8(self):
    #     pass
    #
    # @pytest.mark.skip()
    # #（9）集群目录组添加云服务器入口验证
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0009')
    # @allure.title('集群目录组添加云服务器入口验证')  #对模块子功能进行标注
    # def test_search_clustersUI9(self):
    #     pass
    #
    # @pytest.mark.skip()
    # #（10）集群目录组移动验证
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0010')
    # @allure.title('集群目录组移动验证')  #对模块子功能进行标注
    # def test_search_clustersUI10(self):
    #     pass
    #
    # @pytest.mark.skip()
    # #（11）集群目录组删除验证
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0011')
    # @allure.title('集群目录组删除验证')  #对模块子功能进行标注
    # def test_search_clustersUI11(self):
    #     pass
    #
    #
    # # 1.2.1.云服务器页面/菜单栏功能校验/搜索
    # #(1) 功能入口参数校验/弱提示
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0001')
    # @allure.title('菜单栏功能校验/搜索功能/弱提示信息校验')  #对模块子功能进行标注
    # def test_search__VM1(self):
    #     testdata = self.data['TH-CP-VM-0001']
    #     pagedata = self.main.goto_serverpage().search_VM1()
    #     print(pagedata)
    #     assert testdata['text'] == pagedata
    #
    #
    #
    # # (2) 搜索功能验证/正常场景
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0002')
    # @allure.title('菜单栏功能校验/搜索功能验证/正常场景')  #对模块子功能进行标注
    # def test_search__VM2(self):
    #     testdata = self.data['TH-CP-VM-0002']
    #     pagedata = self.main.goto_serverpage().search_VM2()
    #     print(pagedata)
    #     assert testdata['vm_name'] == pagedata[0]
    #
    #
    # # (3) 搜索功能验证/异常场景
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0003')
    # @allure.title('菜单栏功能校验/搜索功能验证/异常场景')  #对模块子功能进行标注
    # def test_search__VM3(self):
    #     testdata = self.data['TH-CP-VM-0003']
    #     pagedata = self.main.goto_serverpage().search_VM3()
    #     print(pagedata)
    #     assert testdata['vm_name'] == pagedata[0]
    #
    # # 1.2.2.云服务器页面/菜单栏功能校验/虚拟机批量操作

    # 1.2.3.云服务器页面/菜单栏功能校验/添加云服务器
    # 1.2.3.1 创建云服务器
    # <1 自定义
    # <1-1 基本信息页参数校验
    # @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-VM-0004~0007')
    @allure.title('添加云服务器/基本信息页参数校验')  #对模块子功能进行标注
    def test_creat_VM_page1(self):
        # self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page1()

    # <1-1-1云服务器输入框验证
    # (1)云服务器输入框弱提示验证7
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框弱提示验证')  # 对模块子功能进行标注
    def test_creat_VM_page1111(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1111()
        testdata01 = self.data['TH-CP-VM-0004']  # 云服务器输入框弱提示信息
        print(pagedata)
        assert testdata01['cservice_name'] == pagedata

    # (2)云服务器输入框输入为空验证
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1112(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1112()
        testdata = self.data['TH-CP-VM-0005']  # 云服务器输入框输入为空提示信息
        assert testdata['title_name'] == pagedata[0]

    # (3)云服务器输入框输入特殊字符验证
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1113(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1113()
        print(pagedata[0])
        testdata = self.data['TH-CP-VM-0006']  # 云服务器输入框输入特殊字符提示信息
        assert testdata['title_name'] == pagedata[0]

    # (4)云服务器输入框输入大于32位字符验证
    @allure.title('<1-1-1云服务器输入框验证/云服务器输入框输入大于32位字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1114(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1114()
        testdata04 = self.data['TH-CP-VM-0007']  # 云服务器输入框输入大于32位字符提示信息
        assert testdata04['title3_name'] == pagedata[0]

    # <1-1-2操作系统下拉框验证
    # (1)操作系统下拉框选择 FreeBSD
    @allure.title('<1-1-2操作系统下拉框验证/操作系统下拉框选择验证')  # 对模块子功能进行标注
    def test_creat_VM_page1121(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1121()
        testdata = self.data['TH-CP-VM-0008']  # 操作系统下拉框选项
        assert testdata['system_name'] == pagedata[0]

    # <1-1-3创建个数输入框验证
    # (1)创建个数输入默认值验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1131(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1131()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0009']  # 创建个数输入框默认值
        assert testdata['server_num'] == pagedata

    # (2)创建个数输入框输入为空验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1132(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1132()
        testdata = self.data['TH-CP-VM-0010']  # 创建个数输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)创建个数输入框输入特殊字符验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1133(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1133()
        testdata = self.data['TH-CP-VM-0011']  # 创建个数输入框输入特殊字符
        assert testdata['title_name'] == pagedata[0]

    # (4)创建个数输入框输入大于100验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入大于100验证')  # 对模块子功能进行标注
    def test_creat_VM_page1134(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1134()
        testdata = self.data['TH-CP-VM-0012']  # 创建个数输入框输入大于100
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)创建个数输入框输入小于1验证
    @allure.title('<1-1-3创建个数输入框验证/创建个数输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1135(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page1()
        pagedata = self.main.goto_serverpage().creat_VM_page1135()
        testdata = self.data['TH-CP-VM-0013']  # 创建个数输入框输入小于1
        assert testdata['title_name'] == pagedata[0]


    # <1 自定义
    # <1-2 CPU、内存信息页参数校验
    @allure.title('添加云服务器/CPU、内存信息页参数校验')  #对模块子功能进行标注
    def test_creat_VM_page2(self):
        # self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page2()

    # <1-2-1处理器输入框验证
    # (1)处理器输入默认值验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1211(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1211()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0014']  # 创建个数输入框默认值
        assert testdata['server_num'] == pagedata[0]

    # (2)处理器输入框输入为空验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1212(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1212()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0015']  # 创建个数输入框输入为空
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)处理器输入框输入特殊字符验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1213(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1213()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0016']  # 创建个数输入框输入特殊字符
        assert testdata['title_name'] == pagedata[0]

    # (4)处理器输入框输入大于2验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1214(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1214()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0017']  # 创建个数输入框输入大于2
        assert testdata['title_name'] == pagedata[0]

    # (5)处理器输入框输入小于1验证
    @allure.title('<1-2-1处理器输入框验证/处理器输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1215(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1215()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0018']  # 创建个数输入框输入小于1
        assert testdata['title_name'] == pagedata[0]

    # <1-2-2插槽数输入框验证
    # (1)插槽数输入默认值验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1221(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1221()
        print(pagedata)
        testdata = self.data['TH-CP-VM-0019']  # 插槽数输入框默认值
        assert testdata['server_num'] == pagedata[0]

    # (2)插槽数输入框输入为空验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1222(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1222()
        testdata = self.data['TH-CP-VM-0020']  # 插槽数输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)插槽数输入框输入特殊字符验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1223(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1223()
        testdata = self.data['TH-CP-VM-0021']  # 插槽数输入框输入特殊字符
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (4)插槽数输入框输入大于4验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入大于4验证')  # 对模块子功能进行标注
    def test_creat_VM_page1224(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1224()
        testdata = self.data['TH-CP-VM-0022']  # 插槽数输入框输入大于2
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)插槽数输入框输入小于1验证
    @allure.title('<1-2-2插槽数输入框验证/插槽数输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1225(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1225()
        testdata = self.data['TH-CP-VM-0023']  # 插槽数输入框输入小于1
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # <1-2-3插槽核数输入框验证
    # (1)插槽核数输入默认值验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1231(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1231()
        testdata = self.data['TH-CP-VM-0024']  # 插槽核数输入框默认值
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)插槽核数输入框输入为空验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1232(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1232()
        testdata = self.data['TH-CP-VM-0025']  # 插槽核数输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]


    # (3)插槽核数输入框输入特殊字符验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1233(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1233()
        testdata = self.data['TH-CP-VM-0026']  # 插槽核数输入框输入特殊字符
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (4)插槽核数输入框输入大于24验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入大于24验证')  # 对模块子功能进行标注
    def test_creat_VM_page1234(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1234()
        testdata = self.data['TH-CP-VM-0027']  # 插槽核数输入框输入大于24
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)插槽核数输入框输入小于1验证
    @allure.title('<1-2-3插槽核数输入框验证/插槽核数输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1235(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1235()
        testdata = self.data['TH-CP-VM-0028']  # 插槽核数输入框输入小于1
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # <1-2-4内存大小输入框验证
    # (1)内存大小输入默认值验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1241(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1241()
        testdata = self.data['TH-CP-VM-0029']  # 内存大小输入框默认值
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)内存大小输入框输入为空验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1242(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1242()
        testdata = self.data['TH-CP-VM-0030']  # 内存大小输入框输入为空
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)内存大小输入框输入特殊字符验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1243(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1243()
        testdata = self.data['TH-CP-VM-0031']  # 内存大小输入框输入特殊字符
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (4)内存大小输入框输入大于256验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入大于256验证')  # 对模块子功能进行标注
    def test_creat_VM_page1244(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1244()
        testdata = self.data['TH-CP-VM-0032']  # 内存大小输入框输入大于256
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # (5)内存大小输入框输入小于1验证
    @allure.title('<1-2-4内存大小输入框验证/内存大小输入框输入小于1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1245(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1245()
        testdata = self.data['TH-CP-VM-0033']  # 内存大小输入框输入小于0.5
        print(pagedata)
        assert testdata['title_name'] == pagedata[0]

    # <1-2-5基准类型下拉框验证
    # (1)基准类型下拉框选择 arm/Phytium/Tengyun-S2500
    @allure.title('<1-2-5基准类型下拉框验证/基准类型下拉框选择 arm/Phytium/Tengyun-S2500')  # 对模块子功能进行标注
    def test_creat_VM_page1251(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page2()
        pagedata = self.main.goto_serverpage().creat_VM_page1251()
        testdata = self.data['TH-CP-VM-0034']  # 操作系统下拉框选项
        print(pagedata)
        assert testdata['system_name'] == pagedata[0]

    # <1 自定义
    # <1-3 存储信息页参数校验
    #云硬盘/自定义
    @allure.title('存储信息页参数校验')  # 对模块子功能进行标注
    def test_creat_VM_page3(self):
        # self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page3()

    # <1-3-1磁盘大小输入框验证
    # (1)磁盘大小默认为空时弱提示验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小默认为空时弱提示验证')  # 对模块子功能进行标注
    def test_creat_VM_page1311(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1311()
        testdata = self.data['TH-CP-VM-0035']  # 磁盘大小输入框默认为空时弱提示
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)磁盘大小输入框输入为空验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1312(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1312()
        testdata = self.data['TH-CP-VM-0036']  # 磁盘大小输入框输入为空
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (3)磁盘大小输入框输入特殊字符验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1313(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1313()
        testdata = self.data['TH-CP-VM-0037']  # 磁盘大小输入框输入特殊字符
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)磁盘大小输入框输入大于256T验证
    @allure.title('<1-3-1磁盘大小输入框验证/磁盘大小输入框输入大于256T验证')  # 对模块子功能进行标注
    def test_creat_VM_page1314(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1314()
        testdata04 = self.data['TH-CP-VM-0038']  # 磁盘大小输入框输入大于256T
        print(pagedata)
        assert testdata04['server1_num'] == pagedata[0]
        assert testdata04['server2_num'] == pagedata[1]

    # (5)内存大小输入框输入小于0.5验证
    @allure.title('<1-3-1磁盘大小输入框验证/内存大小输入框输入小于0.5验证')  # 对模块子功能进行标注
    def test_creat_VM_page1315(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1315()
        testdata = self.data['TH-CP-VM-0039']  # 内存大小输入框输入小于0.5
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-3-2驱动类型选择项验证
    # (1)默认选择scsi验证(tabindex="0")
    @allure.title('<1-3-2驱动类型选择项验证/默认选择scsi验证')  # 对模块子功能进行标注
    def test_creat_VM_page1321(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1321()
        testdata = self.data['TH-CP-VM-0040']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)选择ide验证(tabindex="0")
    @allure.title('<1-3-2驱动类型选择项验证/选择ide验证')  # 对模块子功能进行标注
    def test_creat_VM_page1322(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1322()
        testdata = self.data['TH-CP-VM-0040']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-3-3存储池下拉框验证
    @allure.title('<1-3-3存储池下拉框验证')  # 对模块子功能进行标注
    def test_creat_VM_page1331(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1331()
        testdata = self.data['TH-CP-VM-0041']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-3-4卷名称输入框验证
    # (1)卷名称输入框默认值验证
    @allure.title('<1-3-4卷名称输入框验证/卷名称输入框默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1341(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1341()
        testdata = self.data['TH-CP-VM-0042']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)卷名称输入框输入为空验证
    @allure.title('<1-3-4卷名称输入框验证/卷名称输入框输入为空验证')  # 对模块子功能进行标注
    def test_creat_VM_page1342(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1342()
        testdata = self.data['TH-CP-VM-0043']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]

    # (3)卷名称输入框输入特殊字符验证
    @allure.title('<1-3-4卷名称输入框验证/卷名称输入框输入特殊字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1343(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1343()
        testdata = self.data['TH-CP-VM-0044']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)卷名称输入框输入大于32位字符验证
    @allure.title('<1-3-4卷名称输入框验证/卷名称输入框输入大于32位字符验证')  # 对模块子功能进行标注
    def test_creat_VM_page1344(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1344()
        testdata = self.data['TH-CP-VM-0045']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-3-5副本数下拉框验证
    # (1)副本数默认值验证
    @allure.title('<1-3-5副本数下拉框验证/副本数默认值验证')  # 对模块子功能进行标注
    def test_creat_VM_page1351(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1351()
        testdata = self.data['TH-CP-VM-0046']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)副本数选择值验证
    @allure.title('<1-3-5副本数下拉框验证/副本数选择值1验证')  # 对模块子功能进行标注
    def test_creat_VM_page1352(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1352()
        testdata = self.data['TH-CP-VM1-0046']
        print(pagedata)
        assert testdata['server_num'] == pagedata


    # <1-3-6云盘类型下拉框验证
    # (1)云盘类型默认值验证：普通云盘1.0
    @allure.title('<1-3-6云盘类型下拉框验证/云盘类型默认值验证：普通云盘1.0')  # 对模块子功能进行标注
    def test_creat_VM_page1361(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1361()
        testdata = self.data['TH-CP-VM-0047']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)云盘类型选择值验证：高效云盘
    @allure.title('<1-3-6云盘类型下拉框验证/云盘类型选择值验证：高效云盘')  # 对模块子功能进行标注
    def test_creat_VM_page1362(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1362()
        testdata = self.data['TH-CP-VM1-0047']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-3-7存储介质下拉框验证
    # (1)存储介质默认值验证：机械硬盘
    @allure.title('<1-3-7存储介质下拉框验证/存储介质默认值验证：机械硬盘')  # 对模块子功能进行标注
    def test_creat_VM_page1371(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1371()
        testdata = self.data['TH-CP-VM-0048']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)存储介质选择值验证：固态硬盘
    @allure.title('<1-3-7存储介质下拉框验证/存储介质选择值验证：固态硬盘')  # 对模块子功能进行标注
    def test_creat_VM_page1372(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1372()
        testdata = self.data['TH-CP-VM1-0048']
        print(pagedata)
        assert testdata['server_num'] == pagedata


    # <1-3-8链路冗余下拉框验证
    # (1)链路冗余默认值验证：1
    @allure.title('<1-3-8链路冗余下拉框验证/链路冗余默认值验证：1')  # 对模块子功能进行标注
    def test_creat_VM_page1381(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1381()
        testdata = self.data['TH-CP-VM-0049']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)链路冗余选择值验证：3
    @allure.title('<1-3-8链路冗余下拉框验证/链路冗余选择值验证：3')  # 对模块子功能进行标注
    def test_creat_VM_page1382(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page3()
        pagedata = self.main.goto_serverpage().creat_VM_page1382()
        testdata = self.data['TH-CP-VM1-0049']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1 自定义
    # <1-4 网卡信息页参数校验
    @allure.title('网卡信息页参数校验')  # 对模块子功能进行标注
    def test_creat_VM_page4(self):
        # self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page4()

    # <1-4-1添加网卡功能验证
    @allure.title('<1-4-1添加网卡功能验证')  # 对模块子功能进行标注
    def test_creat_VM_page1411(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1411()
        testdata = self.data['TH-CP-VM-0050']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-4-2网卡信息折叠功能验证
    @allure.title('<1-4-2网卡信息折叠功能验证')
    def test_creat_VM_page1421(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1421()
        testdata = self.data['TH-CP-VM-0051']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0]
        assert testdata['server2_num'] == pagedata[1]

    # <1-4-3网卡下拉框验证
    # (1)网卡类型默认值验证：本地网络(存在虚拟交换机选项)
    @allure.title('<1-4-3网卡下拉框验证/网卡类型默认值验证：本地网络')
    def test_creat_VM_page1431(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1431()
        testdata = self.data['TH-CP-VM-0052']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)网卡类型选择值验证：VPC网络(存在VPC交换机选项)
    @allure.title('<1-4-3网卡下拉框验证/网卡类型选择值验证：VPC网络')
    def test_creat_VM_page1432(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1432()
        testdata = self.data['TH-CP-VM1-0052']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]


    #<1-4-4适配器下拉框验证
    # (1)适配器类型默认值验证：virtio
    @allure.title('<1-4-4适配器下拉框验证/适配器类型默认值验证：virtio')
    def test_creat_VM_page1441(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1441()
        testdata = self.data['TH-CP-VM-0053']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)适配器类型选择值验证：rtl8139
    @allure.title('<1-4-4适配器下拉框验证/适配器类型选择值验证：rtl8139')
    def test_creat_VM_page1442(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1442()
        testdata = self.data['TH-CP-VM1-0053']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    #<1-4-5多队列设置开关验证
    # (1)默认关闭状态验证(关闭状态下队列数输入框不存在)
    @allure.title('<1-4-5多队列设置开关验证/默认关闭状态验证')
    def test_creat_VM_page1451(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1451()
        testdata = self.data['TH-CP-VM-0054']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)开启状态验证(开启状态下队列数输入框存在)
    @allure.title('<1-4-5多队列设置开关验证/开启状态验证')
    def test_creat_VM_page1452(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1452()
        testdata = self.data['TH-CP-VM1-0054']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-4-6队列数输入框验证
    #(1)队列数输入框默认值验证
    @allure.title('<1-4-6队列数输入框验证/队列数输入框默认值验证')
    def test_creat_VM_page1461(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1461()
        testdata = self.data['TH-CP-VM-0055']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    #(2)队列数输入框输入为空验证
    @allure.title('<1-4-6队列数输入框验证/队列数输入框输入为空验证')
    def test_creat_VM_page1462(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1462()
        testdata = self.data['TH-CP-VM-0056']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0][0]
        assert testdata['server2_num'] == pagedata[1]


    # (3)队列数输入框输入特殊字符验证
    @allure.title('<1-4-6队列数输入框验证/队列数输入框输入特殊字符验证')
    def test_creat_VM_page1463(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1463()
        testdata = self.data['TH-CP-VM-0057']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    #(4)队列数输入框输入大于2验证
    @allure.title('<1-4-6队列数输入框验证/队列数输入框输入大于2验证')
    def test_creat_VM_page1464(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1464()
        testdata = self.data['TH-CP-VM-0058']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    #(5)队列数输入框输入小于1验证
    @allure.title('<1-4-6队列数输入框验证/队列数输入框输入小于1验证')
    def test_creat_VM_page1465(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1465()
        testdata = self.data['TH-CP-VM-0059']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-4-7虚拟交换机下拉框验证
    # (1)虚拟交换机默认值验证
    @allure.title('<1-4-7虚拟交换机下拉框验证/虚拟交换机默认值验证')
    def test_creat_VM_page1471(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1471()
        testdata = self.data['TH-CP-VM-0060']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0]
        assert testdata['server2_num'] == pagedata[1]

    # (2)虚拟交换机下拉框选择值验证
    @allure.title('<1-4-7虚拟交换机下拉框验证/虚拟交换机下拉框选择值验证')
    def test_creat_VM_page1472(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1472()
        testdata = self.data['TH-CP-VM1-0060']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # QOS设置
    # 发送
    # <1-4-8发送速率输入框验证
    #(1)发送速率输入框默认值验证
    @allure.title('<1-4-8发送速率输入框验证/发送速率输入框默认值验证')
    def test_creat_VM_page1481(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1481()
        testdata = self.data['TH-CP-VM-0061']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)发送速率输入框输入为空验证
    @allure.title('<1-4-8发送速率输入框验证/发送速率输入框输入为空验证')
    def test_creat_VM_page1482(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1482()
        testdata = self.data['TH-CP-VM-0062']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (3)发送速率输入框输入特殊字符验证
    @allure.title('<1-4-8发送速率输入框验证/发送速率输入框输入特殊字符验证')
    def test_creat_VM_page1483(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1483()
        testdata = self.data['TH-CP-VM-0063']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    #(4)发送速率输入框输入大于4194303验证
    @allure.title('<1-4-8发送速率输入框验证/发送速率输入框输入大于4194303验证')
    def test_creat_VM_page1484(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1484()
        testdata = self.data['TH-CP-VM-0064']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    #(5)发送速率输入框输入小于0验证
    @allure.title('<1-4-8发送速率输入框验证/发送速率输入框输入小于0验证')
    def test_creat_VM_page1485(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1485()
        testdata = self.data['TH-CP-VM-0065']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-4-9发送峰值输入框验证
    # (1)发送峰值输入框默认值验证
    @allure.title('<1-4-9发送峰值输入框验证/发送峰值输入框默认值验证')
    def test_creat_VM_page1491(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1491()
        testdata = self.data['TH-CP-VM-0066']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)发送峰值输入框输入为空验证
    @allure.title('<1-4-9发送峰值输入框验证/发送峰值输入框输入为空验证')
    def test_creat_VM_page1492(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1492()
        testdata = self.data['TH-CP-VM-0067']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    #(3)发送峰值输入框输入特殊字符验证
    @allure.title('<1-4-9发送峰值输入框验证/发送峰值输入框输入特殊字符验证')
    def test_creat_VM_page1493(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1493()
        testdata = self.data['TH-CP-VM-0068']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)发送峰值输入框输入大于4194303验证
    @allure.title('<1-4-9发送峰值输入框验证/发送峰值输入框输入大于4194303验证')
    def test_creat_VM_page1494(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1494()
        testdata = self.data['TH-CP-VM-0069']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    #(5)发送峰值输入框输入小于0验证
    @allure.title('<1-4-9发送峰值输入框验证/发送峰值输入框输入小于0验证')
    def test_creat_VM_page1495(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page1495()
        testdata = self.data['TH-CP-VM-0070']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-4-10发送突发值输入框验证
    # (1)发送突发值输入框默认值验证
    @allure.title('<1-4-10发送突发值输入框验证/发送突发值输入框默认值验证')
    def test_creat_VM_page14101(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page14101()
        testdata = self.data['TH-CP-VM-0071']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)发送突发值输入框输入为空验证
    @allure.title('<1-4-10发送突发值输入框验证/发送突发值输入框输入为空验证')
    def test_creat_VM_page14102(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page14102()
        testdata = self.data['TH-CP-VM-0072']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (3)发送突发值输入框输入特殊字符验证
    @allure.title('<1-4-10发送突发值输入框验证/发送突发值输入框输入特殊字符验证')
    def test_creat_VM_page14103(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page14103()
        testdata = self.data['TH-CP-VM-0073']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)发送突发值输入框输入大于4194303验证
    @allure.title('<1-4-10发送突发值输入框验证/发送突发值输入框输入大于4194303验证')
    def test_creat_VM_page14104(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page14104()
        testdata = self.data['TH-CP-VM-0074']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (5)发送突发值输入框输入小于0验证
    @allure.title('<1-4-10发送突发值输入框验证/发送突发值输入框输入小于0验证')
    def test_creat_VM_page14105(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        pagedata = self.main.goto_serverpage().creat_VM_page14105()
        testdata = self.data['TH-CP-VM-0075']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # QOS设置
    # 接收
    # 切换到接收按钮验证
    @allure.title('<1-4-11切换到接收按钮验证验证')
    def test_creat_VM_page14110(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        self.main.goto_serverpage().creat_VM_page14110()

    # <1-4-11接收速率输入框验证
    # (1)接收速率输入框默认值验证
    @allure.title('<1-4-11接收速率输入框验证/接收速率输入框默认值验证')
    def test_creat_VM_page14111(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14111()
        testdata = self.data['TH-CP-VM-0061']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)接收速率输入框输入为空验证
    @allure.title('<1-4-11接收速率输入框验证/接收速率输入框输入为空验证')
    def test_creat_VM_page14112(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14112()
        testdata = self.data['TH-CP-VM-0062']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (3)接收速率输入框输入特殊字符验证
    @allure.title('<1-4-11接收速率输入框验证/接收速率输入框输入特殊字符验证')
    def test_creat_VM_page14113(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14113()
        testdata = self.data['TH-CP-VM-0063']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)接收速率输入框输入大于4194303验证
    @allure.title('<1-4-11接收速率输入框验证/接收速率输入框输入大于4194303验证')
    def test_creat_VM_page14114(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14114()
        testdata = self.data['TH-CP-VM-0064']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (5)接收速率输入框输入小于0验证
    @allure.title('<1-4-11接收速率输入框验证/接收速率输入框输入小于0验证')
    def test_creat_VM_page14115(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14115()
        testdata = self.data['TH-CP-VM-0065']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-4-12接收峰值输入框验证
    # (1)接收峰值输入框默认值验证
    @allure.title('<1-4-12接收峰值输入框验证/接收峰值输入框默认值验证')
    def test_creat_VM_page14121(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14121()
        testdata = self.data['TH-CP-VM-0066']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)接收峰值输入框输入为空验证
    @allure.title('<1-4-12接收峰值输入框验证/接收峰值输入框输入为空验证')
    def test_creat_VM_page14122(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14122()
        testdata = self.data['TH-CP-VM-0067']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (3)接收峰值输入框输入特殊字符验证
    @allure.title('<1-4-12接收峰值输入框验证/接收峰值输入框输入特殊字符验证')
    def test_creat_VM_page14123(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14123()
        testdata = self.data['TH-CP-VM-0068']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)接收峰值输入框输入大于4194303验证
    @allure.title('<1-4-12接收峰值输入框验证/接收峰值输入框输入大于4194303验证')
    def test_creat_VM_page14124(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14124()
        testdata = self.data['TH-CP-VM-0069']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (5)接收峰值输入框输入小于0验证
    @allure.title('<1-4-12接收峰值输入框验证/接收峰值输入框输入小于0验证')
    def test_creat_VM_page14125(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14125()
        testdata = self.data['TH-CP-VM-0070']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1-4-13接收突发值输入框验证
    # (1)接收突发值输入框默认值验证
    @allure.title('<1-4-13接收突发值输入框验证/接收突发值输入框默认值验证')
    def test_creat_VM_page14131(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14131()
        testdata = self.data['TH-CP-VM-0071']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)接收突发值输入框输入为空验证
    @allure.title('<1-4-13接收突发值输入框验证/接收突发值输入框输入为空验证')
    def test_creat_VM_page14132(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14132()
        testdata = self.data['TH-CP-VM-0072']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (3)接收突发值输入框输入特殊字符验证
    @allure.title('<1-4-13接收突发值输入框验证/接收突发值输入框输入特殊字符验证')
    def test_creat_VM_page14133(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14133()
        testdata = self.data['TH-CP-VM-0073']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (4)接收突发值输入框输入大于4194303验证
    @allure.title('<1-4-13接收突发值输入框验证/接收突发值输入框输入大于4194303验证')
    def test_creat_VM_page14134(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        # self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14134()
        testdata = self.data['TH-CP-VM-0074']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (5)接收突发值输入框输入小于0验证
    @allure.title('<1-4-13接收突发值输入框验证/接收突发值输入框输入小于0验证')
    def test_creat_VM_page14135(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page4()
        self.main.goto_serverpage().creat_VM_page14110()
        pagedata = self.main.goto_serverpage().creat_VM_page14135()
        testdata = self.data['TH-CP-VM-0075']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1 自定义
    # <1-5 高级配置页参数校验
    @allure.title('<1-5 高级配置页参数校验')  # 对模块子功能进行标注
    def test_creat_VM_page5(self):
        # self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page5()

    # <1-5-1光驱下拉框验证
    # (1)光驱下拉框默认为空验证
    @allure.title('<1-5-1光驱下拉框验证/光驱下拉框默认为空验证')
    def test_creat_VM_page1511(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1511()
        testdata = self.data['TH-CP-VM-0095']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0]
        assert testdata['server2_num'] == pagedata[1]

    # (2)光驱下拉框选择值验证
    @allure.title('<1-5-1光驱下拉框验证/光驱下拉框选择值验证')
    def test_creat_VM_page1512(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1512()
        testdata = self.data['TH-CP-VM-0096']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0]
        assert testdata['server2_num'] == pagedata[1]

    # <1-5-2软驱下拉框验证
    # (1)软驱下拉框默认为空验证
    @allure.title('<1-5-2软驱下拉框验证/软驱下拉框默认为空验证')
    def test_creat_VM_page1521(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1521()
        testdata = self.data['TH-CP-VM-0097']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0]
        assert testdata['server2_num'] == pagedata[1]

    # (2)软驱下拉框选择值验证
    @allure.title('<1-5-2软驱下拉框验证/软驱下拉框选择值验证')
    def test_creat_VM_page1522(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1522()
        testdata = self.data['TH-CP-VM-0098']
        print(pagedata)
        assert testdata['server1_num'] == pagedata[0]
        assert testdata['server2_num'] == pagedata[1]

    # <1-5-3显示选择项验证
    # (1)默认选择VGA验证(tabindex="0")
    @allure.title('<1-5-3显示选择项验证/默认选择VGA验证')
    def test_creat_VM_page1531(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1531()
        testdata = self.data['TH-CP-VM-0099']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择vGPU验证(tabindex="0")
    @allure.title('<1-5-3显示选择项验证/选择vGPU验证')
    def test_creat_VM_page1532(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1532()
        testdata = self.data['TH-CP-VM-0100']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-4高可用选择项验证
    # (1)默认选择ON验证(tabindex="0")
    @allure.title('<1-5-4高可用选择项验证/默认选择ON验证')
    def test_creat_VM_page1541(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1541()
        testdata = self.data['TH-CP-VM-0101']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (2)选择OFF验证(tabindex="0")
    @allure.title('<1-5-4高可用选择项验证/选择OFF验证')
    def test_creat_VM_page1542(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1542()
        testdata = self.data['TH-CP-VM-0102']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-5重要云服务器选择项验证
    # (1)默认选择中验证(tabindex="0")
    @allure.title('<1-5-5重要云服务器选择项验证/默认选择中验证')
    def test_creat_VM_page1551(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1551()
        testdata = self.data['TH-CP-VM-0103']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择高验证(tabindex="0")
    @allure.title('重要云服务器选择项验证/选择高验证')
    def test_creat_VM_page1552(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1552()
        testdata = self.data['TH-CP-VM-0104']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-6巨页内存选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-6巨页内存选择项验证/默认选择OFF验证')
    def test_creat_VM_page1561(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1561()
        testdata = self.data['TH-CP-VM-0105']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-6巨页内存选择项验证/选择ON验证')
    def test_creat_VM_page1562(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1562()
        testdata = self.data['TH-CP-VM-0106']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-7启动选择项验证
    # (1)默认选择BIOS验证(tabindex="0")
    @allure.title('<1-5-7启动选择项验证/默认选择BIOS验证')
    def test_creat_VM_page1571(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1571()
        testdata = self.data['TH-CP-VM-0107']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择UEFI验证(tabindex="0")
    @allure.title('<1-5-7启动选择项验证/选择UEFI验证')
    def test_creat_VM_page1572(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1572()
        testdata = self.data['TH-CP-VM-0108']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-8异常检测选择项验证
    # (1)默认选择ON验证(tabindex="0")
    @allure.title('<1-5-8异常检测选择项验证/默认选择ON验证')
    def test_creat_VM_page1581(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1581()
        testdata = self.data['TH-CP-VM-0109']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择OFF验证(tabindex="0")
    @allure.title('<1-5-8异常检测选择项验证/选择OFF验证')
    def test_creat_VM_page1582(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1582()
        testdata = self.data['TH-CP-VM-0110']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-9VNC选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-9VNC选择项验证/默认选择OFF验证')
    def test_creat_VM_page1591(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1591()
        testdata = self.data['TH-CP-VM-0111']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-9VNC选择项验证/选择ON验证')
    def test_creat_VM_page1592(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page1592()
        testdata = self.data['TH-CP-VM-0112']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-10内存安全选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-10内存安全选择项验证/默认选择OFF验证')
    def test_creat_VM_page15101(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15101()
        testdata = self.data['TH-CP-VM-0113']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-10内存安全选择项验证/选择ON验证')
    def test_creat_VM_page15102(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15102()
        testdata = self.data['TH-CP-VM-0114']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-11嵌套虚拟化选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-11嵌套虚拟化选择项验证/默认选择OFF验证')
    def test_creat_VM_page15111(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15111()
        testdata = self.data['TH-CP-VM-0115']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-11嵌套虚拟化选择项验证/选择ON验证')
    def test_creat_VM_page15112(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15112()
        testdata = self.data['TH-CP-VM-0116']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-12数据本地化选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-12数据本地化选择项验证/默认选择OFF验证')
    def test_creat_VM_page15121(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15121()
        testdata = self.data['TH-CP-VM-0117']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-12数据本地化选择项验证/选择ON验证')
    def test_creat_VM_page15122(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15122()
        testdata = self.data['TH-CP-VM-0118']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-13启用双活选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-13启用双活选择项验证/默认选择OFF验证')
    def test_creat_VM_page15131(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15131()
        testdata = self.data['TH-CP-VM-0119']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-13启用双活选择项验证/选择ON验证')
    def test_creat_VM_page15132(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15132()
        testdata = self.data['TH-CP-VM-0120']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-14绑定主资源池选择项验证
    # (1)默认选择OFF验证(tabindex="0")
    @allure.title('<1-5-14绑定主资源池选择项验证/默认选择OFF验证')
    def test_creat_VM_page15141(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15141()
        testdata = self.data['TH-CP-VM-0121']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # (2)选择ON验证(tabindex="0")
    @allure.title('<1-5-14绑定主资源池选择项验证/选择ON验证')
    def test_creat_VM_page15142(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15142()
        testdata = self.data['TH-CP-VM-0122']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    # <1-5-15启动配置选择项验证
    # (1)默认选择自动验证(tabindex="0")
    @allure.title('<1-5-15启动配置选择项验证/默认选择自动验证')
    def test_creat_VM_page15151(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15151()
        testdata = self.data['TH-CP-VM-0123']
        print(pagedata)
        assert testdata['server_num'] == pagedata

    #(2)选择主机验证(出现主机列表，存在栏位：”宿主机“)
    @allure.title('<1-5-15启动配置选择项验证/选择主机验证')
    def test_creat_VM_page15152(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15152()
        testdata = self.data['TH-CP-VM-0124']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # (3)选择标签验证(出现主机列表，存在栏位：”标签名称“)
    @allure.title('<1-5-15启动配置选择项验证/选择标签验证')
    def test_creat_VM_page15153(self):
        # self.main.goto_cserver()
        # self.main.goto_serverpage().creat_VM_page5()
        pagedata = self.main.goto_serverpage().creat_VM_page15153()
        testdata = self.data['TH-CP-VM-0125']
        print(pagedata)
        assert testdata['server_num'] == pagedata[0]

    # <1 自定义
    # <1-6 完成页参数校验
    @allure.title('完成页页参数校验')  # 对模块子功能进行标注
    def test_creat_VM_page6(self):
        # self.main.goto_cserver()
        self.main.goto_serverpage().creat_VM_page6()

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




