"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/16 15:17       
@Author:zexin                
 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def show_shadow(element):
    # 展开shadow
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
driver.get('https://www.virustotal.com/gui/domain/modem.pw')
driver.maximize_window()
sleep(10)

domain_view = driver.find_element_by_name('domain-view')         # 找到name=domain-view的元素
shadow1 = show_shadow(domain_view)                              # 展开shadowRoot
report = shadow1.find_element_by_id('report')  # 找到id为report的元素
shadow2 = show_shadow(report)                       # 展开shadowRoot
vt_ui_detections_widget = shadow2.find_element_by_css_selector('div > header > div > vt-ui-detections-widget')
shadow3 = show_shadow(vt_ui_detections_widget)
positives = shadow3.find_elements_by_css_selector('.positives')[0]
print(positives.text)


# def assert_dict():
#     dict1 = {'A': '1', 'B': '2', 'C': '3', 'D': '4'}
#     dict2 = {'A': '1', 'B': '2', 'C': '3', 'D': '4'}
#     for k, v in dict1.items():
#         if dict2[k] != v:
#             return False
#     return True
#
# if assert_dict():
#     print("相同")
# else:
#     print("不同")



