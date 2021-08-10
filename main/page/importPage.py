"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/5 10:11       
@Author:zexin                
 
"""

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class ImportPage(BasePage):
    ED = ReadYaml("main\\page_data\\importPage.yaml")

    def import_from_local(self, series_path):
        select_item = ('xpath', '//div[@title="', '"]')
        self.select("data_source_select", self.ED['data_source_select'], select_item, '本地磁盘')
        self.input("file_upload_input", self.ED['upload_input'], series_path)
        self.click("series_checkbox", self.ED['series_checkbox'], flag=20)
        self.click("submit_button", self.ED['submit_button'])
        self.sleep(1)
        self.click("accept_button1", self.ED['accept_button'], num=3)
        self.click("accept_button1", self.ED['accept_button'], num=4)
        self.click("confirm_button", self.ED['confirm_button'])
        if self.element_disappear("import_loading", self.ED['import_loading']):
            self.sleep(5)
            self.click("back_Pa_button", self.ED['back_PA_button'])
