#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 19_WanShu.py
# Created Time: Tue May 17 16:22:41 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


""" 这个程序是分解质因子之和
def if_wanshu(n):
    if n == 1:
        return True
    sum = 1
    tmp = n
    for i in range(2,n+1):
        # print 'n=%d,i=%d'%(n,i)
        while n > i:
            # print 'n=%d,pass while'%n
            if n%i == 0:
                # print 'n=%d,sum = %d'%(n,sum)
                sum+=i
                n/=i
            else: #!!这里不要忘了，不然死循环
                break
    # print 'n=%d,pass'%n
    if sum+n == tmp:
        return True
    else:
        return False

for item in range(1,1001):
    if if_wanshu(item):
        print item
"""

#因子，没说质因子
#例如 28, 因子有1 2 4 7 14。 28 ＝ 1+2+4+7+14 不是说要求分解因子
#那这样也就是说要算出他所有的因子

for item in range(2,1001):
    sum = 0
    for i in range(1,item/2+1):
        if item%i==0:
            sum+=i
    if sum == item:
        print item

