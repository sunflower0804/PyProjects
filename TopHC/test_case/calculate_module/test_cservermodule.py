import allure
import pytest

from TopHC.base.main import Main
from TopHC.others.filepath import readFilepath
from TopHC.others.yamlexcelload import loadyaml


@allure.feature('计算-->云服务器模块')   #对模块功能进行标注
@allure.story('云服务器子模块')  ##对模块子功能进行标注
class TestServicePage:
    def setup_class(self):
        self.main = Main(driver=None)

    # 2.1.1云服务器模块功能验证
    # 1-1-1.云服务器/集群信息导航栏信息校验
    # (1)集群目录信息校验
    '''
    TEST_CASE_LINK = 'https://www.kdocs.cn/p/129592400066'
    @allure.testcase(TEST_CASE_LINK, '用例_编号：TH-CP-CLUSTER-0001')
    # --allure-link-pattern=issue:https://www.baidu.com/{}  #对应的TD链接
    @allure.issue('59561', '测试用例对应的bugID')  # bugID，传入上面的括号里
    @allure.title('集群目录结构信息校验')  #对模块子功能进行标注
    '''

    path = readFilepath.CserverTestPath
    @pytest.mark.parametrize("items", loadyaml(path))
    def test_search_clusterUI1(self, items):
        tt = self.main.goto_serverpage().search_clustersUI1()
        assert items['cluster1'] == tt[0]
        assert items['cluster2'] == tt[1]




    # 2.1.2 模板模块功能验证
    def test_search_clusterUI21(self):
        self.main.goto_cmouldpage().search_clustersUI21()

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




