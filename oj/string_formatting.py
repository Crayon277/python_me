#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Read the integer,  and print the decimal, octal, hexadecimal, and binary values from  to  with space padding so that all fields take the same width as the binary value.

17

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""


import math
n=int(raw_input())
space_format = int(math.ceil(math.log(n+1,2)))
for i in range(1,n+1):
    s=''
    tmp=i
    while i:
        s+=str(i%2)
        i=i/2
    print '%*d %*o %*X %*s'%(space_format,tmp,space_format,tmp,space_format,tmp,space_format,s[::-1])

"""
#熟悉 format方法！！

def fun(N):
    width = len(bin(N)) - 2 #bin 内建函数，return string
    for i in range(1,N+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)

n = input()
fun(n)
"""

"""上面的另一种写法
for i in range(1,N+1):
    for base in 'doXb':
        print '{0:{width}{base}}'.format(i,width = width,base = base),
    print
"""

"""
n = int(raw_input())
spacing = len(bin(n)[2:])

for i in range(1,n+1):
    print str(i).rjust(spacing, ' '),str(oct(i)[1:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' ')

"""
