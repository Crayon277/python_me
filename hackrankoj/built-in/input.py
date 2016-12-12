#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'

如果
>>>input()
x+4
会报错，因为x没有定义
>>>raw_input()
x+4
返回的是'x+4'的字符串
input会把x+4当作表达式
可以事先定义x

>>>x=4
>>>input()
x+4
8

Task

You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .

Constraints
All coefficients of polynomial  are integers.
 and  are also integers.

Input Format

The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format

Print True if . Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True

'''

x,result=map(int,raw_input().split())
print input() == result
