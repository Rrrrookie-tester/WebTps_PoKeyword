"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/9 9:57       
@Author:zexin                
 
"""
# from time import sleep
#
# from selenium import webdriver
#
# from main.page.counterPage import CounterPage
# from main.page.loginPage import LoginPage
# from main.page.patientPage import PatientPage
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml
from utils.Selector import structure_location


class RegistrationPage(BasePage):
    ED = ReadYaml("main\\page_data\\registrationPage.yaml")

    def add_rigid_registration(self, fixed_ct, float_ct):
        self.double_click("fixed_ct: %s" % fixed_ct, structure_location(fixed_ct, self.ED['series_button']))
        # if self.element_disappear("progress_bar", self.ED['progress_bar'], num=-1):
        #     self.right_click("float_ct: %s" % float_ct, structure_location(float_ct, self.ED['series_button']))
        self.sleep(10)
        self.right_click("float_ct: %s" % float_ct, structure_location(float_ct, self.ED['series_button']))
        self.click("add_rigid_button", self.ED['add_rigid_button'], flag=3)
        if self.element_disappear("progress_bar", self.ED['progress_bar']):
            self.click("rigid_saveAs_button", self.ED['rigid_function_button'], num=6)
        registration_name = "Rigid_" + fixed_ct + "_" + float_ct
        self.clear_and_input("registration_name_input", self.ED['registration_name_input'], registration_name, flag=3)
        self.click("submit_button", self.ED['submit_button'], num=-1)
        if self.element_disappear("progress_bar", self.ED['progress_bar'], num=-1):
            return registration_name

    def show_registration_tree(self, num):
        buttons = []
        for n in range(0, num):
            button = self.location("show_tree_node_button", self.ED['show_tree_node_button'], num=n)
            buttons.append(button)
        for button in buttons:
            button.click()
            self.sleep(0.5)
        self.sleep(1)

    def add_nonrigid_registration(self, rigid_name):
        self.right_click('rigid: %s' % rigid_name, structure_location(rigid_name, self.ED['series_button']))
        self.click("add_nonrigid_button", self.ED['add_nonrigid_button'], flag=3)
        if self.element_disappear("progress_bar", self.ED['progress_bar'], num=-1):
            self.click("start_nonrigid_button", self.ED['nonrigid_function_button'], num=1)
        if self.element_disappear("progress_bar", self.ED['progress_bar'], num=-1):
            self.click("save_nonrigid_button", self.ED['nonrigid_function_button'], num=2)
        self.element_disappear("progress_bar", self.ED['progress_bar'], num=-1)


# if __name__ == '__main__':
    # driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
    # username = 'xzx'
    # password = '111111'
    # patient_name = "autotest_0809"
    # login_page = LoginPage(driver)
    # login_page.login(username, password)
    # sleep(5)
    # patient_page = PatientPage(driver)
    # patient_page.open_patient(patient_name)
    # sleep(10)
    # counter_page = CounterPage(driver)
    # counter_page.switch_to_registration()
    # registration_page = RegistrationPage(driver)
    # rigid_list = []
    # for i in range(0, 3):
    #     for j in range(0, 3):
    #         if j != i:
    #             if i == 0:
    #                 fixed_ct_name = 'CT'
    #                 float_ct_name = 'CT' + str(j)
    #             elif j == 0:
    #                 fixed_ct_name = 'CT' + str(i)
    #                 float_ct_name = 'CT'
    #             else:
    #                 fixed_ct_name = 'CT' + str(i)
    #                 float_ct_name = 'CT' + str(j)
    #             rigid = registration_page.add_rigid_registration(fixed_ct_name, float_ct_name)
    #             rigid_list.append(rigid)
    #     print(rigid_list)
    # registration_page.show_registration_tree(3)
    # for rigid in rigid_list:
    #     registration_page.add_nonrigid_registration(rigid)
    #
    # sleep(30)