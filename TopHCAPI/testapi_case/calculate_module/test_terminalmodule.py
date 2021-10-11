import pytest
import yaml

from TopHC.base.main import Main


class TestSearchUI:
    def setup(self):
        self.main = Main(driver=None)

    # 2.1.1.2云服务器模块UI信息检查
    # 1-1.集群目录结构信息校验
    # (1)检查每个集群下目录信息
    '''
    前置条件：
    1、测试环境存在集群cluster1、cluster2
    2、存在租户zh1, 已添加cluster1、cluster2下的资源池
    3、租户zh1在cluster1、cluster2下分别存在云服务器vm1、vm2

    操作步骤：
    1、登录企业云系统当前租户选择zh1
    2、进入计算 - -云服务器首页
    3、检查集群信息列表
    4、检查对应集群下的云服务器信息

    预期结果：
    3、集群信息列表中存在集群cluster1、cluster2，对应集群名称显示正确
    4、cluster1中存在云服务器vm1、cluster1中存在云服务器vm1，对应云服务器名称显示正确
    '''
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open(
        "cserver_module/test_search_text1.yaml")))
    def test_search_text(self, value1, value2):
        #tt = self.main.goto_cal_cserver_searchUI().search_clusters1()
        print(value1)
        print(value2)
        #assert value1 == tt[0]
        #assert value2 == tt[1]

        #print(value1),value1,value2
    #def test_search_text2(self):
        #self.main.goto_cal_cserver_searchUI().search_clusters2()



