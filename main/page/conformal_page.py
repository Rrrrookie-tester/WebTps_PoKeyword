"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/3 13:55       
@Author:zexin                
 
"""
# from time import sleep
#
# from selenium import webdriver
#
# from main.page.addBeamPage import AddBeamPage
# from main.page.addPlanPage import AddPlanPage
# from main.page.counterPage import CounterPage
# from main.page.ctDensityPage import CTDensityPage
# from main.page.loginPage import LoginPage
# from main.page.patientPage import PatientPage
# from main.page.planPage import PlanPage
import allure

from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class ConformalPage(BasePage):
    ED = ReadYaml("main\\page_data\\conformal_page.yaml")

    @allure.step("beam conformal target")
    def conformal_target(self, target_name):
        self.click("target_lab_button", self.ED['target_lab'])
        self.select("target_select", self.ED['target_select'], self.ED['target_item'], target_name)
        self.click("conformal_submit_button", self.ED['conformal_submit'])
        self.sleep(1)

#
# if __name__ == '__main__':
#     driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
#     username = 'xzx'
#     password = '111111'
#     login_page = LoginPage(driver)
#     login_page.login(username, password)
#     sleep(5)
#     patient_page = PatientPage(driver)
#     patient_page.open_patient("autotest_debug_1")
#     sleep(10)
#     counter_page = CounterPage(driver)
#     counter_page.switch_series("CT")
#     counter_page.enter_ct_density()
#     ct_density_page = CTDensityPage(driver)
#     ct_density_page.select_density()
#     # self.counter_page.enter_add_roi_by_template()
#     # self.roi_template_page = RoiTemplatePage(self.driver)
#     # self.roi_template_page.add_roi_by_template(roi_config[3])
#     # self.logger1.info("add roi by template: %s" % roi_config[3])   //按模板添加ROI部分
#     counter_page.switch_to_plan()
#     plan_page = PlanPage(driver)
#     plan_page.enter_add_plan()
#     add_plan_page = AddPlanPage(driver)
#     add_plan_page.create_plan_ng('plan_simrt_autotest', 'ng1_autotest','Trilogy-SN6334','PHOTON','SIMRT','20','200','95','PTV_Rectum','95')
#     plan_page.switch_plan_list()
#     plan_page.select_plan('plan_simrt_autotest')
#     plan_page.enter_add_beam()
#     add_beam_page = AddBeamPage(driver)
#     add_beam_page.add_beam('beam1_autotest','PTV_Rectum','6X','600','15',0)
#     plan_page.select_beam("beam1_autotest")
#     plan_page.enter_conformal()
#     conformal_page = ConformalPage(driver)
#     conformal_page.conformal_target("PTV_Rectum")
#     sleep(1)
#     plan_page.calculate()
#     sleep(60)