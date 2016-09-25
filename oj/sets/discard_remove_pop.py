#!/usr/bin/env python
# coding=utf-8


'''
#我的

n = input()
s = set(map(int, raw_input().split()))
for _ in range(input()):
    order=raw_input().split()
    cmd = order[0]
    arg = order[1:]
    cmd = 's.'+cmd+'('+''.join(arg)+')'
    eval(cmd)
print sum(s)
#关于分解这个命令，给忘了。翻了以前的记起来的。
因为pop没有带参数，而discard, remove 是带参数的，所以如果用order[0],order[1]这样来引用cmd,arg是会出现错误的
因为pop没有。然后想order.pop()，然后用＊解包，貌似加法中还不能用。
用切片！！！
然后注意要用eval，其实eval的参数就是命令，就是对字符串操作，arg里面怎么提取出来那个值，还要不管是不是有没有这个值。
'''

#nb
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*raw_input().split()+['']))
#字符串的操作嘛！！！format函数。
print sum(s)
'''
1.［‘1’，‘2’］ ＋ ［‘3’］ ＝ ［‘1’，’2‘，’3’］ 列表的加法
2. *貌似优先级比+低，所以+先做
3. 为什么要加一个［‘’］，保证至少有2个以上的参数
4. '{0}{1}'.format([1,2])这会报错参数不够，所以可以把format（），这个（）看作是一个元祖的括号，
    里面有几个参数，才是对应位置参数。[1,2]只能对应上{0}
'''

"""
#python 3

n = int(input())
s = set(map(int, input().split()))
t = int(input())
for i in range(t):
    c, *args = map(str,input().split())
    getattr(s,c) (*(int(x) for x in args))
print sum(s)

getattr函数！！！  类似于

getattr(...)
    getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.


The getattr function uses the same lookup rules as ordinary attribute access, and you can use it both with ordinary attributes and methods:

result = obj.method(args)

func = getattr(obj, "method")  #此时交互命令行输入func会提示类似<built in method....at 0x12345678>,所以它是一个地址
result = func(args)
or, in one line:

result = getattr(obj, "method")(args)
Calling both getattr and the method on the same line can make it hard to handle exceptions properly. To avoid confusing AttributeError exceptions raised by getattr with similar exceptions raised inside the method, you can use the following pattern:

try:
    func = getattr(obj, "method")
except AttributeError:
    ... deal with missing method ...
else:
    result = func(args)
The function takes an optional default value, which is used if the attribute doesn’t exist. The following example only calls the method if it exists:

func = getattr(obj, "method", None)
if func:
    func(args)
Here’s a variation, which checks that the attribute is indeed a callable object before calling it.

func = getattr(obj, "method", None)
if callable(func):
    func(args)

"""
