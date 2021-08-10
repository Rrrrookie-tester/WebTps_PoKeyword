"""
@Project: WebTps_PoKeyword   
@Description: To add list type data into log
@Time:2021/8/2 11:09       
@Author:zexin                
 
"""


def list_log(list_data):
    str_data = ','.join(list_data)
    str_log = '[' + str_data + ']'
    return str_log

