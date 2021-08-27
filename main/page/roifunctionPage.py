"""
@Project: WebTps_PoKeyword   
@Description: To local and control roi function page's elements
@Time:2021/7/9 9:46       
@Author:zexin                
 
"""
from time import sleep

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
#
# from main.page.counterPage import CounterPage
# from main.page.loginPage import LoginPage
# from main.page.patientPage import PatientPage
# from main.page.roitemplatePage import RoiTemplatePage
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml
from utils.Selector import structure_selector


class RoiFunctionPage(BasePage):
    element_config = ReadYaml("main\\page_data\\roifunctionPage.yaml")

    add_function_button = element_config['add_function_button']
    output_type_button = element_config['output_type_button']
    selectbox_button = element_config['selectbox_button']
    selectitem_button = element_config['selectitem_button']
    # input_box_button = element_config['']
    margin_input_box = element_config['margin_input_box']
    create_ring_checkbox = element_config['create_ring_checkbox']
    ring_size_inputbox = element_config['ring_size_inputbox']
    submit_button = element_config['submit_button']
    close_modal_button = element_config['close_modal_button']

    @allure.step("update roi by function: Expand")
    def update_roi_by_expand(self, yuan_roi_name, res_roi_name, expand_size):
        self.click("add_function_button", self.add_function_button, num=5, flag=0)
        self.sleep(2)
        self.click("roi_select_box", self.selectbox_button, num=4, flag=0)
        roi_select_item_selector = structure_selector(yuan_roi_name, self.element_config['selectitem_button'][1], self.element_config['selectitem_button'][2])
        yuan_select_item = (self.element_config['selectitem_button'][0], roi_select_item_selector)
        self.click("select_item", yuan_select_item)
        self.clear_and_input("margin_input_box", self.margin_input_box, expand_size)
        self.sleep(3)
        self.click("submit_button", self.submit_button, num=3, flag=0)
        self.sleep(2)
        self.click("close_button", self.close_modal_button, num=1, flag=0)
        self.sleep(2)
        self.click("output_type_button", self.output_type_button, num=0, flag=0)
        self.click("roi_list_select_box", self.selectbox_button, num=0, flag=0)
        roilist_select_item_selector = structure_selector(res_roi_name, self.element_config['selectitem_button'][1],
                                                      self.element_config['selectitem_button'][2])
        res_select_item = (self.element_config['selectitem_button'][0], roilist_select_item_selector)
        self.click("res_select_item", res_select_item)
        self.sleep(1)
        self.click("submit_button", self.submit_button, num=1, flag=0)
        self.sleep(20)

    @allure.step("update roi by function: Expand and Create ring")
    def expand_create_ring(self, yuan_roi_name, res_roi_name, expand_size, ring_size):
        self.click("add_function_button", self.add_function_button, num=5, flag=0)
        self.sleep(2)
        self.click("roi_select_box", self.selectbox_button, num=4, flag=0)
        roi_select_item_selector = structure_selector(yuan_roi_name, self.element_config['selectitem_button'][1],
                                                      self.element_config['selectitem_button'][2])
        yuan_select_item = (self.element_config['selectitem_button'][0], roi_select_item_selector)
        self.click("select_item", yuan_select_item)
        self.clear_and_input("margin_input_box", self.margin_input_box, expand_size)
        self.sleep(3)
        self.click("create_ring_checkbox", self.create_ring_checkbox, flag=0)
        self.clear_and_input("ring_size_inputbox", self.ring_size_inputbox, ring_size, flag=0)
        self.click("submit_button", self.submit_button, num=3, flag=0)
        self.sleep(2)
        self.click("close_button", self.close_modal_button, num=1, flag=0)
        self.sleep(2)
        self.click("output_type_button", self.output_type_button, num=0, flag=0)
        self.click("roi_list_select_box", self.selectbox_button, num=0, flag=0)
        roilist_select_item_selector = structure_selector(res_roi_name, self.element_config['selectitem_button'][1],
                                                          self.element_config['selectitem_button'][2])
        res_select_item = (self.element_config['selectitem_button'][0], roilist_select_item_selector)
        self.click("res_select_item", res_select_item)
        self.sleep(1)
        self.click("submit_button", self.submit_button, num=1, flag=0)
        self.sleep(20)

    def combine_subtract(self, goal1_name, goal2_name, res_roi_name):
        # 报错，目标二ring1找不到
        self.click("add_function_button", self.add_function_button, num=5, flag=0)
        self.sleep(2)
        self.click("function_type_selectbox", self.selectbox_button, num=3, flag=0)
        self.sleep(1)
        function_type_item = (By.XPATH, '//div[text()="Combine"]')
        self.click("function_type_item", function_type_item)
        self.sleep(1)
        self.click("goal1_selectbox", self.selectbox_button, num=4, flag=0)
        goal1_selectitem = structure_selector(goal1_name, self.element_config['selectitem_button'][1], self.element_config['selectitem_button'][2])
        goal1_selector = (self.element_config['selectitem_button'][0], goal1_selectitem)
        self.click("goal1_selectitem", goal1_selector)
        sleep(2)
        self.click("goal2_selectbox", self.selectbox_button, num=6, flag=0)
        self.sleep(1)
        goal2_selectitem = structure_selector(goal2_name, self.element_config['selectitem_button'][1],
                                              self.element_config['selectitem_button'][2])
        goal2_selector = (self.element_config['selectitem_button'][0], goal2_selectitem)
        self.click("goal2_selectitem", goal2_selector, flag=0)
        self.click("submit_button", self.submit_button, num=3, flag=0)
        self.sleep(2)
        self.click("close_button", self.close_modal_button, num=1, flag=0)
        self.sleep(2)
        self.click("output_type_button", self.output_type_button, num=0, flag=0)
        self.click("roi_list_select_box", self.selectbox_button, num=0, flag=0)
        roilist_select_item_selector = structure_selector(res_roi_name, self.element_config['selectitem_button'][1],
                                                          self.element_config['selectitem_button'][2])
        res_select_item = (self.element_config['selectitem_button'][0], roilist_select_item_selector)
        self.click("res_select_item", res_select_item)
        self.sleep(1)
        self.click("submit_button", self.submit_button, num=1, flag=0)
        self.sleep(20)


# if __name__ == '__main__':
#     driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
#     username = 'xzx'
#     password = '111111'
#     patient_name = "autotest_debug"
#     login_page = LoginPage(driver)
#     login_page.login(username, password)
#     sleep(5)
#     patient_page = PatientPage(driver)
#     patient_page.open_patient(patient_name)
#     sleep(10)
#     counter_page = CounterPage(driver)
#     # counter_page.enter_add_roi_by_template()
#     # roi_template_page = RoiTemplatePage(driver)
#     # roi_template_page.add_roi_by_template('Rectun_xzx')
#     # sleep(30)
#     counter_page.enter_roi_function()
#     sleep(2)
#     roi_function_page = RoiFunctionPage(driver)
#     #roi_function_page.expand_create_ring('PTV_Rectum', 'ring1', '1.5', '1')
#     roi_function_page.combine_subtract('Bladder', 'ring1', 'xxxx')
