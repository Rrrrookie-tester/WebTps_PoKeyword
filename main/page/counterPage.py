"""
@Project: WebTps_PoKeyword   
@Description: To local and control counter page's elements
@Time:2021/7/8 14:12       
@Author:zexin                
 
"""
import allure

from main.page.autosegmentationPage import AutoSegmentationPage
from main.page.ctDensityPage import CTDensityPage
from main.page.planPage import PlanPage
from main.page.registrationPage import RegistrationPage
from main.page.roitemplatePage import RoiTemplatePage
from utils.ReadYaml import ReadYaml
from utils.BasePage import BasePage
from utils.Selector import structure_selector


class CounterPage(BasePage):
    element_config = ReadYaml("main\\page_data\\counterPage.yaml")

    plan_module_button = element_config['module_button']
    auto_segmentation_button = element_config['operate_button']
    add_roi_by_template_button = element_config['operate_button']
    roi_function_button = element_config['operate_button']
    ct_density_button = element_config['ct_density_button']

    @allure.step("switch to registration page")
    def switch_to_registration(self):
        self.click("registration_module_button", self.plan_module_button, num=1)
        self.sleep(3)
        registration_page = RegistrationPage(self.driver)
        return registration_page

    @allure.step("switch to plan page")
    def switch_to_plan(self):
        self.click("plan_module_button", self.plan_module_button, num=2)
        self.sleep(3)
        plan_page = PlanPage(self.driver)
        return plan_page

    @allure.step("open auto segmentation page")
    def enter_auto_segmentation(self):
        self.click("auto_segmentation_button", self.auto_segmentation_button, num=5)
        self.sleep(1)
        autosegmentation_page = AutoSegmentationPage(self.driver)
        return autosegmentation_page

    @allure.step("open add ROI by template page")
    def enter_add_roi_by_template(self):
        # 100服务器上按钮序号为8， 98服务器上序号为7
        # self.click("add_roi_by_template_button", self.add_roi_by_template_button, num=8)
        self.click("add_roi_by_template_button", self.add_roi_by_template_button, num=7)
        self.sleep(1)
        roi_template_page = RoiTemplatePage(self.driver)
        return roi_template_page

    @allure.step("open roi function page")
    def enter_roi_function(self):
        self.click("roi_function_button", self.roi_function_button, num=9)
        self.sleep(1)

    @allure.step("switch series")
    def switch_series(self, series_name):
        series_selector = structure_selector(series_name, self.element_config['series_button'][1], self.element_config['series_button'][2])
        series_button = (self.element_config['series_button'][0], series_selector)
        self.double_click("series:%s" % series_name, series_button)
        self.sleep(5)

    @allure.step("open CTDensity page")
    def enter_ct_density(self):
        self.click("ct_density_button", self.ct_density_button)
        self.sleep(1)
        ct_density_page = CTDensityPage(self.driver)
        return ct_density_page
