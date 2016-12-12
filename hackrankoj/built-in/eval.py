#!/usr/bin/env python
# coding=utf-8


'''
eval(cmd)
本质上就是python在执行cmd，这样想就对了
有什么用？cmd是以字符串给出，有了这样的一层，我们可以更好的操作字符串来改变命令

Task
You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).

NOTE: Python2 users, please import from __future__ import print_function.

Constraint
Input string is less than 100 characters.

Sample Input

print(2 + 3)
Sample Output

5
'''

from __future__ import print_function
eval(raw_input())
