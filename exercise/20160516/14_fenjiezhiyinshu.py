#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 14_fenjiezhiyinshu.py
# Created Time: Tue May 17 09:55:59 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
import math
import sys
#找到最小的质数
def if_prime(n):
    top = int(math.sqrt(n+1))
    flag = 0
    for i in range(2,top+1):
        if n % i == 0:
            flag = 1
            break
    if flag:
        return False
    else:
        return True

#看能否被n整除
#能，打印，不能，回到上面再找

# def next_prime(num):
    # for i in range(2,num+1):
        # if if_prime(i):
            # yield i

while 1:
    try:
        num = int(raw_input("> "))
        # divide = 2
        if num < 1:
            print 'wrong number.input digit bigger than 1'
            continue
        while num != 1:

            # if not if_prime(divide):
                # divide += 1
                # continue
            divide = next_prime(num).next()#这个不行
            #原因是因为这每次迭代就相当于新的执行，一直都会是2
            if num % divide == 0:
                print divide
                num /= divide
            # else:
                # divide+=1


    except EOFError or KeyboardInterrupt:
        sys.exit(0)
    


