'''
    pytest框架规则：
        测试文件以test_开头，或者_test结尾
        1.测试类以Test开头，并且类中不能带有初始化方法（__init__）
        2.测试函数以test_开头
        3.断言使用基本的assert即可
'''
import pytest

def setup_model():
    print('作用于整个模块，适用于多个类')

def teardown_model():
    print('作用于整个模块，适用于多个类')

class aaacase01:
    age = 10
    def setup_class(self):
        print('类的前置条件,创建数据库连接')

    def teardown_class(self):
        print('类的后置条件,断开数据库连接')

    def setup(self):
        print('方法的前置条件，打开浏览器')

    def teardown(self):
        print('方法的后置条件，关闭浏览器')

    def test_01(self):
        print('第一条用例')
        assert 1 == 1

    @pytest.mark.run(order=1)  #调整执行顺序
    @pytest.mark.smoke         #mark标记(名字随便取)，需要在pytest.ini文件中设置
    @pytest.mark.skip(reason="环境不满足")   #跳过该条用例
    def test_02(self):
        print('第二条用例')
        assert 1 == 2

    @pytest.mark.smoke  # mark标记(名字随便取)，需要在pytest.ini文件中设置
    @pytest.mark.skip(age > 18 ,reason="环境满足")  # 条件满足，不跳过该条用例
    def test_03(self):
        print('第三条用例')
        assert 1 != 1


class Testcase02:
    def setup_class(self):
        print('类的前置条件')

    def teardown_class(self):
        print('类的后置条件')

    def setup(self):
        print('方法的前置条件，打开浏览器')

    def teardown(self):
        print('方法的后置条件，关闭浏览器')

    def test_01(self):
        print('第一条用例')
        assert 1 == 1

    def test_02(self):
        print('第二条用例')
        assert 1 == 2

    def test_03(self):
        print('第三条用例')
        assert 1 != 1


'''
    运行：
        1.mian pytest.main
        2.终端里边运行
    参数
        -v :打印详细的运行日志信息
        -s :带控制台输出结果
        -x :一旦发生错误就停止运行
        -k "类名 and not 方法名" :跳过运行某个用例
        pytest -m 标记名:只运行有这个标记的测试用例   (@pytest.mark.[标记名])
        
    修改规则：
        改.ini文件
          
'''


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'smoke', 'test_pytestway.py'])  #加了'-m', 'smoke'参数就只运行smoke标记的用例
