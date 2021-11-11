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
    DataPath = BasePath + '\TopHCS\data'
    #获取测试用例文件所在路径
    TestPath = BasePath + r'\TopHCS\test_case'
    #日志文件所在路径
    LogPath = BasePath + '\TopHCS\log'
    # 报错截图路径
    ImagePath = BasePath + r'\TopHCS\images'
    #HTML报告所在路径
    ReportPath = BasePath + r'\TopHCS\report'

    #各模块测试数据路径
    #浏览器驱动路径
    DriverPath = BasePath + '\TopHCS\others\driver'

    #0.登录模块
    # 0.1 登录页面
    # （1）测试步骤数据
    LoginDataPath = DataPath + '\page_data\login_module\login.yaml'
    # # （2）测试用例数据
    # LoginTestDataPath = DataPath + r'\test_data\hmoe_module_data\home_module\logintest.yaml'
    # # （3）测试用例
    # LoginTestPath = TestPath + r'\calculate_module\test_loginpage.py'

    #1.首页模块

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
    MouldTestDataPath = DataPath + r'\test_data\calculate_module_data\cserver_module\mouldtest.yaml'
    #（3）测试用例
    MouldTestPath = TestPath + r'\calculate_module\test_cservermodule.py'

    # 2.1.3 规格页面
    #（1）测试步骤数据
    SpecsDataPath = DataPath + '\page_data\calculate_module_data\cserver_module\specsdata.yaml'
    #（2）测试用例数据
    SpecsTestDataPath = DataPath + r'\test_data\calculate_module_data\cserver_module\specstest.yaml'
    #（3）测试用例
    SpecsTestPath = TestPath + r'\calculate_module\test_cservermodule.py'
    # 2.1.4 备份页面
    #（1）测试步骤数据
    BackupDataPath = DataPath + r'\page_data\calculate_module_data\cserver_module\backupdata.yaml'
    #（2）测试用例数据
    BackupTestDataPath = DataPath + r'\test_data\calculate_module_data\cserver_module\backuptest.yaml'
    #（3）测试用例
    BackupTestPath = TestPath + r'\calculate_module\test_cservermodule.py'
    # 2.1.5 策略页面
    #（1）测试步骤数据
    StrategyDataPath = DataPath + r'\page_data\calculate_module_data\cserver_module\strategydata.yaml'
    #（2）测试用例数据
    StrategyTestDataPath = DataPath + r'\test_data\calculate_module_data\cserver_module\strategytest.yaml'
    #（3）测试用例
    StrategyTestPath = TestPath + r'\calculate_module\test_cservermodule.py'

    # 2.2 云容器模块
    # 2.2.1 云容器页面
    # （1）测试步骤数据
    CcontainerDataPath = DataPath + r'\page_data\calculate_module_data\cloudcontainer_module\ccontainerdata.yaml'
    # （2）测试用例数据
    CcontainerTestDataPath = DataPath
    #（3）测试用例
    CcontainerTestPath = TestPath + r'\calculate_module\test_ccontainermodule.py'
    # 2.2.2 密钥页面
    # （1）测试步骤数据
    CiperDataPath = DataPath + r'\page_data\calculate_module_data\cloudcontainer_module\cipher.yaml'
    # （2）测试用例数据
    CiperTestDataPath = DataPath
    #（3）测试用例
    CiperTestPath = TestPath + r'\calculate_module\test_ccontainermodule.py'

    # 2.2.3 配置页面
    #（1）测试步骤数据
    DisposeDataPath = DataPath + r'\page_data\calculate_module_data\cloudcontainer_module\dispose.yaml'
    #（2）测试用例数据
    DisposeTestDataPath = DataPath
    #（3）测试用例
    DisposeTestPath = TestPath + r'\calculate_module\test_ccontainermodule.py'





    #8.运营模块

    #8.2 计费模块
    #8.2.1账单页面
    #8.2.2规格页面
    SpeciDataPath = DataPath + '\page_data\operation_module_data\cost_module\specidata.yaml'
    #（2）测试用例数据
    SpeciTestDataPath = DataPath + r'\test_data\operation_module_data\cost_module\specitest.yaml'
    #（3）测试用例
    SpeciTestPath = TestPath + r'\operation_module\test_costmodule.py'

    #10.系统模块
    #10.1 配置模块
    #2.1.1配置页面
    #（1）测试步骤数据
    ConfigureDataPath = DataPath + '\page_data\system_module\configure_module\configuredata.yaml'
    #（2）测试用例数据
    ConfigureTestDataPath = DataPath + r'\test_data\system_module_data\configure_module\configuretest.yaml'
    #（3）测试用例
    ConfigureTestPath = TestPath + r'\system_module\test_configuremodule.py'


#实例化Filepath类并赋值给readFilepath,后面可直接调用readFilepath
readFilepath=Filepath()
