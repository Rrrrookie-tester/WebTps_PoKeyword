"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/28 9:56       
@Author:zexin                
 
"""
from main.page.carResultPage import CarResultPage
from utils.BasePage import BasePage
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml


class CarMainPage(BasePage):
    logger = Logger("CarMainPage.py").getlog()
    ED = ReadYaml("main\\page_data\\axxxxe.yaml")

    def show_all(self):
        self.click("show_more_button", self.ED['show_more_button'])
        self.sleep(1)

    def perfect_information(self, information_data):
        owner = information_data[0]
        phone = information_data[1]
        plate_color = information_data[2]
        plate_num = information_data[3]

        Vin = information_data[4]
        engine_num = information_data[5]
        use_nature = information_data[6]  # shiyongxingzhi
        service_num = information_data[7]

        plate_type = information_data[8]
        car_type1 = information_data[9]
        car_type2 = information_data[10]
        car_type3 = information_data[11]
        car_color = information_data[12]
        engine_ml = information_data[13]   # pailiang

        drive_type = information_data[14]
        double_shaft = information_data[15]  # shuangzhuanzhou
        suspension = information_data[16]  # xuanjia
        headlight = information_data[17]
        tyre_size = information_data[18]

        product_date = information_data[19]
        first_date = information_data[20]
        last_date = information_data[21]
        km = information_data[22]
        km_h = information_data[23]

        fuel_supply = information_data[24]  # ranliaogonggei
        fuel_type = information_data[25]
        fuel_specification = information_data[26]  # ranliaoguige
        supply_mode = information_data[27]  # gongyoufangshi
        car_using = information_data[28]
        using_attribute = information_data[29]  # yongtushuxing

        transmission_form = information_data[30]  # biansuxiangxingshi
        gear = information_data[31]  # dangwei
        cylinder = information_data[32]  # qigang
        stroke = information_data[33]  # chongcheng
        Obd = information_data[34]  # Obd
        car_brand = information_data[35]  # cheliangpinpai
        car_model = information_data[36]  # cheliangxingha

        braking_source = information_data[37]  # zhidongliyuan
        lgnition_mode = information_data[38]  # dianhuofangshi
        air_inlet_mode = information_data[39]  # jinqifangshi
        electronic_parking = information_data[40]  # dianzizhuche
        Scr = information_data[41]   # SCR
        Dpf = information_data[42]   # DPF

        self.input("owner_input", self.ED['owner_input'], owner)
        self.sleep(1)
        self.input("phone_input", self.ED['phone_input'], phone)
        self.sleep(1)
        self.select("plate_color_select", self.ED['plate_color_select_box'], self.ED['select_item'], plate_color)
        self.sleep(1)
        self.input("plate_num_input", self.ED['plate_num_input'], plate_num)
        self.sleep(1)
        # ----------------
        self.input("vin_input", self.ED['vin_input'], Vin)
        self.sleep(1)
        self.input("engine_num_input", self.ED['engine_num_input'], engine_num)
        self.sleep(1)
        self.select("use_nature_select", self.ED['use_nature_select_box'], self.ED['select_item'], use_nature)
        self.sleep(1)
        self.input("service_num_input", self.ED['service_num_input'], service_num)
        self.sleep(1)
        # ---------------
        self.select("plate_type_select", self.ED['plate_type_select_box'], self.ED['select_item'], plate_type)
        self.sleep(1)
        self.select("car_type1_select", self.ED['car_type1_select_box'], self.ED['select_item'], car_type1)
        self.sleep(1)
        self.select("car_type2_select", self.ED['car_type2_select_box'], self.ED['select_item'], car_type3)
        self.sleep(1)
        self.select("car_type3_select", self.ED['car_type3_select_box'], self.ED['select_item'], car_type2)
        self.sleep(1)
        self.select("car_color_select", self.ED['car_color_select_box'], self.ED['select_item'], car_color)
        self.sleep(1)
        self.input("engine_ml_input", self.ED['engine_ml_input'], engine_ml)
        self.sleep(1)
        # --------------
        self.select("driver_type_select", self.ED['driver_type_select_box'], self.ED['select_item'], drive_type)
        self.sleep(1)
        if double_shaft:
            self.click("is_double_shaft_button", self.ED['is_double_shaft_button'])
        else:
            self.click("not_double_shaft_button", self.ED['not_double_shaft_button'])
        self.sleep(1)
        if suspension:
            self.click("independent_suspension_button", self.ED['independent_suspension_button'])
        else:
            self.click("not_independent_suspension_button", self.ED['not_independent_suspension_button'])
        self.sleep(1)
        self.select("headlight_select", self.ED['headlight_select_box'], self.ED['select_item'], headlight)
        self.sleep(1)
        self.input("tyre_size_input", self.ED['tyre_size_input'], tyre_size)
        self.sleep(1)
        # ------------
        self.input("product_date_input", self.ED['product_date_input'], product_date)
        self.sleep(1)
        self.input("first_date_input", self.ED['first_date_input'], first_date)
        self.sleep(1)
        self.input("last_date_input", self.ED['last_date_input'], last_date)
        self.sleep(1)
        self.input("km_input", self.ED['km_input'], km)
        self.sleep(1)
        self.input("km_h_input", self.ED['km_h_input'], km_h)
        self.sleep(1)
        # -------------
        self.select("fuel_supply_select", self.ED['fuel_supply_select_box'], self.ED['select_item'], fuel_supply)
        self.sleep(1)
        self.select("fuel_type_select", self.ED['fuel_type_select_box'], self.ED['select_item'], fuel_type)
        self.sleep(1)
        self.select("fuel_specification_select", self.ED['fuel_specification_select_box'], self.ED['select_item'], fuel_specification)
        self.sleep(1)
        self.select("supply_mode_select", self.ED['supply_mode_select_box'], self.ED['select_item'], supply_mode)
        self.sleep(1)
        self.select("car_using_select", self.ED['car_using_select_box'], self.ED['select_item'], car_using)
        self.sleep(1)
        if using_attribute:
            self.click("special_using_button", self.ED['special_using_button'])
        else:
            self.click("not_special_using_button", self.ED['not_special_using_button'])
        self.sleep(1)
        # ---------------
        self.select("transmission_form_select", self.ED['transmission_form_select_box'], self.ED['select_item'], transmission_form)
        self.sleep(1)
        self.select("gear_select", self.ED['gear_select_box'], self.ED['select_item'], gear)
        self.sleep(1)
        self.select("cylinder_select", self.ED['cylinder_select_box'], self.ED['select_item'], cylinder)
        self.sleep(1)
        self.select("stroke_select", self.ED['stroke_select_box'], self.ED['select_item'], stroke)
        self.sleep(1)
        if Obd:
            self.click("have_obd_button", self.ED['have_obd_button'])
        else:
            self.click("not_have_obd_button", self.ED['not_have_obd_button'])
        self.sleep(1)
        self.input("car_brand_input", self.ED['car_brand_input'], car_brand)
        self.sleep(1)
        self.input("car_model_input", self.ED['car_model_input'], car_model)
        self.sleep(1)
        # ------------
        self.select("braking_source_select", self.ED['braking_source_select_box'], self.ED['select_item'], braking_source)
        self.sleep(1)
        self.select("lgnition_mode_select", self.ED['lgnition_mode_select_box'], self.ED['select_item'], lgnition_mode)
        self.sleep(1)
        if air_inlet_mode:
            self.click("natural_ari_button", self.ED['natural_ari_button'])
        else:
            self.click("turbine_intake_button", self.ED['turbine_intake_button'])
        self.sleep(1)
        if electronic_parking:
            self.click("have_electronic_parking_button", self.ED['have_electronic_parking_button'])
        else:
            self.click("not_have_electronic_parking_button", self.ED['not_electronic_parking_button'])
        self.sleep(1)
        self.input("SCR_input", self.ED['Scr_input'], Scr)
        self.sleep(1)
        self.input("DPF_input", self.ED['Dpf_input'], Dpf)
        self.sleep(1)

    def submit(self):
        self.click("submit_button", self.ED['submit_button'])
        self.sleep(2)
        car_result_page = CarResultPage(self.driver)
        return car_result_page


