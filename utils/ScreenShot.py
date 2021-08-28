"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/8/28 12:15       
@Author:zexin                
 
"""
import os
import time


def get_shot(name):
    now_date = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(time.time()))
    shot_path = os.path.dirname(os.path.dirname(os.path.abspath('.'))) + '\\ScreenShot'
    # log_name = log_path + "WebTPSTestLog_%s.log" % now_date
    shot_name = shot_path + name + "_%s.png" % now_date
    return str(shot_name)