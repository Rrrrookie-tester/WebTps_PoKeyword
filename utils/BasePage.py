"""
@Project: WebTps_PoKeyword   
@Description: To package common operate function
@Time:2021/7/8 9:18       
@Author:zexin                
 
"""
import traceback
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.Logger import Logger
from utils.Selector import structure_selector
from utils.ListLog import list_log


class ReadYaml(object):
    pass


class BasePage:
    logger = Logger("BasePage.py").getlog()

    # 初始化

    def __init__(self, driver):
        #config_data = ReadYaml("data\\config.yaml")
        #self.base_url = config_data['base_url']
        self.base_url = "http://10.8.77.100:10010/emr/data-center"
        # self.base_url = "http://10.8.77.98:10010/emr/data-center"
        self.driver = driver
        self.timeout = 30

    # 定义打开登录页面方法
    def _open(self):
        try:
            url = self.base_url
            self.driver.get(url)
            self.logger.info("open %s succeed !" % url)
        except:
            self.logger.error("open %s error !" % url)
            self.logger.debug(traceback.format_exc())
            quit()
        # url = self.base_url
        # self.driver.get(url)

    def open(self):
        self._open()

    def quit(self):
        self.driver.quit()
        quit()

    def max_window(self):
        try:
            self.driver.maximize_window()
            self.logger.info("max window succeed !")
        except:
            self.logger.error("max window error !")
            self.logger.debug(traceback.format_exc())
            self.quit()

    def local(self, element_name, loc, num, flag):
        # flag 0shibuxuyaojinxing xianshidengdai
        # try:
        #     if flag:
        #         WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        #         return self.driver.find_elements(*loc)[num]
        #     else:
        #         return self.driver.find_elements(*loc)[num]
        #     self.logger.info("local %s succeed !" % element_name)
        # except:
        #     self.logger.error("local %s error !" % element_name)
        #     self.logger.debug("selector:" + list_log(loc))
        #     self.logger.debug(traceback.format_exc())
        #     self.quit()
        try:
            if flag != 0:
                WebDriverWait(self.driver, flag).until(EC.visibility_of_element_located(loc))
                return self.driver.find_elements(*loc)[num]
            else:
                return self.driver.find_elements(*loc)[num]
            self.logger.info("local %s succeed !" % element_name)
        except:
            self.logger.error("local %s error !" % element_name)
            self.logger.debug("selector:" + list_log(loc))
            self.logger.debug(traceback.format_exc())
            self.quit()

    def location(self, element_name, loc, num=0):
        try:
            return self.driver.find_elements(*loc)[num]
        except:
            self.logger.error("local %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def locations(self, element_name, loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            self.logger.error("local %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def click(self, element_name, loc, num=0, flag=0):
        try:
            self.local(element_name, loc, num, flag).click()
            self.logger.info("click %s succeed !" % element_name)
        except:
            self.logger.error("click %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def select(self, element_name, box_loc, item_loc, item_feature, num=0, flag=0):
        try:
            self.local(element_name, box_loc, num, flag).click()
            self.logger.info("click %s box succeed !" % element_name)
        except:
            self.logger.error("click %s box error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()
        try:
            sleep(0.5)
            element_name_item = element_name + '_item'
            selector = structure_selector(item_feature, item_loc[1], item_loc[2])
            location = (item_loc[0], selector)
            num = 0
            self.local(element_name_item, location, num, flag).click()
            self.logger.info("click %s succeed !" % element_name_item)
        except:
            self.logger.error("click %s error !" % element_name_item)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def clear_and_input(self, element_name, loc, string, num=0, flag=0):
        try:
            element = self.local(element_name, loc, num, flag)
            element.send_keys(Keys.CONTROL, 'a')
            element.send_keys(string)
            self.logger.info("send %s to %s succeed !" % (string, element_name))
        except:
            self.logger.error("send %s to %s error !" % (string, element_name))
            self.logger.debug(traceback.format_exc())
            self.quit()

    def input(self, element_name, loc, string, num=0, flag=0):
        try:
            self.local(element_name, loc, num, flag).send_keys(string)
            self.logger.info("send %s to %s succeed !" % (string, element_name))
        except:
            self.logger.error("send %s to %s error !" % (string, element_name))
            self.logger.debug(traceback.format_exc())
            self.quit()

    def double_click(self, element_name, loc, num=0):
        try:
            ac = ActionChains(self.driver)
            ac.double_click(self.location(element_name, loc, num)).perform()
            self.logger.info("double click %s succeed !" % element_name)
        except:
            self.logger.error("double click %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def move(self, element_name, loc, num=0, flag=0):
        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.local(element_name, loc, num, flag)).perform()
            self.logger.info("move to element: %s succeed !" % element_name)
        except:
            self.logger.error("move to %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def go_mark(self, element_name, x, y):
        try:
            ac = ActionChains(self.driver)
            ac.move_by_offset(x, y).click().perform()
            self.logger.info("move to element: %s succeed !" % element_name)
        except:
            self.logger.error("move to mark %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def element_disappear(self, element_name, loc, num=0):
        # 等待元素消失后返回true,仍存在遗留bug
        try:
            self.sleep(0.3)
            if WebDriverWait(self.driver, 120).until(EC.staleness_of(self.driver.find_elements(*loc)[num])):
                self.logger.info("element: %s disappeared !" % element_name)
                self.sleep(1)
                return True
        except:
            self.logger.error("wait element: %s disappear error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    def right_click(self, element_name, loc, num=0):
        try:
            ac = ActionChains(self.driver)
            ac.context_click(self.location(element_name, loc, num)).perform()
            self.logger.info("right click %s succeed !" % element_name)
        except:
            self.logger.error("right click %s error !" % element_name)
            self.logger.debug(traceback.format_exc())
            self.quit()

    # def can_click(self, element_name, loc, flag):
    #     button = WebDriverWait(self.driver, flag).until(EC.element_to_be_clickable(loc))
    #     self.logger.info("%s can be clicked" % element_name)
    #     button.click()
    #     self.logger.info("click %s succeed !" % element_name)
    #     # self.logger.error("wait and click: %s error !" % element_name)
    #     # self.logger.debug(traceback.format_exc())
    #     # self.quit()

    def sleep(self, time):
        sleep(time)





