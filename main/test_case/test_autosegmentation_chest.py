"""
@Project: WebTps_PoKeyword   
@Description: Test Chest auto segmentation
@Time:2021/7/14 10:49       
@Author:zexin                
 
"""
from time import sleep

import pytest
from selenium import webdriver

from main.page.autosegmentationPage import AutoSegmentationPage
from main.page.counterPage import CounterPage
from main.page.loginPage import LoginPage
from main.page.patientPage import PatientPage
from utils.Logger import Logger


class TestAutoSegmentationChest:
    logger1 = Logger("chestAutoSegmentation").getlog()

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '111111'
        patient_name = "AutoTest_Chest_AutoSegmentation"

        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login(username, password)
        sleep(5)
        cls.patient_page = PatientPage(cls.driver)
        cls.patient_page.open_patient(patient_name)
        cls.logger1.info("open patient: %s " % patient_name)
        sleep(10)
        cls.counter_page = CounterPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('series_name', ['CT', 'CT1', 'CT2', 'CT3', 'CT4', 'CT5', 'CT6', 'CT7', 'CT8', 'CT9', 'CT10',
                                             'CT11', 'CT12', 'CT13', 'CT14'])
    def test_chest_auto_segmentation(self, series_name):
        self.counter_page.switch_series(series_name)
        self.logger1.info("switch to series: %s " % series_name)
        sleep(10)
        self.counter_page.enter_auto_segmentation()
        self.logger1.info("open auto segmentation page")
        autosegmentation_page = AutoSegmentationPage(self.driver)
        try:
            result = autosegmentation_page.autosegment_chest()
        except:
            self.logger1.error("series: %s auto segmentation failed !" % series_name)
        assert result, self.logger1.error("series: %s auto segmentation failed !" % series_name)


if __name__ == '__main__':
    pytest.main(['-s', 'test_autosegmentation_chest.py'])