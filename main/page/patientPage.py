"""
@Project: WebTps_PoKeyword   
@Description: To local and control patient page's elements
@Time:2021/7/8 12:11       
@Author:zexin                
 
"""
from main.page.counterPage import CounterPage
from main.page.importPage import ImportPage
from main.page.newPatientPage import NewPatientPage
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class PatientPage(BasePage):
    element_config = ReadYaml("main\\page_data\\patientPage.yaml")

    patient_name_input = element_config['patient_name_input']
    search_button = element_config['search_button']
    select_patient = element_config['select_patient']
    counter_button = element_config['counter_button']
    new_patient_button = element_config['new_patient_button']

    def open_patient(self, patient_name):
        self.input("patient_name_input", self.patient_name_input, string=patient_name, flag=20)
        self.click("search_button", self.search_button)
        self.sleep(1)
        self.double_click("select_patient", self.select_patient)
        self.click("counter_button", self.counter_button, num=9, flag=5)
        counter_page = CounterPage(self.driver)
        return counter_page

    def enter_new_patient(self):
        self.click("new_patient_button", self.new_patient_button, num=0)
        self.sleep(2)
        new_patient_page = NewPatientPage(self.driver)
        return new_patient_page

    def enter_import(self, patient_name):
        self.input("patient_name_input", self.patient_name_input, string=patient_name, flag=20)
        self.click("search_button", self.search_button)
        self.sleep(1)
        self.double_click("select_patient", self.select_patient)
        self.click("import_button", self.counter_button, num=17, flag=5)
        self.sleep(2)
        import_page = ImportPage(self.driver)
        return import_page