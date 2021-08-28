"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/28 10:26       
@Author:zexin                
 
"""
import allure

from main.page.carMainPage import CarMainPage
from utils.BasePage import BasePage
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml


class CarLoginPage(BasePage):
    logger = Logger("CarLoginPage.py").getlog()
    ED = ReadYaml("main\\page_data\\axxxxe.yaml")

    @allure.step("login")
    def login(self, usn, pwd):
        self.open()
        self.max_window()
        self.input("username_input", self.ED['username_input'], usn)
        self.input("password_input", self.ED['password_input'], pwd)
        self.click("login_button", self.ED['login_button'])
        car_main_page = CarMainPage(self.driver)
        return car_main_page
