# 偏函数应用
这个意思就是我们有一些函数。类似重载，我们要重新定义函数的行为。但是
偏函数不是重新定义函数的行为，它是要将函数的一些参数给固定，然后我们
可以直接调用，这样就不用去实现新的只是需要将原来函数的一些参数固定的
函数了。

```python
>>> from functools import partial
>>> from operator import add,mul
>>> add1 = partial(add,1) # 我们经常要让一个数+1，原来我们要定义add(1,x)
>>> add1(10) # 现在我们相当于将原来add的两个参数中的一个参数固化为固定参数
11
>>> mul100 = partial(mul,100)
>>> mul100(11)
1100
#另一个例子
>>> baseTwo = partial(int,base=2)#这里的例子是关键字参数的PFA
>>> baseTwo('110001')
49
#像这种有关键字参数的函数要生成偏函数，如果在偏函数的创建中没有指定关键字，可能
#造成参数以错误的顺序传入的问题。因为固定参数的总是放在运行时刻的参数的左边
#比如add1(x) = add(1,x) 这个参数1是在原函数参数列表的左边
#假如上面的baseTwo = partial(int,2),那baseTwo(x) = int(2,x)
>>> baseTwoBad = partial(int,2)
>>> baseTwoBad('110001')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: an integer is required
```

### 警惕关键字
固定参数总是放在运行时刻参数的左边，看例子
```python

>>> def myfunc(arg1,arg2 = 'default',*nkw,**kw):
...     print 'arg1',arg1
...     print 'arg2',arg2
...     for each in nkw:
...             print 'addtinal unkown argument',each
...     for each in kw.keys():
...             print 'addtinal keyword {} argument {}'.format(each,kw[each])
...
>>> myfunc(1,2,3,4)
arg1 1
arg2 2
addtinal unkown argument 3
addtinal unkown argument 4

>>> l = (1,2,3,4)
>>> ld={'x':1,'y':4}
>>> myfunc1 = partial(myfunc,2) # 没有指定关键字
>>> myfunc1(1,2,3,4) # 相当于 myfunc(2,1,2,3,4)
arg1 2 # 因为上面没有指定关键字，2是被传入到arg1
arg2 1
addtinal unkown argument 2
addtinal unkown argument 3
addtinal unkown argument 4

>>> myfunc2 = partial(myfunc,arg2='hello')
>>> myfunc2(1,2,3,4)
#相当于myfunc(1,2,3,4,arg2='hello') 但是arg2和前面的未知参数冲突
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: myfunc() got multiple values for keyword argument 'arg2'


```
