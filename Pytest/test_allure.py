#allure测试报告
#1.allure测试报告的生成
'''
import pytest

def test_success():
    assert True

def test_failure():
    assert False

def test_skip():
    pytest.skip('for a reason')

def test_broken():
    raise Exception('oops')

#方法一：生成网页版测试报告（关闭后无法保存）
#D:\Pyprojects\project01\Package02>pytest test_allure.py --alluredir=./result/01
#>allure serve ./result/01

#方法二：生成可保存的测试报告
#D:\Pyprojects\project01\Package02>pytest test_allure.py --alluredir=./result/01
#>allure generate ./result/01 -o ./report/01 --clean
#>allure open -h 127.0.0.1 -p 8884 ./report/01




#2.allure特性分析
#2.1希望在测试报告中看到测试功能，子功能或场景，测试步骤，包括测试附加信息
import pytest
import allure

@allure.feature('登录模块')    #对模块功能进行标注
class Test_login():
    @allure.story('登录成功')  ##对模块子功能进行标注
    def test_login_success_a(self):
        print('这是登录1：测试用例，登录成功')
        pass

    @allure.story('登录成功')
    def test_login_success_b(self):
        print('这是登录2：测试用例，登录成功')
        pass

    @allure.story('用户名缺失')
    def test_login_failure_a(self):
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    def test_login_failure_b(self):
        with allure.step('点击用户名'):   #对测试步骤进行标记
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('点击登录之后登录失败'):
            assert '1' == 1
            print('登录失败')
        pass

    @allure.story('登录失败')
    def test_login_failure_c(self):
        print('这是登录2：测试用例，登录失败')
        pass



#2.2测试报告用例结果中加入链接
import allure

#@allure.link('https://www.baidu.com/')
@allure.link('https://www.baidu.com/',name='百度')
def test_with_link():
    print('这是一条加了链接的测试用例')
    pass



#2.2测试报告用例结果中加入TP上该用例的具体地址
import allure

TEST_CASE_LINK = 'https://www.baidu.com/'
@allure.testcase(TEST_CASE_LINK,'登录测试用例001的id')
def test_with_testcase_link():
    print('这是一条测试用例的链接，链接到该用例的具体测试步骤')
    pass



#2.3测试报告用例结果中加入TD上该用例对应的bug的具体地址
import allure

# --allure-link-pattern=issue:https://www.baidu.com/{}  #对应的TD链接
@allure.issue('59561','登录测试用例001的对应的bug')         #bugID，传入上面的括号里
def test_with_issue_link():
    print('这是一条测试用例对应的bug链接，链接到该用例对应的bug')
    pass



#2.4希望按重要性级别来分别执行用例
import pytest
import allure

def test_with_trivial_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)  #此用例标记为不重要,轻微缺陷
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)  #此用例标记为正常问题，普通缺陷
def test_with_normal_severity():
    pass

@allure.feature('登录模块')    #对模块功能进行标注
@allure.severity(allure.severity_level.NORMAL)  #此模块标记为正常问题，普通缺陷
class Test_login():
    @allure.story('登录成功')  ##对模块子功能进行标注
    def test_login_success_a(self):
        print('这是登录1：测试用例，登录成功')
        pass

    @allure.story('登录成功')
    def test_login_success_b(self):
        print('这是登录2：测试用例，登录成功')
        pass

    @allure.story('用户名缺失')
    @allure.severity(allure.severity_level.CRITICAL)  # 此用例标记为严重，临界缺陷
    def test_login_failure_a(self):
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    def test_login_failure_b(self):
        with allure.step('点击用户名'):   #对测试步骤进行标记
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('点击登录之后登录失败'):
            assert '1' == 1
            print('登录失败')
        pass

    @allure.story('登录失败')
    def test_login_failure_c(self):
        print('这是登录2：测试用例，登录失败')
        pass

if __name__ == '__main__':
    pytest.main()

#D:\Pyprojects\project01\Package02>pytest -s -v test_allure.py --alluredir=./result/06  --allure-severities  normal,critical
#>allure generate ./result/06 -o ./report/06 --clean
#>allure open -h 127.0.0.1 -p 8884 ./report/06
'''

#2.5希望在测试报告中添加图片或html
import allure

#在测试报告里附加纯文本
def test_attach_text():
    allure.attach('这是一个纯文本',attachment_type=allure.attachment_type.TEXT)

#在测试报告里附加网页
def test_attach_html():
    allure.attach('<head></head>这是一段html/body块<body></body>','这是html测试的结果信息',allure.attachment_type.HTML)

#在测试报告里附加图片
def test_attach_photo():
    allure.attach.file('./result/test.png',name='这是一张图片',attachment_type=allure.attachment_type.PNG)

#在测试报告里附加视频
def test_attach_mp4():
    allure.attach.file('./result/test.mp4',name='这是一段视频',attachment_type=allure.attachment_type.MP4)