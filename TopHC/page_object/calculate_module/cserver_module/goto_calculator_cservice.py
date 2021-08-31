
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from TopHC.base.basepage import BasePage

class Cal_Cservice(BasePage):
    #从首页进入计算模块-->云服务器页面
    def goto_cal_cserver(self):
        element = self.find(By.XPATH, '//*[@id="navBar_item_计算_content"]')
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()
        self.find(By.XPATH, '//*[@id="navBar_item_计算_content_云服务器"]/span').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="tab-vmlist"]').click()





    #方法一：参数驱动
    '''
    def goto_calculator(self):
        sleep(2)
        #return self.find(By.XPATH,'//*[@id="panel-c-scroll"]/div[1]/section/section/div/div[1]/section[1]/div/div[1]/div/div[2]/div/div[1]/span').text
        return self.steps(r"D:/WorkTools/PyProjects/TopHC/page_object/calculate_module/goto_calculator_cservice.yaml")
        #return self.find(By.ID, "overview_nav_container").click()


    #方法二：元素定位操作

        code = self.find(By.ID, "login_confirm")
        action = ActionChains(self.driver)
        action.move_to_element(code)
        action.perform() #鼠标悬停后才会出现的元素，然后找到该元素，正常定位即可
        sleep(2)
        self.find(By.XPATH, '//*[@id="navBar_item_计算_content_云服务器"]/span').click()
        sleep(2)
        return self.find(By.XPATH, '//*[@id="tab-vmlist"]').text
        sleep(3)
'''

