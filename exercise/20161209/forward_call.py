#!/usr/bin/env python
# coding=utf-8

# 有关前向引用的问题

def foo ():
    print 'in foo()'
    bar()

foo() #这里如果调用了foo会报错，因为没有定义bar

def bar():
    print 'in bar'

foo() # 这里调用foo不会报错，因为bar已经被定义了

'''
这里可能会有一个疑问，为什么foo里面有bar却可以在bar声明之前定义。
因为虽然foo里面对bar的调用是在bar定义之前，但是对foo的调用却是在bar之后，
也就是先声明foo，再声明bar，接着调用foo，但是在这个时候，bar已经存在了，所以是没有问题的。
'''
