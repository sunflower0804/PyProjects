from TopEC.others.filepath import readFilepath
from TopEC.others.yamlexcelload import loadyaml




# @pytest.mark.parametrize("items", loadyaml(filepath))

def test_search_clusterUI1():
    filepath = readFilepath.ServerTestPath
    data = loadyaml(filepath)
    testdata = data['TH-CP-CLUSTER-0006']['data01']
    # pagedata = self.main.goto_serverpage().search_clustersUI1()
    # assert testdata['cluster1'] == pagedata[0]
    # assert testdata['cluster2'] == pagedata[1]
    print(testdata)
    #print(testdata[0]['cluster1'])
