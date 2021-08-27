"""
@Project: WebTps_PoKeyword   
@Description: To local and control ct to density page's elements
@Time:2021/7/23 9:42       
@Author:zexin                
 
"""
import allure

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class CTDensityPage(BasePage):
    element_config = ReadYaml("main\\page_data\\ctDensityPage.yaml")

    density_select_box = element_config['density_select_box']
    density_select_item = element_config['density_select_item']
    submit_button = element_config['submit_button']

    @allure.step("set CTDensity")
    def select_density(self):
        self.click("density_select_box", self.density_select_box)
        self.sleep(0.5)
        self.click("density_select_item", self.density_select_item)
        self.sleep(1)
        self.click("submit_button", self.submit_button)

