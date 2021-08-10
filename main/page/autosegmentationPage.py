"""
@Project: WebTps_PoKeyword   
@Description: To local and control auto segmentation page's elements
@Time:2021/7/8 14:32       
@Author:zexin                
 
"""
import re
from time import sleep

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class AutoSegmentationPage(BasePage):
    element_config = ReadYaml("main\\page_data\\autosegmentationPage.yaml")

    head_neck_button = element_config["head_neck_button"]
    other_button = element_config["other_button"]
    cavumpelvis_button = element_config["cavumpelvis_button"]
    chest_button = element_config["chest_button"]
    abdomen_button = element_config["abdomen_button"]
    all_select_button = element_config["all_select_button"]
    move_button = element_config["move_button"]
    submit_button = element_config["submit_button"]

    roi_color = element_config["roi_color"]

    def autosegment_cavumpelvis(self):
        self.click("cavumpelvis_button", self.cavumpelvis_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        sleep(2)
        self.click("other_button", self.other_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        self.click("submit_button", self.submit_button)
        sleep(60)
        roi_colors = self.locations("roi_color", self.roi_color)
        for roi_color in roi_colors:
            text = roi_color.get_attribute()
            if "none" in text:
                return False

    def autosegment_chest(self):
        self.click("chest_button", self.chest_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        sleep(2)
        self.click("other_button", self.other_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        self.click("submit_button", self.submit_button)
        sleep(60)
        roi_colors = self.locations("roi_color", self.roi_color)
        for roi_color in roi_colors:
            text = roi_color.get_attribute()
            if "none" in text:
                return False

    def autosegment_headNeck(self):
        self.click("head_neck_button", self.head_neck_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        sleep(2)
        self.click("other_button", self.other_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        self.click("submit_button", self.submit_button)
        sleep(60)
        roi_colors = self.locations("roi_color", self.roi_color)
        for roi_color in roi_colors:
            text = roi_color.get_attribute()
            if "none" in text:
                return False

    def autosegment_abdomen(self):
        self.click("abdomen_button", self.abdomen_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        sleep(2)
        self.click("other_button", self.other_button)
        sleep(1)
        self.click("all_select_button", self.all_select_button)
        self.click("move_button", self.move_button)
        self.click("submit_button", self.submit_button)
        sleep(60)
        roi_colors = self.locations("roi_color", self.roi_color)
        for roi_color in roi_colors:
            text = roi_color.get_attribute()
            if "none" in text:
                return False


