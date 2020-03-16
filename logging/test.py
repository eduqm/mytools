#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-3-16 10:09
# @Author  : duquanming
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import logging
#  默认只显示后三个级别，设置默认级别
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')

''' 名词解释
Logging.Formatter：这个类配置了日志的格式，在里面自定义设置日期和时间，输出日志的时候将会按照设置的格式显示内容。
Logging.Logger：Logger是Logging模块的主体，进行以下三项工作：
    1. 为程序提供记录日志的接口
    2. 判断日志所处级别，并判断是否要过滤
    3. 根据其日志级别将该条日志分发给不同handler
常用函数有：
    Logger.setLevel() 设置日志级别
    Logger.addHandler() 和 Logger.removeHandler() 添加和删除一个Handler
    Logger.addFilter() 添加一个Filter,过滤作用
    Logging.Handler：Handler基于日志级别对日志进行分发，如设置为WARNING级别的Handler只会处理WARNING及以上级别的日志。
常用函数有：
    setLevel() 设置级别
    setFormatter() 设置Formatter
'''