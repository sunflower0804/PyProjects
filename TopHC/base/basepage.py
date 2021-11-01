# 封装所有界面都公用的属性和方法：例如driver、find_element等
import component as component
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from TopHC.others.log import logs



class BasePage():
    # 共同属性
    _driver = None  # 类变量，需要在类函数之前进行赋值
    _base_url = ''

    # __init__:父类的构造方法，子类执行之前首先会去调用执行父类的构造方法
    def __init__(self, driver: WebDriver = None):  # driver的类型为 WebDriver = None
        # 这里如果不对参数进行初始化会报错：TypeError: __init__() missing 1 required positional argument: 'driver'
        # 定义页面基础类时，初始化webdiver，传参数的时候没有对参数driver赋默认None值，即一个默认参数，导致页面报错如下：
        # 传人默认参数，在调用self.main=Main()时，就可以不传入参数了(或者直接在调用时传入默认参数初始值self.main=Main(WebDriver = None))
        # 且不指定浏览器驱动类型时，后面调用时定位元素会出问题
        if driver is None:  # 如果外面没有对driver进行传值（即第一次调用），那么就对driver进行初始化
            options = Options()  # 使用 selenium 时，我们可能需要对 chrome 做一些特殊的设置，以完成我们期望的浏览器行为，比如阻止图片加载，阻止JavaScript执行 等动作。这些需要 selenium的 ChromeOptions 来帮助我们完成
            options.debugger_address = '127.0.0.1:9500'  # 开启浏览器调试模式：cmd命令窗口输入： chrome  --remote-debugging-port=端口1（随便取），回车
            self._driver = webdriver.Chrome(options=options)
            sleep(2)
            # 加入隐式等待时间
            # 弊端：全局生效，但只要找到元素不管有没有完全加载就继续下一步，这样会造成操作失败
            #self._driver.implicitly_wait(10)
            # 解决办法:使用显示等待
        else:
            self._driver = driver  # 后面每次有方法调用self._driver时，都是初始化之后的driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    # 共同方法
    # 1、元素定位+显示等待
    def find(self, *loc):
        '''元素显示等待'''
        locs = loc
        aa = tuple(locs)
        try:
            ele = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(aa))
            return ele
        except Exception as e:
            print('{0}元素未找到'.format(loc[1]))


    def finds(self, *loc, index):
        '''显示存在，只要元素存在目标'''
        locs = loc
        aa = tuple(locs)
        try:
            ele = WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located(aa))
            return ele[index]
        except Exception as e:
            print('{0}元素{1}未找到'.format(loc[1], [index]))

    def check_element_exist(self, by, loc):
        '''判断元素是否存在'''
        locs = (by, loc)   #将传入的参数转换为元组
        try:
            ele = WebDriverWait(self._driver, 1).until(EC.visibility_of_element_located(locs))
            result = ele.is_displayed()
            return result   #存在返回True
        except:
            return False

    # 2、输入框输入
    def send(self, *loc, value):
        '''输入值，自动先调用显示等待'''
        self.find(*loc).send_keys(value)
        logs.info('在{0}元素中，输入了{1}'.format(loc[1], value))

    # 3、点击按钮
    def click(self, *loc):
        '''点击，自动先调用显示等待'''
        self.find(*loc).click()
        logs.info('点击了{0}元素'.format(loc[1]))

    def clicks(self, *loc, index):
        '''点击，自动先调用显示等待'''
        self.finds(*loc, index).click()
        logs.info('点击了{0}元素'.format(loc[1]))

    # 4、鼠标移动
    def move_mouse(self, *loc):
        '''移动鼠标至指定元素'''
        ele = self.find(*loc)
        ActionChains(self._driver).move_to_element(ele).perform()
        logs.info('鼠标光标移动至{0}元素'.format(loc[1]))

    def move_and_click(self, *loc):
        '''移动鼠标至指定位置并点击'''
        ele = self.find(*loc)
        ActionChains(self._driver).move_to_element(ele).click().perform()
        logs.info('鼠标光标移动至{0}元素并点击'.format(loc[1]))

    def move_to_offset(self):
        '''移动鼠标至指定坐标'''
        coordinates = (100, 100)
        ActionChains(self._driver).move_by_offset(*coordinates).click().perform()
        logs.info('移动鼠标至坐标{0}'.format(coordinates))

    # 5、获取文本
    def text(self, *loc, attr= 'placeholder'):
        '''获取元素属性值信息'''
        div = self.find(*loc)
        text = div.get_attribute(attr)
        logs.info('元素文本信息为{0}'.format(text))
        return text

    def texts(self, *loc, index):
        '''获取元素属性值信息，当元素为元素组时'''
        div = self.finds(*loc, index)
        texts = div.get_attribute('innerText')
        logs.info('元素文本信息为{0}'.format(texts))
        return texts

    def input_text(self, *loc):
        '''获取输入框/下拉框中输入的值'''
        input = self.find(*loc)
        value = input.get_attribute('value')
        logs.info('元素文本信息为{0}'.format(value))
        return value

    # 6、键盘操作
    def keys_choose_all(self):
        '''键盘操作:control a :输入框文本全部选中'''
        ActionChains(self._driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        logs.info('键盘操作:control a')

    def keys_delete(self):
        '''键盘操作Backspace: 删除'''
        ActionChains(self._driver).send_keys(Keys.BACK_SPACE).perform()
        logs.info('键盘操作:Backspace')

    def keys_send(self, value):
        ActionChains(self._driver).send_keys(value).perform()
        logs.info('键盘输入:{0}'.format(value))

    def clear_books(self, *loc):
        '''清除输入框内容'''
        self.find(*loc).send_keys(Keys.CONTROL, 'a')
        self.find(*loc).send_keys(Keys.BACK_SPACE)
        logs.info('键盘输入后清理')

    def keys_PageDown(self):
        '''键盘操作方向键：向下翻页'''
        ActionChains(self._driver).send_keys(Keys.PAGE_DOWN).perform()
        logs.info('键盘操作:向下翻页')

    # 7、表单切换
    def switch_iframe(self, *loc):
        return self._driver.switch_to.frame(self.find(*loc))

    # 8、窗口切换封装
    def switch_window(self, n):
        return self._driver.switch_to.window(self._driver.window_handles[n])

    # 9、测试步骤驱动:yaml文件数据解析
    # def steps(self, path):  # path为yaml文件路径
    #     with open(path) as f:  # 打开yaml文件
    #         steps = yaml.safe_load(f)  # 加载yaml文件
    def steps(self, data):  # path为yaml文件路径
        texts = []
        for step in data:  # 对yaml文件进行遍历，以便执行多个动作
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            else:
                element = None

            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    sleep(1)
                    element.click()
                if action == "send":
                    #self.send(step["by"], step["locator"], value=step["value"])
                    element.click()
                    sleep(1)      #未加等待时间时会导致输入的字符被清除
                    #element.set_value(step["value"])
                    element.send_keys(step["value"])
                if action == "clear":
                    self.clear_books(step["by"], step["locator"])
                if action == "text":
                    # element.text
                    texts.append(element.text)
        return texts

    def quit(self):
        '''浏览器退出'''
        self._driver.quit()


    #日志截图

'''
    #出现闪现的提示信息，定位方法如下：
    # 操作步骤：
    # 因为闪退弹窗速度比较快，需要按如下步骤操作：
    # 1)在打开的浏览器中按F12 ，选择Sources；
    # 2)操作触发弹窗步骤；
    # 3) 鼠标按下暂停图标（pause） 或快捷键（Ctrl +\），这样弹窗就暂停了，不会闪退了（这里如果动作慢也可能定位不到，就需要重复步骤2）和3）了）;
    # 4)再选Elements,鼠标选中弹窗内容就可以定位了

    #定位悬浮元素
    def test_moveto_code(self):
        sleep(2)
        #定位到悬浮位置
        code = self.find(By.XPATH,'//*[@id="_hmt_click"]/div[2]/div[1]/div[6]/div[1]/span')
        action = ActionChains(self._driver)
        action.move_to_element(code)
        action.perform() #鼠标悬停后才会出现的元素，然后找到该元素，正常定位即可
        self.find(By.XPATH,'//*[@id="copyDownload"]').click()  #悬停出现的文本内容“复制下载链接”的超链接,并点击
        return self.find(By.XPATH,'//*[@id="js_tips"]').text
'''

