"""
@Project: WebTps_PoKeyword   
@Description: To local and control add optimization constraints page's elements
@Time:2021/7/31 11:19       
@Author:zexin                
 
"""
import allure

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class AddOptimizationConstraints(BasePage):
    ED = ReadYaml("main\\page_data\\addOptimizationConstraintsPage.yaml")

    @allure.step("create optimization constraints")
    def create_optimization_constraints(self, roi_name, func_type, dose, is_weak, weights, a=0, volume=0):
        self.select("roi_select", self.ED['roi_select_box'], self.ED['roi_select_item'], roi_name, num=1)
        self.select("function_type_select", self.ED['func_type_select_box'], self.ED['func_type_select_item'], func_type, num=2)
        self.clear_and_input("dose_input", self.ED['dose_input'], dose)
        if func_type == '最大EUD' or func_type == '最小EUD':
            self.clear_and_input("EUD_a_input", self.ED['eud_a_input'], a)
        elif func_type == '最大DVH' or func_type == '最小DVH':
            self.clear_and_input("DVH_volume_input", self.ED['dvh_volume_input'], volume)
        if is_weak:
            self.click("weak_constraint_radio", self.ED['weak_constraint_radio'], num=-1)
        self.clear_and_input("weights_input", self.ED['weights_input'], weights)
        self.click("submit_button", self.ED['submit_button'], num=-1)
        self.sleep(1)

    @allure.step("close optimization constraint")
    def close_optimization_constraint_page(self):
        self.click("close_optimization_constraint_page_button", self.ED['close_button'])
        self.sleep(1)


