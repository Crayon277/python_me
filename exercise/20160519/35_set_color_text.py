#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 35_set_color_text.py
# Created Time: Thu May 19 16:03:05 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#文本颜色设置。

class bcolors:
    HEADER = '\033[95m' #
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #关闭所有属性
    BOLD = '\033[1m' 
    UNDERLINE = '\033[4m' #下划线

print bcolors.HEADER+'大头的颜色'
print 'how about this one following header'
print bcolors.OKBLUE+'okblue的颜色'
print bcolors.OKGREEN+"okgreen的颜色"
print bcolors.WARNING+'警告的颜色字体？'#+bcolors.ENDC
print bcolors.WARNING+'警告的颜色字体？'+bcolors.ENDC
print bcolors.FAIL+'Fail的颜色？'
print bcolors.ENDC+"endc 的颜色"
print bcolors.BOLD+"BOLD 的颜色"
print bcolors.UNDERLINE+"underline 的颜色"
print 'how about this'

#如果没有加bcolors.ENDC的话，后面print的格式也会有颜色跟最后一个的格式一样
# Console上运行的python程序，有没有办法让print输出的文本可以显示不同的颜色？ 
# 这个其实跟python无关，跟具体所用console的类型有关系，不同的类型对应不同的控制码，如果是ansi终端，可以用ansi的控制码。
