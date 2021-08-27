"""
@Project: WebTps_PoKeyword   
@Description: To local and control auto segmentation page's elements
@Time:2021/7/8 14:32       
@Author:zexin                
 
"""
import re
from time import sleep

import allure

from utils.BasePage import BasePage
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml


class AutoSegmentationPage(BasePage):
    logger = Logger("autoSegmentation.py").getlog()
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
    auto_segment_result = element_config['auto_segment_result']

    @allure.step("autoSegment(cavumPelvis)")
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
            text = roi_color.get_attribute('style')
            if "none" in text:
                return False
        return True

    @allure.step("autoSegment(Chest)")
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
            text = roi_color.get_attribute('style')
            if "none" in text:
                return False
        return True

    @allure.step("autoSegment(headNeck)")
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
        sleep(90)
        # error_list = []
        # roi_colors = self.locations("roi_color", self.roi_color)
        # print(len(roi_colors))
        # for roi_color in roi_colors:
        #     text = roi_color.get_attribute('style')
        #     print(roi_color)
        #     print(text)
        #     if "none" in text:
        #         f1roi = self.find_parent(roi_color)
        #         print("f111111")
        #         f2roi = self.find_parent(f1roi)
        #         print('f22222')
        #         f3roi = self.find_parent(f2roi)
        #         print("f33333")
        #         f4roi = self.find_parent(f3roi)
        #         print("f44444")
        #         f5roi = self.find_parent(f4roi)
        #         print(f5roi)
        #         roi = self.find_child(f5roi, num=2).text     # 重新找父节点，且修改找子节点方法（修改为css selector
        #         print("roi:" + roi)
        #         error_list.append(roi)
        #     print(error_list)
        # print(error_list.text())
        # return error_list

        # result_message = self.local("result_message", self.auto_segment_result, num=0, flag=120)
        # message = result_message.text
        # print(message)
        # return message
        roi_colors = self.locations("roi_color", self.roi_color)
        for roi_color in roi_colors:
            text = roi_color.get_attribute('style')
            if "none" in text:
                return False
        return True

    @allure.step("autoSegment(abdomen)")
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
        sleep(120)
        roi_colors = self.locations("roi_color", self.roi_color)
        for roi_color in roi_colors:
            text = roi_color.get_attribute('style')
            if "none" in text:
                return False
        return True


