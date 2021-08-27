"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/7/8 10:03       
@Author:zexin                
 
"""
import os

import yaml


def ReadYaml(yaml_dic_name):
    current_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(os.path.abspath(os.path.join(current_path, "..")), yaml_dic_name)
    f = open(yaml_path, 'r', encoding='utf-8',  errors='ignore')
    data = yaml.load(f.read(), Loader=yaml.BaseLoader)
    return data