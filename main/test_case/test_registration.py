"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/9 14:23       
@Author:zexin                
 
"""
from time import sleep

import pytest
from selenium import webdriver

from main.page.loginPage import LoginPage
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml


class TestRegistration:
    logger = Logger("TestRegistration").getlog()

    def registration(self, registration_data):
        username = 'xzx'
        password = '111111'
        patient_name = registration_data[0]
        series_path = registration_data[1]
        series_num = registration_data[2]
        self.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')

        login_page = LoginPage(self.driver)
        self.logger.info("user: %s login " % username)
        patient_page = login_page.login(username, password)
        sleep(5)
        # ----添加创建患者、导入序列步骤----
        # self.logger.info("create patient: %s " % patient_name)
        # new_patient_page = patient_page.enter_new_patient()
        # new_patient_page.new_patient(patient_name)
        # self.logger.info("import series ")
        # import_page = patient_page.enter_import(patient_name)
        # import_page.import_from_local(series_path)
        # ----添加创建患者、导入序列步骤----
        self.logger.info("open patient: %s " % patient_name)
        counter_page = patient_page.open_patient(patient_name)
        sleep(10)
        self.logger.info("switch to registration page")
        registration_page = counter_page.switch_to_registration()
        rigid_list = []
        for i in range(0, series_num):
            for j in range(0, series_num):
                if i != j:
                    if i == 0:
                        fixed_ct_name = 'CT'
                        float_ct_name = 'CT' + str(j)
                    elif j == 0:
                        fixed_ct_name = 'CT' + str(i)
                        float_ct_name = 'CT'
                    else:
                        fixed_ct_name = 'CT' + str(i)
                        float_ct_name = 'CT' + str(j)
                    self.logger.info("add rigid registration,fixed_ct:%s;float_ct:%s" % (fixed_ct_name, float_ct_name))
                    rigid = registration_page.add_rigid_registration(fixed_ct_name, float_ct_name)
                    rigid_list.append(rigid)
        self.logger.info("show rigid registration tree")
        registration_page.show_registration_tree(series_num)
        for rigid in rigid_list:
            self.logger.info("add nonrigid registration: non%s" % rigid)
            registration_page.add_nonrigid_registration(rigid)

    registration_config = ReadYaml("main\\test_data\\registration_normal.yaml")

    @pytest.mark.parametrize('registration_config', registration_config)
    def test_registration(self, registration_config):
        self.registration(registration_config)


if __name__ == '__main__':
    pytest.main(['-s', 'test_registration.py'])
