"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/4 9:35       
@Author:zexin                
 
"""
from time import sleep

import pytest
from selenium import webdriver

from main.page.addBeamPage import AddBeamPage
from main.page.loginPage import LoginPage
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml


class TestNormalDIMRT:
    logger1 = Logger("TestNormalDIMRT").getlog()
    plan_config = ReadYaml("main\\config\\reverse_plan_config.yaml")
    # test_data = ReadYaml("main\\test_data\\normal_UArc.yaml")
    # roi_config = test_data['roi_config']
    # plan_ng_config = test_data['plan_ng_config']
    # beam_config = test_data['beam_config']
    # constraint_config = test_data['optimization_constraint_config']

    # @classmethod
    # def setup_class(cls):
    #     cls.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
    #     username = 'xzx'
    #     password = '111111'
    #     patient_name = cls.roi_config[0]
    #
    #     cls.login_page = LoginPage(cls.driver)
    #     cls.login_page.login(username, password)
    #     sleep(5)
    #     cls.patient_page = PatientPage(cls.driver)
    #     cls.patient_page.open_patient(patient_name)
    #     cls.logger1.info("open patient: %s " % patient_name)
    #     sleep(10)
    #     cls.counter_page = CounterPage(cls.driver)
    #     cls.counter_page.switch_series(cls.roi_config[1])
    #     cls.logger1.info("select series: %s", cls.roi_config[1])
    #     cls.counter_page.enter_ct_density()
    #     cls.ct_density_page = CTDensityPage(cls.driver)
    #     cls.ct_density_page.select_density()
    #     cls.logger1.info("update CTDensity to 'Default Template'")
    #
    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()

    @pytest.mark.parametrize('plan_config', plan_config)
    def test_normal_dimrt(self, plan_config):
        data_path = "main\\test_data\\" + plan_config
        test_data = ReadYaml(data_path)
        patient_config = test_data['patient_config']
        roi_config = test_data['roi_config']
        plan_ng_config = test_data['plan_ng_config']
        beam_config = test_data['beam_config']
        constraint_config = test_data['optimization_constraint_config']
        self.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '111111'
        patient_name = patient_config[0]

        login_page = LoginPage(self.driver)
        patient_page = login_page.login(username, password)
        sleep(5)
        # ----添加创建患者、导入序列步骤----
        new_patient_page = patient_page.enter_new_patient()
        new_patient_page.new_patient(patient_name)
        import_page = patient_page.enter_import(patient_name)
        import_page.import_from_local(patient_config[1])
        # ----添加创建患者、导入序列步骤----
        counter_page = patient_page.open_patient(patient_name)
        self.logger1.info("open patient: %s " % patient_name)
        sleep(10)
        counter_page.switch_series(patient_config[2])
        self.logger1.info("select series: %s", patient_config[2])
        ct_density_page = counter_page.enter_ct_density()
        ct_density_page.select_density()
        self.logger1.info("update CTDensity to 'Default Template'")
        roi_template_page = counter_page.enter_add_roi_by_template()
        roi_template_page.add_roi_by_template(roi_config[0])
        self.logger1.info("add roi by template: %s" % roi_config[0])

        # 以上为PWS，接下来为TPS

        plan_page = counter_page.switch_to_plan()
        add_plan_page = plan_page.enter_add_plan()
        add_plan_page.create_plan_ng(*plan_ng_config)
        self.logger1.info("create plan and ng end")
        plan_page.switch_plan_list()
        plan_page.select_plan(plan_ng_config[0])
        add_beam_page = AddBeamPage(self.driver)
        beam_num = len(beam_config)
        self.logger1.info("The total number of beams is %d" % beam_num)
        beam_index = 1
        for single_beam in beam_config:
            plan_page.enter_add_beam()
            add_beam_page.add_beam(*single_beam)
            self.logger1.info("add index: %d beam end" % beam_index)
            beam_index = beam_index + 1
        add_optimization_constraints = plan_page.open_add_optimization_constraints()
        constraint_num = len(constraint_config)
        self.logger1.info("The total number of constraint is %d" % constraint_num)
        constraint_index = 1
        for constraint in constraint_config:
            add_optimization_constraints.create_optimization_constraints(*constraint)
            self.logger1.info("add index: %d constraint end" % constraint_index)
            constraint_index = constraint_index + 1
        add_optimization_constraints.close_optimization_constraint_page()
        self.logger1.info("start optimize plan: %s " % plan_ng_config[0])
        plan_page.start_optimize()
        self.logger1.info(" plan: %s optimize end" % plan_ng_config[0])
        result = plan_page.save_result()
        self.logger1.info("save plan: %s" % plan_ng_config[0])
        assert result, self.logger1.error("plan: %s optimize failed" % plan_ng_config[0])


if __name__ == '__main__':
    pytest.main(['-s', 'test_reverse_plan.py'])