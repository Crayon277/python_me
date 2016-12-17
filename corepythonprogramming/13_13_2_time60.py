#!/usr/bin/env python
# coding=utf-8

'''
创建一个简单的应用，用来操作时间，精确到小时和分
可用来跟踪职员的工作时间，ISP用户在线时间，，在扑克比赛中玩家总时间等。
'''

class Time60(object):
    def __init__(self,hour,minute):
        self.hr = hour
        self.min = minute

    def __str__(self):
        return '%d:%d'%(self.hr,self.min)
    __repr__ = __str__

    #下一步干什么呢？ 可考虑与我们的对象进行交互，比如在时间片的应用中，有
    #必要把Time60的实例放到一起让我们的对象执行所有有意义的操作。比如时间相加

    def __add__(self,other):
        #return Time60(self.hr+other.hr,self.min+other.min)
        #上面这种，可以，但是如果改了类名，那么就要进行代码修改
        return self.__class__(self.hr+other.hr,self.min+other.min)
        #这种是一个更面向对象的方法，由于self.__class__与Time60相同，
        #上面执行的结果就是Time60()实例化这个对象并返回

    def __iadd__(self,other):
        """
            是用来支持+=操作的，返回值必须是self.覆盖原位操作。
            修改，但没有创建一个新对象！！！
        """
        self.hr += other.hr
        self.min += other.min
        return self
if __name__ == "__main__":
    mon = Time60(10,30)
    tue = Time60(11,15)

    print mon,tue
    print mon+tue
    mon+=tue
    print mon
