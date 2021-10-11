import os


class Filepath:
    '''
    定义一个Filepath类,用来获取文件路径
    1.自动传入data.yaml文件的路劲并读取数据
    2.获取yaml文件中各组数据并返回
    '''
    #获取当前项目的绝对路径
    BasePath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/../..')
    #获取数据yaml文件所在绝对路径
    DataPath = BasePath + '\TopHCAPI\data'
    #获取测试用例文件所在路径
    TestPath = BasePath + r'\TopHCAPI\test_case'
    #日志文件所在路径
    LogPath = BasePath + '\TopHCAPI\log'
    #HTML报告所在路径
    ReportPath = BasePath + r'\TopHCAPI\report'

    #各模块测试数据路径
    #1.首页模块
    #2.1.1登录页面
    #（1）测试步骤数据
    LoginDataPath = DataPath + '\pageapi_data\home_module_data\loginapi.yaml'
    #（2）测试用例数据
    LoginTestDataPath = DataPath + r'\test_data\home_module_data\loginapitest.yaml'
    #（3）测试用例
    LoginTestPath = TestPath + r'\home_module\test_homemodule.py'

    # 2.1.1概览页面
    # （1）测试步骤数据
    HomeDataPath = DataPath + r'\pageapi_data\home_module_data\homeapi.yaml'
    # （2）测试用例数据
    HomeTestDataPath = DataPath + r'\test_data\home_module_data\home_module\hometest.yaml'
    # （3）测试用例
    HomeTestPath = TestPath + r'\home_module\test_homemodule.py'


    #2.计算模块
    #2.1 云服务器模块
    #2.1.1云服务器页面
    #（1）测试步骤数据
    ServerDataPath = DataPath + '\page_data\calculate_module_data\cserver_module\serverdata.yaml'
    #（2）测试用例数据
    ServerTestDataPath = DataPath + r'\test_data\calculate_module_data\cserver_module\servertest.yaml'
    #（3）测试用例
    ServerTestPath = TestPath + r'\calculate_module\test_cservermodule.py'

    #2.1.2 模板页面
    #（1）测试步骤数据
    MouldDataPath = DataPath + '\page_data\calculate_module_data\cserver_module\moulddata.yaml'
    #（2）测试用例数据
    MouldTestPath = DataPath + r'\test_data\calculate_module_data\cserver_module\mouldtest.yaml'
    #（3）测试用例

    # 2.1.3 规格页面
    #（1）测试步骤数据
    SpecsDataPath = DataPath + '\page_data\calculate_module_data\cserver_module\specsdata.yaml'
    #（2）测试用例数据
    SpecsTestPath = DataPath + r'\test_data\calculate_module_data\cserver_module\specstest.yaml'
    # 2.1.4 备份页面
    #（1）测试步骤数据
    BackupDataPath = DataPath + r'\page_data\calculate_module_data\cserver_module\backupdata.yaml'
    #（2）测试用例数据
    BackupTestPath = DataPath + r'\test_data\calculate_module_data\cserver_module\backuptest.yaml'
    # 2.1.5 策略页面
    #（1）测试步骤数据
    StrategyDataPath = DataPath + r'\page_data\calculate_module_data\cserver_module\strategydata.yaml'
    #（2）测试用例数据
    StrategyTestPath = DataPath + r'\test_data\calculate_module_data\cserver_module\strategytest.yaml'

    # 2.2 VDI桌面模块
    # 2.2.1 桌面页面
    # （1）测试步骤数据
    DesktopDataPath = DataPath
    # （2）测试用例数据
    DesktopTestPath = DataPath
    # 2.2.2 桌面池页面
    # （1）测试步骤数据
    DesktopPoolDataPath = DataPath
    # （2）测试用例数据
    DesktopPoolTestPath = DataPath
    # 2.2.3 模板页面
    # （1）测试步骤数据
    DesktopMouldDataPath = DataPath
    # （2）测试用例数据
    DesktopMouldTestPath = DataPath
    # 2.2.4 个性化页面
    # （1）测试步骤数据
    PersonalDataPath = DataPath
    # （2）测试用例数据
    PersonalTestPath = DataPath

    # 2.3 终端模块

    # 2.4 云容器模块

    # 2.5 裸金属模块

    # 2.6 云容器模块
    # 2.6.1 云容器页面
    # （1）测试步骤数据
    CcontainerDataPath = DataPath
    # （2）测试用例数据
    CcontainerTestPath = DataPath
    # 2.6.1 密钥页面
    # （1）测试步骤数据
    CiperDataPath = DataPath
    # （2）测试用例数据
    CiperTestPath = DataPath
    # 2.6.1 配置页面
    # （1）测试步骤数据
    DeployDataPath = DataPath
    # （2）测试用例数据
    DeployTestPath = DataPath


    #3.存储模块


    #4.网络模块


    #5.应用模块


    #6.镜像模块


    #7.功能模块
    #7.1标签模块
    #2.1.1标签页面
    #（1）测试步骤数据
    LabelDataPath = DataPath + r'\pageapi_data\functional_module_data\label_module\labelapi.yaml'
    #（2）测试用例数据
    LabelTestDataPath = DataPath + r'\test_data\functional_module_data\label_module\labelapi.yaml'
    #（3）测试用例
    LabelTestPath = TestPath + r'\functional_module\test_labelmodule.py'

    #7.2任务模块
    # 7.2.1任务页面
    # （1）测试步骤数据
    TaskDataPath = DataPath + '\pageapi_data\home_module_data\loginapi.yaml'
    # （2）测试用例数据
    TaskTestDataPath = DataPath + r'test_data\home_module_data\logintest.yaml'
    # （3）测试用例
    TaskTestPath = TestPath + r'\home_module\test_homemodule.py'


    #8.运营模块


    #9.运维模块


    #10.系统模块







#实例化Filepath类并赋值给readFilepath,后面可直接调用readFilepath
readFilepath=Filepath()
