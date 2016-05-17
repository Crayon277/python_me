#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 18_sum_a_aa_aaa_v2.py
# Created Time: Tue May 17 15:48:50 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。


Tn = 0
Sn = []
n = int(raw_input("times> "))
a = int(raw_input("a> "))

for count in range(n):
    Tn = Tn+a #Tn表示的是每个加数
    a = a*10  #a表示每个序列数的最高位的级别    
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y:x+y,Sn)

print Sn

#我的思想在每次循环就直接加上sum，a表示的是就是每个序列数
#他这里的细想是Tn表示低几位，a表示最高位， 每次循环Tn+a才是真正的加数

