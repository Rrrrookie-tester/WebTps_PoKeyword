"""
@Project: WebTps_PoKeyword   
@Description: TODO          
@Time:2021/7/8 9:19       
@Author:zexin                
 
"""
import logging
import os
import time


class Logger(object):
    def __init__(self, logger="root"):
        now_date = time.strftime("%Y_%m_%d", time.localtime(time.time()))
        log_path = os.path.dirname(os.path.dirname(os.path.abspath('.'))) + '\\log\\'
        log_name = log_path + "WebTPSTestLog_%s.log" % now_date
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建用于输出到本地文件的FileHandler
        if not self.logger.handlers:
            fh = logging.FileHandler(log_name, 'a', 'utf-8')  # 日志写入式追加模式
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s - %(filename)s - %(name)s - [line:%(lineno)d] - %(levelname)s - %('
                'message)s', "%Y-%b-%d %H:%M:%S")
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            # 创建用于输出到控制台得ConsoleHandler
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def getlog(self):
        return self.logger