"""
@Project: WebTps_PoKeyword   
@Description: Test Chest auto segmentation
@Time:2021/7/14 10:49       
@Author:zexin                
 
"""
from time import sleep

import allure
import pytest
from selenium import webdriver

from main.page.loginPage import LoginPage
from utils.Logger import Logger


@allure.feature("chest autoSegment")
@pytest.mark.autoSegment
# @pytest.mark.debugAutoSegment
class TestAutoSegmentationChest:
    logger1 = Logger("chestAutoSegmentation").getlog()

    @classmethod
    def setup_method(cls):
        cls.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'autotester01'
        password = '10retsetotua'
        patient_name = "AT_AS_Chest"

        cls.login_page = LoginPage(cls.driver)
        cls.patient_page = cls.login_page.login(username, password)
        sleep(10)
        cls.counter_page = cls.patient_page.open_patient(patient_name)
        cls.logger1.info("open patient: %s " % patient_name)
        sleep(10)

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()

    @allure.story("auto segment on chest series")
    # @pytest.mark.parametrize('series_name', ['CT'])
    @pytest.mark.parametrize('series_name', ['CT', 'CT1', 'CT2', 'CT3', 'CT4', 'CT5', 'CT6', 'CT7', 'CT8', 'CT9', 'CT10',
                                             'CT11', 'CT12', 'CT13', 'CT14'])
    def test_chest_auto_segmentation(self, series_name):
        self.logger1.info("start auto segment on series: %s" % series_name)
        self.counter_page.switch_series(series_name)
        self.logger1.info("switch to series: %s " % series_name)
        sleep(10)
        autosegmentation_page = self.counter_page.enter_auto_segmentation()
        self.logger1.info("open auto segmentation page")
        # try:
        #     result = autosegmentation_page.autosegment_chest()
        # except:
        #     self.logger1.error("series: %s auto segmentation failed !" % series_name)
        result = autosegmentation_page.autosegment_chest()
        assert result, self.logger1.error("series: %s auto segmentation failed !" % series_name)


if __name__ == '__main__':
    pytest.main(['-s', 'test_autosegmentation_chest.py', '--alluredir=../result/test_registration'])