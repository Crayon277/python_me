#!/usr/bin/python

def common_divisor(a,b):
    n = a % b
    if n == 0:
        print b,"is the max common divisor"
    else:
        a,b = b,n
        common_divisor(a,b)

common_divisor(153,123)
