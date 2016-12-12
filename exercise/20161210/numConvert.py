#!/usr/bin/env python
# coding=utf-8

'''
将函数名作为参数进行传递！

函数对象的引用，和函数对象的调用的区别

>>> def foo():
...     print 'in foo'
...
>>> foo()
in foo
>>> bar = foo
>>> bar()
in foo
>>> def tool(argfunc):
...     argfunc()
...
>>> tool(foo)
in foo
>>>


'''
#这个程序是接受一个内置函数作为参数，然后在函数内用内置函数转换数列
def convert(func,myseq):
    print 'convert each elemnts to the type',func.__name__
    return [func(x) for x in myseq]

myseq = (123,45.67,-6.2e8,999999999999L)
print convert(int,myseq)
print convert(float,myseq)
print convert(long,myseq)
