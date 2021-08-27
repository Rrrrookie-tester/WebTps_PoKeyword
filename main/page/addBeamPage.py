"""
@Project: WebTps_PoKeyword   
@Description: To local and control add beam page's elements
@Time:2021/7/30 9:57       
@Author:zexin                
 
"""
import allure

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class AddBeamPage(BasePage):
    ED = ReadYaml("main\\page_data\\addBeamPage.yaml")

    @allure.step("add beam")
    def add_beam(self, beam_name, voi_name, irradiation_mode, dose_rate, beam_angle, arc_length):
        self.input("beam_name_input", self.ED['beam_name_input'], beam_name)
        self.select("voi_select", self.ED['voi_select_box'], self.ED['voi_select_item'], voi_name)
        self.select("irradiation_mode_select", self.ED['irradiation_mode_select'], self.ED['irradiation_mode_item'],
                    irradiation_mode)
        self.select("dose_rate_select", self.ED['dose_rate_select'], self.ED['dose_rate_item'], dose_rate)
        if arc_length != 0:
            self.clear_and_input("beam_arc_angle_input", self.ED['arc_beam_angle_input'], beam_angle)
            self.clear_and_input("beam_arc_length_input", self.ED['arc_length_input'], arc_length)
        else:
            self.clear_and_input("beam_angle_input", self.ED['beam_angle_input'], beam_angle)
        self.click("add_beam_submit_button", self.ED['submit_button'], num=-1)
        self.sleep(1)


