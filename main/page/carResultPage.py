"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/28 10:35       
@Author:zexin                
 
"""
from utils.BasePage import BasePage
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml
from utils.ScreenShot import get_shot


class CarResultPage(BasePage):
    logger = Logger("CarResultPage.py").getlog()
    ED = ReadYaml("main\\page_data\\axxxxe.yaml")

    def screenShot(self, name):
        name = get_shot(name)
        self.driver.get_screenshot_as_file(name)

    def download(self):
        download_data = []
        return download_data