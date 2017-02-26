```
#!/usr/bin/env python
# coding=utf-8

class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe = safe

        self.iter = iter(data)  #接受一个可迭代的数据类型
        """
        知道这里为什么要转化为iter对象了，因为后面要用到next(）方法
        而测试数据是range(10)是一个列表，如果不转化，列表是没有
        next()方法的。如果不转化，可以用
        retval.append(self.data.pop(0))来完成这个功能
        """
    def __iter__(self):
        return self  #将一个对象声明为迭代器的方式

    def next(self,howmany=1):
        retval=[]
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next()) #如果next接收参数为2，返回的是两个元素的列表。
            except StopIteration:
                if self.safe:
                    break # 不报错
                else:
                    raise # safe如果是False就报错
        return retval

if __name__=="__main__":
    a = AnyIter(range(10))#a将参数转化为迭代对象当作数据成员
    i = iter(a) # ???? 怎么将a转化为迭代对象。好像是的。
    #a是一个对象，又将a转化为迭代对象？
    #iter(a) 是调用了a的__iter__()函数，其实就是返回self给i，i和a指向的是一样的。所以i和a没什么区别应该
    for j in range(1,5):
        print j,':',i.next(j) #为什么不能直接a.next
    #其实我这个的问题就是问的是i调用next是调用的a的next么？？？从结果上来看，是的
    '''
    #i.next(j) 改成a.next(j)也是可以的，结果一样
    1 : [0]
    2 : [1, 2]
    3 : [3, 4, 5]
    4 : [6, 7, 8, 9]
    '''
    # for i in a:
        # print i
    '''
    #这个其实就是直接调用a的next，然后当中的参数是1
    [0]
    [1]
    [2]
    [3]
    [4]
    [5]
    [6]
    [7]
    [8]
    [9]
    '''
```
![代码结构图](http://b287.photo.store.qq.com/psb?/V10X9IqN05vrJi/hgbGFw5qYobyMsDy*n9RwtY8vAYdYLQoPDpk389xLf0!/b/dB8BAAAAAAAA&bo=gALwAgAAAAADB1I!&rf=viewer_4)
