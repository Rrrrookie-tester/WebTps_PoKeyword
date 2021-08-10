"""
@Project: WebTps_PoKeyword   
@Description: To test create normal dimrt plan
@Time:2021/7/31 17:14       
@Author:zexin                
 
"""
from time import sleep

import pytest
from selenium import webdriver

from main.page.addBeamPage import AddBeamPage
from main.page.addOptimizationConstraintsPage import AddOptimizationConstraints
from main.page.addPlanPage import AddPlanPage
from main.page.counterPage import CounterPage
from main.page.ctDensityPage import CTDensityPage
from main.page.loginPage import LoginPage
from main.page.patientPage import PatientPage
from main.page.planPage import PlanPage
from main.page.roitemplatePage import RoiTemplatePage
from utils.Logger import Logger

from utils.ReadYaml import ReadYaml


class TestNormalDIMRT:
    logger1 = Logger("TestNormalDIMRT").getlog()
    test_data = ReadYaml("main\\test_data\\normal_DIMRT.yaml")
    roi_config = test_data['roi_config']
    plan_ng_config = test_data['plan_ng_config']
    beam_config = test_data['beam_config']
    constraint_config = test_data['optimization_constraint_config']

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '111111'
        patient_name = cls.roi_config[0]

        cls.login_page = LoginPage(cls.driver)
        cls.login_page.login(username, password)
        sleep(5)
        cls.patient_page = PatientPage(cls.driver)
        cls.patient_page.open_patient(patient_name)
        cls.logger1.info("open patient: %s " % patient_name)
        sleep(10)
        cls.counter_page = CounterPage(cls.driver)
        cls.counter_page.switch_series(cls.roi_config[1])
        cls.logger1.info("select series: %s", cls.roi_config[1])
        cls.counter_page.enter_ct_density()
        cls.ct_density_page = CTDensityPage(cls.driver)
        cls.ct_density_page.select_density()
        cls.logger1.info("update CTDensity to 'Default Template'")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_normal_dimrt(self):
        self.counter_page.enter_add_roi_by_template()
        self.roi_template_page = RoiTemplatePage(self.driver)
        self.roi_template_page.add_roi_by_template(self.roi_config[3])
        self.logger1.info("add roi by template: %s" % self.roi_config[3])
        self.counter_page.switch_to_plan()
        self.plan_page = PlanPage(self.driver)
        self.plan_page.enter_add_plan()
        self.add_plan_page = AddPlanPage(self.driver)
        self.add_plan_page.create_plan_ng(*self.plan_ng_config)
        self.logger1.info("create plan and ng end")
        self.plan_page.switch_plan_list()
        self.plan_page.select_plan(self.plan_ng_config[0])
        self.add_beam_page = AddBeamPage(self.driver)
        beam_num = len(self.beam_config)
        self.logger1.info("The total number of beams is %d" % beam_num)
        beam_index = 1
        for single_beam in self.beam_config:
            self.plan_page.enter_add_beam()
            self.add_beam_page.add_beam(*single_beam)
            self.logger1.info("add index: %d beam end" % beam_index)
            beam_index = beam_index + 1
        self.plan_page.open_add_optimization_constraints()
        self.add_optimization_constraints = AddOptimizationConstraints(self.driver)
        constraint_num = len(self.constraint_config)
        self.logger1.info("The total number of constraint is %d" % constraint_num)
        constraint_index = 1
        for constraint in self.constraint_config:
            self.add_optimization_constraints.create_optimization_constraints(*constraint)
            self.logger1.info("add index: %d constraint end" % constraint_index)
            constraint_index = constraint_index + 1
        self.add_optimization_constraints.close_optimization_constraint_page()
        self.logger1.info("start optimize plan: %s " % self.plan_ng_config[0])
        self.plan_page.start_optimize()
        self.logger1.info(" plan: %s optimize end" % self.plan_ng_config[0])
        result = self.plan_page.save_result()
        self.logger1.info("save plan: %s" % self.plan_ng_config[0])
        assert result, self.logger1.error("plan: %s optimize failed" % self.plan_ng_config[0])


if __name__ == '__main__':
    pytest.main(['-s', 'test_normal_dimrt.py'])