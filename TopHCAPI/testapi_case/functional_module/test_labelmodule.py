from TopHCAPI.others.filepath import readFilepath
from TopHCAPI.others.yamlexcelload import loadyaml
from TopHCAPI.pageapi.functional_module.labelapi import LabelApi


class TestLabelApi:
    def setup(self):
        self.labelapi = LabelApi()

    filepath = readFilepath.LabelTestDataPath
    data = loadyaml(filepath)

    # 1.标签类型
    # 1.1创建标签类型
    def test_addlabel(self):
        testdata = self.data['TH-CP-LABEL-0001']
        res = self.labelapi.add_label()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res) #获取创建标签类型返回值

    # 1.4删除标签类型
    def test_dellabel(self):
        testdata = self.data['TH-CP-LABEL-0001']
        res = self.labelapi.add_label()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res) #获取创建标签类型返回值

    # 2.标签
    #2.1创建标签
    def test_addtag(self):
        testdata = self.data['TH-CP-LABEL-0001']
        res = self.labelapi.add_label()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res) #获取创建标签类型返回值

    #2.2查询标签
    def test_gettag(self):
        testdata = self.data['TH-CP-LABEL-0001']
        res = self.labelapi.add_label()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res) #获取创建标签类型返回值

    #2.3修改标签
    def test_updatetag(self):
        testdata = self.data['TH-CP-LABEL-0001']
        res = self.labelapi.add_label()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res) #获取创建标签类型返回值

    #2.4删除标签
    def test_deltag(self):
        testdata = self.data['TH-CP-LABEL-0001']
        res = self.labelapi.add_label()
        assert res['scode'] == testdata['scode']
        assert res['message'] == testdata['message']
        print(res) #获取创建标签类型返回值