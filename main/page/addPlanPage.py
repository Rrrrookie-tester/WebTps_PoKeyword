"""
@Project: WebTps_PoKeyword   
@Description: To local and control add plan page's elements
@Time:2021/7/28 9:37       
@Author:zexin                
 
"""
import allure

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml
from utils.Selector import structure_selector


class AddPlanPage(BasePage):
    element_config = ReadYaml("main\\page_data\\addPlanPage.yaml")

    plan_name_input = element_config['plan_name_input']
    ng_name_input = element_config['ng_name_input']
    machine_select_box = element_config['machine_select_box']
    machine_select_item = element_config['machine_select_item']
    radiation_type_box = element_config['radiation_type_box']
    radiation_type_item = element_config['radiation_type_item']
    technology_type_box = element_config['technology_type_box']
    technology_type_item = element_config['technology_type_item']
    fraction_input = element_config['fraction_input']
    single_dose_input = element_config['single_dose_input']
    prescription_percentage_input = element_config['prescription_percentage_input']
    beamGroupGoal_roiPropertiesId_box = element_config['beamGroupGoal_roiPropertiesId_box']
    beamGroupGoal_roiPropertiesId_item = element_config['beamGroupGoal_roiPropertiesId_item']
    radio_button = element_config['radio_button']
    beamGroupGoal_doseVolume_input = element_config['beamGroupGoal_doseVolume_input']
    submit_button = element_config['submit_button']

    @allure.step("add plan and Ng")
    def create_plan_ng(self, plan_name, ng_name, machine, radiation_type, technology_type, fraction, single_dose,
                       prescription_percentage, beamGroupGoal_roiPropertiesId, doseVolume):
        self.clear_and_input("plan_name_input", self.plan_name_input, plan_name)
        self.clear_and_input("ng_name_input", self.ng_name_input, ng_name)
        self.click("machine_select_box", self.machine_select_box, num=2)
        selector = structure_selector(machine, self.machine_select_item[1], self.machine_select_item[2])
        location = (self.machine_select_item[0], selector)
        self.click("machine_select_item", location)
        self.select("radiation_type", self.radiation_type_box, self.radiation_type_item, radiation_type, 3)
        self.select("technology_type", self.technology_type_box, self.technology_type_item, technology_type, num=4)
        self.clear_and_input("fraction_input", self.fraction_input, fraction)
        self.clear_and_input("single_dose_input", self.single_dose_input, single_dose)
        self.clear_and_input("prescription_percentage_input", self.prescription_percentage_input, prescription_percentage)
        self.click("radio_button", self.radio_button)
        self.select("beamGroupGoal_roiPropertiesId", self.beamGroupGoal_roiPropertiesId_box,
                    self.beamGroupGoal_roiPropertiesId_item, beamGroupGoal_roiPropertiesId)
        self.clear_and_input("beamGroupGoal_doseVolume_input", self.beamGroupGoal_doseVolume_input, doseVolume)
        self.click("submit_button", self.submit_button, num=1)




