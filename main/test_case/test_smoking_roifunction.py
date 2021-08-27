"""
@Project: WebTps_PoKeyword   
@Description: To smoking roi function
@Time:2021/8/3 9:17       
@Author:zexin                
 
"""
from time import sleep

from selenium import webdriver

from main.page.counterPage import CounterPage
from main.page.ctDensityPage import CTDensityPage
from main.page.loginPage import LoginPage
from main.page.patientPage import PatientPage


class TestSmokingROIFunction:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '111111'
        patient_name = cls.roi_config[0]

        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login(username, password)
        sleep(5)
        cls.patient_page = PatientPage(cls.driver)
        cls.patient_page.open_patient(patient_name)
        cls.logger1.info("open patient: %s " % patient_name)
        sleep(10)
        cls.counter_page = CounterPage(cls.driver)
        cls.counter_page.switch_series(cls.roi_config[1])
        cls.logger1.info("select series: %s", cls.roi_config[1])
        cls.counter_page.enter_ct_density()
        cls.ct_density_page = CTDensityPage(cls.driver)
        cls.ct_density_page.select_density()
        cls.logger1.info("update CTDensity to 'Default Template'")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_expand_subtract_ring(self):
        pass

