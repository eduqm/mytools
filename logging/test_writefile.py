#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-3-16 10:26
# @Author  : duquanming
# @Site    : 
# @File    : test_writefile.py
# @Software: PyCharm

import logging
import os.path
import time

#  创建logger
logger = logging.getLogger()
#  设置级别
logger.setLevel(logging.INFO)
#  创建handler,用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/logs/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)
# 定义输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

# 第四步，将logger添加到handler里面
logger.addHandler(fh)
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')