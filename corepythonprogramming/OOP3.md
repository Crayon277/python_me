#

一定要谨慎，而且要意识到你正在干什么。
```python

class SortedKeyDict(dict):
  def keys(self):
    return sorted(self.keys())
```
这个是死循环，（死递归）
其实你想做的是
```python
def keys(self):
  return sorted(super(SortedKeyDict,self).keys())
```

# 多重继承

## 方法解释顺序

这个问题就是我没有覆盖的时候，在多重继承中，我调用的继承方法是哪个父类的方法（如果两个父类都有这个方法）？

![父类子类及子孙关系](http://a3.qpic.cn/psb?/V10X9IqN05vrJi/oxt0U1QHSF7VZU11WbM*SHB2HLh8.7.4whRG23D99sU!/b/dLAAAAAAAAAA&bo=SAKaAQAAAAADB*M!&rf=viewer_4)

```python
class P1:#(object):
  def foo(self):
    print 'called P1-foo()'

class P2:#(object):
  def foo(self):
    print 'called P2-foo()'
  def bar(self):
    print 'called P2-bar()'

class C1(P1,P2):
  pass

class C2(P1,P2):
  def bar(self):
    print 'called C2-bar'

class GC(C1,C2):
  pass
```

### 对于经典类,深度优先来查找

```python
>>> gc = GC()
>>> gc.foo()  #GC --> C1 --> P1
called P1-foo()
#首先在当前类查找，如果没有找到，向上查找最亲的父类C1
>>> gc.bar()  #GC --> C1 --> P1 --> P2
called P2-bar
```
### 对于新式类,广度优先来查找

取消类注释（object）

```python
>>>gc = GC()
>>>gc.foo() # GC --> C1 --> C2 --> P1
called P1-foo()
>>>gc.bar()  # GC --> C1 --> C2
called C2-bar()
```

如果想调用其他的，用非绑定的方法
`GC.__mro__`属性告诉我们查找顺序，新式类有这个属性

### 为什么要改？

![菱形效应](http://a1.qpic.cn/psb?/V10X9IqN05vrJi/UNQDYN8*os7TFEJg*qUcQmrsU4GdtgHu4pcSdJbq09A!/b/dKsAAAAAAAAA&bo=SgK0AQAAAAADANg!&rf=viewer_4)

```python
>>> class B：#(object):
...     pass
...
>>> class C：#(object):
...     def __init__(self):
...             print 'the default constructor'
...
>>> class D(B,C):
...     pass
...
>>> d = D()
the default constructor
```
当在经典类的时候是没有问题的，看图。当定义了新式类，因为B中没有重写init函数，C重写了。
但是如果还是深度优先的话，那么就会直接找到object类中的init，而会略过了C中的init函数

集成的问题是由于在新式类中，需要出现基类，这样就在继承结构中，形成了一个菱形。D的实例上溯的时候，不应当错过C。但不能两次上溯到A（因为B和C都从A派生）。

经典类沿用老式MRO，新式类使用自己的MRO

[PEP 252:使类型看起来更像类](http://www.python.org/doc/peps/pep-0252)

[Guido van Rossum 有关类型和类统一的文章：](http://www.python.org/download/releases/2.2.3/descrintro)


# 用特殊的方法定制类

特别说一下__new__和__init__
两个都是构造器，new通常用在设置不变数据类型的子类

```python
class RoundFloat(float): #带两位小数位的数值
  def __new__(cls,val): #它是类方法，所以传入参数cls
    return super(RoundFloat,cls).__new__(cls,round(val,2))
```

## 简单定制

```python
class RoundFloatManual(object):
  def __init__(self,val):
    assert isinstance(val,float),'Value must be a float'
    self.value = round(val,2)
```

```python
>>> rfm = RoundFloatManual(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in __init__
AssertionError: Value must be a float
>>> rfm = RoundFloatManual(3.2)
>>> rfm
<__main__.RoundFloatManual object at 0x10322c710>
>>> print rfm
<__main__.RoundFloatManual object at 0x10322c710>
```

之所以打印不出来是因为没有定制__str__和__repr__
str是和print有关的，repr是和python交互界面有关的

都是输出相同的信息，让两个输出一致，除了重复写相同的代码，还有就是，
因为str中的代码也是一个对象，所以可以引用，
`__repr__ = __str__`

```python
def __str__(self):
  return '%.2f'%self.value
```
