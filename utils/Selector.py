"""
@Project: WebTps_PoKeyword   
@Description: To structure selector
@Time:2021/7/8 14:21       
@Author:zexin                
 
"""


def structure_selector(num, part1, part2):
    return part1 + str(num) + part2


def structure_location(key, selector):
    # 直接返回定位元组
    selector_str = str(selector[1]) + str(key) + str(selector[2])
    location = (selector[0], selector_str)
    return location
