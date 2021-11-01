from TopHC.base.main import Main


class Test_HomePage:
    def setup(self):
        self.main = Main(driver=None)


    # 1.首页页面信息检查测试用例
    #测试点1：检查首页是否存在对应文字
    '''
    @pytest.mark.parametrize("value1, value2",yaml.safe_load(open("./test_search_text.yaml")))
    def test_search_text(self,value1,value2):
        self.main.goto_main_searchUI().search_text()
        #assert "健康" == self.main.goto_main_searchUI().search_text()
        print(value1)
    '''

    def test_search_text(self):
        rr = self.main.goto_home_searchUI().search_text1()
        print(rr)
        #assert "集群状态" == rr


    #测试点2：


    # 2.首页功能验证测试用例

    # 测试点1:添加云容器入口
    # 点击首页中云容器按钮，出现创建云容器弹窗（验证是否创建云容器成功）
    def test_add_rongqi(self):
        self.main.goto_home_functionAdd_cloud_container().add_cloud_container()
        #断言1：出现请求成功的提示
        #断言2：云容器列表存在创建的容器

    # 测试点2：添加云服务器入口
        def test_add_yunfuwuqi(self):
            pass
        # 断言1：出现请求成功的提示
        # 断言2：云服务器列表存在创建的容器

    # 测试点3：添加云硬盘入口
    def test_add_yunpan(self):
        pass
        # 断言1：出现请求成功的提示
        # 断言2：云硬盘列表存在创建的容器

    # 测试点4：网络拓扑页面入口
    def test_nettopu(self):
        pass
        # 断言1：正常跳转至网络--网络拓扑页面



