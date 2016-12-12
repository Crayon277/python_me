#!/usr/bin/env python
# coding=utf-8

'''
带有参数的装饰器 是用参数做了些事，返回函数对象，而该函数对象正是以foo为其参数的装饰器

@deco2(deco_arg)
@deco1
def func():pass
等价于

func = deco2(deco_arg)(deco1(func))


装饰器实际就是函数。他们接受函数对象。当包装一个函数的时候，最终会调用它。在执行函数之前，可能有些预处理
在函数之后可能有些清理工作，所以很可能有这些代码，它定义了某个函数并在定义内的某处嵌入了对目标函数的
调用或者至少一些引用。可以考虑在装饰器中植入通用功能的代码降低程序复杂度。
可以用装饰器来：
引入日志
增加计时逻辑来检测性能
给函数加入事务的能力 *
'''

#例子，显示函数执行时间，这是一个时戳装饰

from time import ctime,sleep

def tsfunc(func):
    def wrapperFunc():
        print '[%s] %s() called'%(ctime(),func.__name__)
        return func()
    return wrapperFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
    
