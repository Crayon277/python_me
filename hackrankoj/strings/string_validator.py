#!/usr/bin/python
#-*- coding: utf-8 -*-
# 问题
# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


'''
方法1（错误）
task = ['isalnum()','isalpha()','isdigit()','islower()','isupper()']
string = raw_input()

result = [eval('string.'+item) for item in task]
print result

和要求不对！！
Output Format
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
是any,只要有一个就行，
也就是qA2 中，有一个是alphanumeric,那就打印True,有一个是alpha就打印True ，其它类推。
而isalnum 这些都是检查整个字符串的。
'''


"""
方法2

就要对string中每个字符进行对比。
string = raw_input()
d = {'alnum':False,'alpha':False,'digit':False,'lower':False,'upper':False}
for c in string:
# 循环了一次，对每个字符检查一遍是否是如下的几种状态。但是前面一旦有，就不必检查了。
    if not d['alnum']:
        d['alnum']=c.isalnum()
    if not d['alpha']:
        d['alpha']=c.isalpha()
    if not d['digit']:
        d['digit']=c.isdigit()
    if not d['lower']:
        d['lower']=c.islower()
    if not d['upper']:
        d['upper']=c.isupper()
print d['alnum']
print d['alpha']
print d['digit']
print d['lower']
print d['upper']
这里我用的字典。
"""

"""
方法3

#可以用数组和下标。
task = ['isalnum()','isalpha()','isdigit()','islower()','isupper()']
string = raw_input()
d=[False,False,False,False,False]
alnum,alpha,digit,lower,upper = 0,1,2,3,4
for c in string:
    d=[(d[i] or eval('c.'+task[i])) for i in range(5)]
    #d=map(lambda x,y:x or y,d,[eval('c.'+task[i]) for i in range(5)])
    #map是列表算好，然后一起来，上面那个是列表的每一项算好生成一个列表
for _ in range(5):
    print d[_]
"""


"""
s = input()
for f in [ "isalnum", "isalpha", "isdigit", "islower", "isupper" ] :
    print( any( eval( "c." + f + "()" ) for c in s ) )
和我的解法相似，他是先对每一个字符进行一类检查，外循环是每一类检查，内循环是字符，如对每一个字符都进行isalnum, 然后对每一个字符都进行isalpha
我的是，先对第一个进行所有的检查，再对第二个字符进行所有的检查，所以我的外循环是字符，内循环是每一类检查，

"""

#牛人的方法 一行代码
# uses all five string methods on each character in input string
# prints True if at least one character made the method return True
print "\n".join([str(any(i)) for i in (list(zip(*[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in raw_input()])))])
#zip用法。 看例子
# x = [1,2,3]
# y = [4,5,6]
# zip(x,y)
# 显示的是 [(1,4),(2,5),(3,6)] 相同索引的打包起来，总索引取值最小的那个列表
# 结果等于 map(None,x,y)

#为什么要str(any(i)),直接any(i)不行么？print True 是True是可以的，关键是join()函数参数如果是list，list里面必须要是字符串
# 报错TypeError,sequence item0: expected string, int(or other)found

"""
 *-operator to unpack the arguments out of a list or tuple:

>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

>>>
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

但是 字典d中的key要与函数parrot中的形参名字相同！！！
不然会报错 got an unexpected keyword argument

"""


"""
# 上面的分解
# user input

s = raw_input()

# uses all 5 methods on each character and creates a list for each,
# containing the results of each method used on the character.
newList = [[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]
#每个字符的每个比较 [[第一个字符的5个比较],[第二个字符的5个比较],[第三个字符的5个比较],[第四个字符的5个比较],[第五个字符的5个比较]]
# rotates lists clockwise to get lists of each method instead
rotated = list(zip(*newList))
# 将同类型比较的放在一起！[[都是isalnum的],[都是isalpha的],[都是isdigit的],[都是islower的],[都是isupper的]]
# prints whether or not a True is present for each List
print '\n'.join([str(any(i)) for i in rotated])   #any(iter)
"""

"""
官方解法
S = raw_input()
print any([char.isalnum() for char in S])
print any([char.isalpha() for char in S])
print any([char.isdigit() for char in S])
print any([char.islower() for char in S])
print any([char.isupper() for char in S])
"""
