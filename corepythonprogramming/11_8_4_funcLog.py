#!/usr/bin/env python
# coding=utf-8

'''
这个例子展示了带有参数的装饰器，该参数最终决定哪一个闭包会被用。

'''
from time import time

def logged(when):
    '''
    这个logged内定义了三个内部函数，log,pre_log,post_log
    @logged(arg)通过arg决定使用哪个装饰器。pre_log,还是post_log,
    同时，pre_log,和post_log里面调用了log函数。
    其实这里当我给一个函数hello(arg)装饰了logged('pre'),发生了这么几件事情，logged('pre')返回了
    pre_log，pre_log接收了hello函数参数，返回wrapper，此时原来hello指向的是pre_log里面的wrapper

    这里有一个问题就是hello(arg)中的arg是怎么传到wrapper中去的，这个机制是什么？？？
    为什么有这个问题是因为，当pre_log接收f的时候，它的参数是怎么到了wrapper了？代码中没有明确的给出这个过程
    我只是在wrapper中定义了它的参数，f的参数怎么会传到wrapper的参数中去？？？


    然后调用hello函数的话执行的是33-34行代码，f为hello自己本身。为什么要用return 不能直接f（），
    这要看f的具体实现，如果是要有返回值的话。虽然给加了装饰，但是也是有返回值的啊。装饰不会影响原来的功能。

    '''
    def log(f,*nkw,**kw): # 用来打印函数的一些信息，
        print '''
        function name:{}
        arg1         :{}
        arg2         :{}'''.format(f,nkw,kw)

    def pre_log(f):
        '''
        这里的wrapper是pre_log 的闭包
        '''
        def wrapper(*nkw,**kw):
            log(f,*nkw,**kw)
            return f(*nkw,**kw)
        return wrapper
    def post_log(f):
        '''
        这里的wrapper是post_log的闭包
        '''
        def wrapper(*nkw,**kw):
            start = time()
            try:
                return f(*nkw,**kw)
            finally:
                log(f,*nkw,**kw)
                print 'usage time :',time()-start
        return wrapper

    '''
    两个*log（）函数都包括了一个名叫wrapper 的闭包。当合适将其写入日志的时候，它便会调用目标函数。这个函数
    返回了包括好的函数对象，该对象随后将被重新复制给原始的目标函数标识符。
    '''

    try:
        return {'pre':pre_log,'post':post_log}[when]
        #上面的语句返回调用哪个真正装饰器
    except KeyError ,e:
        print 'argument of logged must be pre or post'
'''
那么logged函数里面的pre_log,post_log 也叫闭包么？闭包的概念是对外部作用域的变量进行引用。
两个wrapper是闭包，因为引用了f,pre_log,post_log也是，因为引用了log函数！！
闭包就是体现在这里，我没有对外面说我有log函数，但是我只是用pre_log来装饰，但其实它的作用是用到了log
这里的作用域跟平常的全局什么的不一样，闭包的此法变量不属于全局名称空间域或者局部的。而属于其他的名称空间
带着’流浪‘的作用域。
对，就是让我想到了对象的private成员和public成员，只有对象内部的成员才能访问private
注意者不同于对象因为那些变量是存活在一个对象的名称空间但是闭包变量存活在一个函数的名称空间和作用域

'''

@logged('post')
def greet(msg):
    print msg

greet('hello world')

'''结果如下

hello world

        function name:<function greet at 0x10073a6e0>
        arg1         :('hello world',)
        arg2         :{}
usage time : 4.6968460083e-05

'''



'''
这个例子的闭包中含有闭包，和之前简单的闭包有什么区别之前的
'''
#简单形式的装饰器
def simple_log(func):
    def wrapper(*args,**kargs):
        print 'function %s has been called'%func.__name__
        return func(*args,**kargs)
    return wrapper
'''
上面那个最终的效果就是
@post_log
def greet....

只是post_log需要再求，这样就灵活了，我们想要哪个装饰器就改一下参数就行了。
'''
@simple_log
def hello(name):
    print 'hello,',name

hello('word')

'''结果如下

function hello has been called
hello, word

'''
