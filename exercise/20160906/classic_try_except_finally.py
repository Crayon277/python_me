#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: classic_try_except_finally.py
# Created Time: Tue Sep  6 22:07:00 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

try:
    data = open('missing.txt')
    print data.readline()
except IOError:
#except IOError as err: #给异常对象起个名字
    print "missing file doesn't exists!"
    # print 'file error'+err
#print 'file error'+ str(err)

finally:
    data.close()

#有点类似悖论
#解决方法：
# finally:
    # if 'data' in locals(): #先做一个简单的测试。locals()会返回当前作用域中定义的所有名的一个集合
        # data.close()

#第二种解决方法！！！with语句
#妥善关闭一个可能打开的数据文件
try:
    with open('miss.txt') as data:
        print data.readline()
except IOError as err:
    print 'file error' + str(err)

#with语句利用了一种上下文管理协议的Python技术
