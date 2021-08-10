"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/10 9:36       
@Author:zexin                
 
"""
from time import sleep

from selenium import webdriver

from main.page.counterPage import CounterPage
from main.page.loginPage import LoginPage
from main.page.patientPage import PatientPage
# from main.page.registrationPage import RegistrationPage

if __name__ == '__main__':
    driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
    username = 'xzx'
    password = '111111'
    patient_name = "autotest_0809"
    login_page = LoginPage(driver)
    patient_page = login_page.login(username, password)
    sleep(5)
    counter_page = patient_page.open_patient(patient_name)
    sleep(10)
    registration_page = counter_page.switch_to_registration()
    rigid_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            if j != i:
                if i == 0:
                    fixed_ct_name = 'CT'
                    float_ct_name = 'CT' + str(j)
                elif j == 0:
                    fixed_ct_name = 'CT' + str(i)
                    float_ct_name = 'CT'
                else:
                    fixed_ct_name = 'CT' + str(i)
                    float_ct_name = 'CT' + str(j)
                rigid = registration_page.add_rigid_registration(fixed_ct_name, float_ct_name)
                rigid_list.append(rigid)
        print(rigid_list)
    registration_page.show_registration_tree(3)
    for rigid in rigid_list:
        registration_page.add_nonrigid_registration(rigid)

    sleep(30)