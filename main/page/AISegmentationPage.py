"""
@Project: WebTps_PoKeyword   
@Description: To local and control AI segmentation's elements
@Time:2021/7/22 10:23       
@Author:zexin                
 
"""
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class AISegmentationPage(BasePage):
    element_config = ReadYaml("main\\page_data\\AISegmentationPage.yaml")

    search_input = element_config['search_input']
    search_button = element_config['search_button']
    search_result = element_config['search_result']
    counter_button = element_config['counter_button']

    def AI_segmentation(self, Ai_template_name):
        self.input("search_input", self.search_input, Ai_template_name)
        self.click("search_button", self.search_button)
        self.click("search_result", self.search_result)
        self.click("counter_button", self.counter_button)