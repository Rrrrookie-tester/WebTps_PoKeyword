"""
@Project: WebTps_PoKeyword   
@Description: To local and control roi template page's elements
@Time:2021/7/8 15:43       
@Author:zexin                
 
"""

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class RoiTemplatePage(BasePage):
    element_config = ReadYaml("main\\page_data\\roitemplatePage.yaml")

    template_name_selectbox = element_config['template_name_selectbox']
    template_name_selectitem = element_config['template_name_selectitem']
    all_select_button = element_config['all_select_button']
    submit_button = element_config['submit_button']

    def add_roi_by_template(self, template_name):
        self.select("template_select",self.template_name_selectbox, self.template_name_selectitem, template_name)
        self.sleep(1)
        self.click("all_select_button", self.all_select_button, num=8)
        self.click("submit_button", self.submit_button)
        self.sleep(20)




