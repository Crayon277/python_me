#!/usr/bin/env python
# coding=utf-8

import math
ab,bc=float(raw_input()),float(raw_input())
print str(int(round((math.atan(ab/bc)*180)/math.pi)))+'°'


'''
我一开始是import cmath
终于明白了，cmath是complexmath，cmath.atan()等操作返回的都是complex类型的数！！！

import math
ab = float(raw_input())
bc = float(raw_input())
tang = ab / bc
rad = math.atan(tang)
print '{}°'.format(int(round(math.degrees(rad))))

弧度转角度 有现成的函数math.degrees

round函数,四舍五入，返回浮点型

怎么算这个角度，中位线
'''
