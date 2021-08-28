"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/28 11:44       
@Author:zexin                
 
"""
import allure
import pytest
from selenium import webdriver

from main.page.carLoginPage import CarLoginPage
from utils.Logger import Logger
from utils.SQLHelper.SQLManager import SQLManager


@allure.feature("TestCar")
class TestCar:
    logger1 = Logger("TestCar").getlog()

    def get_car_data(self, plate):
        sql = 'select * from test1 where name = "%s"' % plate
        sql_manager = SQLManager()
        car_data = sql_manager.query_all(sql)
        return car_data

    def get_plate_data(self):
        sql = "select name from test1"
        sql_manager = SQLManager()
        plate_data = sql_manager.query_all(sql)
        return plate_data

    def save_sql(self, plate, data):
        inspection_items1 = data[0]
        inspection_items2 = data[1]
        picture_list = data[2]
        sql = 'update test1 set a = "%s", b = "%s", c = "%s" where plate = "%s"' %(inspection_items1, inspection_items2, picture_list, plate)
        sql_manager = SQLManager()
        sql_manager.edit(sql)

    plate_result = get_plate_data()

    @pytest.mark.parametrize('data', plate_result)
    def test_car(self, data):
        car_data = self.get_car_data(data)
        driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'test'
        password = '123456'
        car_login_page = CarLoginPage(driver)
        car_main_page = car_login_page.login(username, password)
        car_main_page.show_all()
        car_main_page.perfect_information(car_data)
        car_result_page = car_main_page.submit()
        car_result_page.screenShot()
        download_data = car_result_page.download()
        self.save_sql(download_data)

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()

