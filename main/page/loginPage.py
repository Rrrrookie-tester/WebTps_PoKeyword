"""
@Project: WebTps_PoKeyword   
@Description: To local and control login page's elements
@Time:2021/7/8 9:49       
@Author:zexin                
 
"""
from main.page.patientPage import PatientPage
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class LoginPage(BasePage):
    element_config = ReadYaml("main\\page_data\\loginPage.yaml")

    username_input = element_config["username_input"]
    password_input = element_config["password_input"]
    login_button = element_config["login_button"]

    def login(self, une, pwd):
        self.open()
        self.max_window()
        self.input("username_input", self.username_input, une, flag=1)
        self.input("password_input", self.password_input, pwd, flag=1)
        self.click("login_button", self.login_button, flag=1)
        patient_page = PatientPage(self.driver)
        return patient_page
