"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/4 17:52       
@Author:zexin                
 
"""
import allure

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class NewPatientPage(BasePage):
    ED = ReadYaml("main\\page_data\\newPatientPage.yaml")

    @allure.step("new patient")
    def new_patient(self, p_name):
        self.input("new_patient_name_input", self.ED['new_patient_name_input'], p_name)
        self.click("submit_button", self.ED['submit_button'])
        self.sleep(1)
