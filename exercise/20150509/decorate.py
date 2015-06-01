#!/usr/bin/python
import functools
def log(text = ''):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'Begin call %s()'%func.__name__
            def temp():
                return func(*args,**kw)
            print '%s End call'%text
            return temp
        return wrapper
    print 'decorate exit'
    return decorate

@log()
def now():
    print 'hello world'

now()
