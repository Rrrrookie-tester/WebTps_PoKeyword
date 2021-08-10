"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/7/8 11:18       
@Author:zexin                
 
"""
# from selenium import webdriver
#
# from utils.BasePage import BasePage
# config = ['id', 'userName_input']
# driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
# base = BasePage(driver)
# base.open()
# ele = base.find_element_wait("username", *config)
# print(ele)
# from typing import List
#
# import pytest
# import pandas as pd
#
# from utils.Logger import Logger
#
#
# class TestAutoSegmentation:
#     logger1 = Logger("test_Page1.py").getlog()
#
#     @pytest.mark.parametrize('series_num', range(1, 16))
#     def test_assert(self, series_num):
#         # 验证自动分割结果的思路
#         a = ['(1,2,3)', '(1,2,3)']
#         b = ['(1,2,3)', '(1,2,3)']
#         c = ['(1,2,3)', '(1,1,3)']
#         d = ['(1,2,3)', '(1,2,3)']
#         res = [a, b, c, d]
#         print(len(res))
#         print(res)
#         for i in res:
#             assert i[0] == i[1], self.logger1.error("series %s auto segmentation failed !" % str(series_num))
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_page.py'])


# 分割两个正方形
# from typing import List
#
#
# class Solution:
#     def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
#         node_list = []
#         center1_x = square1[0]+square1[2]/2
#         center1_y = square1[1]+square1[2]/2
#         center2_x = square2[0] + square2[2]/2
#         center2_y = square2[1] + square2[2]/2
#         if center2_x-center1_x !=0:
#             k = (center2_y - center1_y)/(center2_x - center1_x)
#             b = center1_y - (k * center1_x)
#             if k>1 or k<-1:
#                 # 将纵坐标带入
#                 y_min = min(square1[1], square2[1], square2[1] + square2[2], square1[1] + square1[2])
#                 y_max = max(square1[1], square2[1], square2[1] + square2[2], square1[1] + square1[2])
#                 x_1 = (y_min - b) / k
#                 x_2 = (y_max - b) / k
#                 node_list.append(min(x_1, x_2))
#                 node_list.append(k*min(x_1, x_2)+b)
#                 node_list.append(max(x_1, x_2))
#                 node_list.append(k*max(x_1, x_2)+b)
#
#             elif -1<=k<=1:
#                 # 横坐标带入
#                 x_min = min(square1[0], square2[0], square2[0] + square2[2], square1[0] + square1[2])
#                 x_max = max(square1[0], square2[0], square2[0] + square2[2], square1[0] + square1[2])
#                 y_min = k * x_min + b
#                 y_max = k * x_max + b
#                 node_list.append(x_min)
#                 node_list.append(y_min)
#                 node_list.append(x_max)
#                 node_list.append(y_max)
#         else:
#             b = center1_x
#             y_min = min(square1[1], square2[1], square2[1] + square2[2], square1[1] + square1[2])
#             y_max = max(square1[1], square2[1], square2[1] + square2[2], square1[1] + square1[2])
#             node_list.append(b)
#             node_list.append(y_min)
#             node_list.append(b)
#             node_list.append(y_max)
#         result = []
#         for item in node_list:
#             result.append(float(item))
#         return result
#
#
# so = Solution()
# print(so.cutSquares([-2, -2, 3], [0, 0, 4]))

# def test(a, list1, list2, b):
#     print(a)
#     print(list1)
#     print(list2)
#     print(b)
#     # #beamGroupGoal
#
#
# test('a', ['css selector', '.tps-ant-select-selector'], ['xpath', '//div[@title="', '"]'], b=3)
from typing import List

from utils.ReadYaml import ReadYaml


# def YamlData(cls):
#     cls.element_config = ReadYaml("main\\page_data\\addBeamPage.yaml")
#     # print(type(element_config))
#     # print(element_config)
#     return cls
#
#
# # @YamlData(path="main\\page_data\\addBeamPage.yaml")
# @YamlData
# class Test1():
#     element_config = {}
#
#     def __init__(self):
#         pass
#
#
# if __name__ == '__main__':
#     test1 = Test1()
#     print(test1.element_config)


# data = ReadYaml("main\\test_data\\normal_DIMRT.yaml")
# print(data['plan_ng_config'])
# print(data['beam_config'])
# print(data['beam_config'][0])
# print(data['constraint_config'])

# "main\\page_data\\addBeamPage.yaml"
# list_data = ['beam1_autotest', 'PTV_Rectum', '6X', 600, 15]
#
#
# def add_beam(bname, roi_name, type, rate, angle):
#     print(bname)
#     print(roi_name)
#     print(type)
#     print(rate)
#     print(angle)
#
#
# add_beam(*list_data)


# def test(number):
#     # 在函数内部再定义一个函数
#     def test_in(number_in):
#         return number + number_in
#
#     # 返回闭包
#     return test_in
#
#
# res = test(10)
# print(res(100))
# # print(res(200))
# # print(res(300))

# import json
# data1 = [{'a': 1, 'b': 2, 'c': 3}]
# print(json.dumps(data1))
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         for i in range(0, len(flowerbed)-3, 3):
#             if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
#                 n = n-1
#         if n == 0:
#             return True
#         else:
#             return False
#
#
# so = Solution()
# if so.canPlaceFlowers([1,0,1,0,1,0,1],1):
#     print("True")
# else:
#     print("False")
#
# d = {'a': 30, 'g': 50, 'i': 12, 'k': 23}
# print(d.items())
# # sorted(d.items(), key=lambda x: x[1])
# print(d.items(), key=lambda x: x[1])

def test(a):
    indexs = []
    length = len(a)
    for i in range(0, length):
        if a[i] == 0:
            indexs.append(i)
    for index in indexs:
        a.insert(index+1, 0)
    print(a[0:length])


test([1, 0, 2, 0, 3])