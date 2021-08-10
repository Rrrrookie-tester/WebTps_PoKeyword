"""
@Project: WebTps_PoKeyword   
@Description: To local and control plan page's elements
@Time:2021/7/8 17:02       
@Author:zexin                
 
"""
from main.page.addOptimizationConstraintsPage import AddOptimizationConstraints
from main.page.addPlanPage import AddPlanPage
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml
from utils.Selector import structure_selector


class PlanPage(BasePage):
    element_config = ReadYaml("main\\page_data\\planPage.yaml")

    plan_list_button = element_config['plan_list_button']
    select_plan_button = element_config['select_plan_button']
    show_plan_button = element_config['show_plan_tree_node']
    load_plan_button = element_config['load_plan_button']
    select_ng_button = element_config['select_ng_button']
    show_add_plan_button = element_config['show_add_plan_button']
    add_plan_button = element_config['add_plan_button']
    show_add_beam_button = element_config['show_add_beam_button']
    add_beam_button = element_config['add_beam_button']
    dose_calculate_button = element_config['dose_calculate_button']
    optimize_button = element_config['optimize_button']
    optimization_constraints_lab = element_config['optimization_constraints_lab']
    add_optimization_constraints_button = element_config['add_optimization_constraints_button']
    select_beam_button = element_config['select_beam_button']

    def switch_plan_list(self):
        self.click("plan_list_button", self.plan_list_button, 1)
        self.sleep(1)

    def enter_add_plan(self):
        self.move("show_add_plan_button", self.show_add_plan_button, 2)
        self.sleep(1)
        self.go_mark("add_plan_button", 0, 25)
        self.sleep(1)
        add_plan_page = AddPlanPage(self.driver)
        return add_plan_page

    def select_plan(self, plan_name):
        element_name = "select_" + plan_name + "_button"
        selector = structure_selector(plan_name, self.select_plan_button[1], self.select_plan_button[2])
        location = (self.select_plan_button[0], selector)
        self.click(element_name, location, num=0)
        self.click("load_plan_button", self.load_plan_button)
        self.sleep(5)
        self.click("show_plan_button", self.show_plan_button, num=-1)
        self.sleep(0.5)
        self.click("select_ng_button", self.select_ng_button, num=-1)
        self.sleep(1)

    def select_beam(self, beam_name):
        self.click("show_ng_tree_node", self.element_config['show_ng_tree_node'], num=1)
        selector = structure_selector(beam_name, self.select_beam_button[1], self.select_beam_button[2])
        local = (self.select_beam_button[0], selector)
        self.click("beam: %s " % beam_name, local)
        self.sleep(0.5)

    def enter_conformal(self):
        self.click("conformal_button", self.show_add_plan_button, num=5)
        self.sleep(1)

    def calculate(self):
        self.move("show_calculate_button", self.show_add_plan_button, 7)
        self.sleep(1)
        self.go_mark("calculate_button", 0, 25)
        self.sleep(1)

    def enter_add_beam(self):
        # -----------------
        self.move("show_add_beam_button", self.show_add_beam_button, num=4)
        self.sleep(1)
        self.go_mark("add_beam_button", 0, 25)
        self.sleep(1)
        # ----以上为 清除按钮上已有浮贴，bug修改后可以删去
        self.move("show_add_beam_button", self.show_add_beam_button, num=4)
        self.sleep(1)
        self.go_mark("add_beam_button", 0, 25)
        self.sleep(1)

    # def enter_add_other_beam(self):
    #     self.move("show_add_beam_button", self.show_add_beam_button, num=4, flag=0)
    #     self.sleep(1)
    #     self.go_mark("add_beam_button", 0, 25)
    #     self.sleep(1)
    #     # 以上为 清除按钮上已有浮贴，bug修改后可以删去
    #     self.move("show_add_beam_button", self.show_add_beam_button, num=4, flag=0)
    #     self.sleep(1)
    #     self.go_mark("add_beam_button", 0, 25)
    #     self.sleep(1)

    def open_add_optimization_constraints(self):
        self.click("optimization_constraints_lab", self.optimization_constraints_lab)
        self.sleep(1)
        self.click("add_optimization_constraints_button", self.add_optimization_constraints_button)
        self.sleep(1)
        add_optimization_constraints = AddOptimizationConstraints(self.driver)
        return add_optimization_constraints

    def start_optimize(self):
        self.click("start_optimize_button", self.optimize_button, num=15)
        self.sleep(60)

    def save_result(self):
        try:
            self.click("save result button", self.show_add_plan_button)
            self.sleep(3)
            return 1
        except:
            return 0

