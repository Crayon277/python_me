#!/usr/bin/env python
# coding=utf-8


#我的
input()
a = set(map(int,raw_input().split()))
for _ in range(input()):
    eval('a.{0}({1})'.format(raw_input().split()[0],map(int,raw_input().split())))
print sum(a)

#改成列表解析的形式
#for _ in range(input()):
(eval('a.{0}({1})'.format(raw_input().split()[0],map(int,raw_input().split()))) for _ in range(input()))
#这样会出错
[eval('a.{0}({1})'.format(raw_input().split()[0],map(int,raw_input().split()))) for _ in range(input())]
#换成列表就对了，为什么？print 出来，这条语句生成的是[None,None,None,None]
#()的形式的话 是<generator object <genexpr> at 0x7ff69eb87960>。
'''
因为 (expr for iter_var in iterable if cond_expr) 这个是生成器表达式！！！
他并不真正的创建数字列表，在这里，也就不真正的执行eval。可以用next方法
>>> test = (x for x in range(4))
>>> test.next()
0
>>> for _ in test:
...     print _
...
1
2
3
'''
[getattr(a,raw_input().split()[0])(map(int,raw_input().split())) for _ in range(input())]

"""
As it was very easy challenge I was trying to reduce number of lines and I came up with this (python 3).

S = input() == 0 or set(input().split())
[getattr(S, input().split()[0])(input().split()) for _ in range(int(input()))]
print(sum(map(int, S)))

Is it possible to use list comprehension from 2nd line and print from 3rd line together on single line?
Update:
I came up with this one, but it looks far fetched approach->

S = input() == 0 or set(input().split())
print([getattr(S, input().split()[0])(input().split()) for _ in range(int(input()))] == [] or sum(map(int, S)))

input() == 0 or .....: This is a way to skip past the unneeded input line, while guaranteeing the correct line gets skipped.
Functions/methods on a single line are not necessarily called in left-to-right order, but or and and need to evaluate left-to-right
because they allow for short circuit evaluation. In this case, the left side of the or is always False, so evaluation moves to the right side.
The right side evaluates to a True-like value (a non-empty list), so that right-side value becomes the value of the entire operation.
getattr(x, y)(z): getattr(x, y) is returning a function/method (not necessarily in general, but that's what it's returning here).
To use the method, it needs the parentheses and (if applicable) arguments. The (z) is not for getattr, but rather for the method that is returned by getattr.
"""

'''
16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
 '''
