## 组合

就是在一个大点的类中创建自己的类的实例，然后实现一些其他属性和方法来增加类的功能，通过拼凑
将一些类‘组件’形成一个系统，来完成一定的功能。这个常常用于一些关系不那么紧密的类，然后是互相
向上形成一个整体的时候。

```python
class AddrBookEntry(object):
  def __init__(self,nm,ph):
    self.name = Name(nm) #实例一个name对象
    self.phone = Phone(ph) #实力一个Phone对象
```

当对象之间有更接近的关系的时候，需要一些相似的对象，但是却又少许不同的功能。使用派生

---

## 子类和派生

先讲派生和继承是什么区别。母亲生儿子，儿子被母亲生的关系，从不同的角度讲的是一件事情。
派生从父类角度，继承从子类角度

比如：上面的地址本是将name对象和phone对象给拼凑一起，但是如果我们必须创建不同类型的地址本，即
不仅仅是创建地址本的多个实例，比如希望EmplAddrbookentry类中包含更多与工作有关的属性，如员工ID和电子邮件
但PersonalAddrbookentry类不同，它包含更多基于家庭的信息，比如家庭地址、关系、生日等。

### 继承覆盖方法

不扯多远，如果子类中重写了同名的父类函数。父类的函数会被覆盖，那么这时候有两种方法可以调用父类的这个函数
一个是利用非绑定的基类方法，`P.foo(s)`

第二个方法就是用`super()`内建函数
```python
class C(P):
  def __init__(self):
    super(C,self).__init__()
    print 'calling C constructor'
```
这种的好处就是不需要明确给出任何基类的名字，不是硬编码，也就是如果改变了类继承关系，只需要改一行代码(class语句本身)就可以了


## type class

[类和类型 参考 原文链接](http://www.cnblogs.com/blackmatrix/p/5594109.html)

类型（type）和类（class）的概念不要弄混

在理解这两个之前要先把前面的经典类和新式类弄清楚

> 在Python 2.x及以前的版本中，由任意内置类型派生出的类（只要一个内置类型位于类树的某个位置），都属于“新式类”，都会获得所有“新式类”的特性；反之，即不由任意内置类型派生出的类，则称之为“经典类”。
>
> “新式类”和“经典类”的区分在Python 3.x之后就已经不存在，在Python 3.x之后的版本，因为所有的类都派生自内置类型object(即使没有显示的继承object类型)，即所有的类都是“新式类”。

 我所理解的就是新式类就是不管怎么样都要有一个继承。如果没有制定一个父类，或者如果所子类化的基本类没有父类，那这样就是创建了一个经典类

> 在很多语言中，类的实例与类的对象，只是同一事物的不同名称。而在Python中，类的对象与类的实例，是完全不同的概念。在本文中，所称的类对象，是指由class代码块执行后创建的类对象，而类的实例则是由类对象所创建的实例。这里只做简单提及，便于下文理解，要更深入的理解这个概念，可以参考“python一切皆对象”的相关知识。

```python
#以下结果出自python2.7
>>> class A():pass
...
>>> class B():pass
...
>>> a = A()
>>> b = B()
>>> a is b
False
>>> type(a) == type(b)
True
>>> type(a)
<type 'instance'>
>>> type(b)
<type 'instance'>
#所有经典类的类实例都是'instance'（实例类型）

>>> a.__class__
<class __main__.A at 0x10322b120>
>>> b.__class__
<class __main__.B at 0x10322b1f0>
>>> a.__class__ == b.__class__
False

>>> type(A)
<type 'classobj'>
>>> type(B)
<type 'classobj'>
```
```python
#以下结果是python3
>>> class A():
...     pass
...
>>> class B():pass
...
>>> a = A()
>>> b = B()
>>> type(a)
<class '__main__.A'>
>>> type(b)
<class '__main__.B'>
#这里和python2中不一样，
>>> a.__class__
<class '__main__.A'>
>>> b.__class__
<class '__main__.B'>
>>>
```
**类实例的类型，类实例的类型，类实例的类型** 注意说法，在经典类的情况中都是instance类型，所以我们用type(\*)得不到过多的信息，所以用\*.\_\_class\_\_可以得到信息。
> 需要注意的是，在Python 2.x版本中，“经典类的实例都是instance类型”，这个结论只适用于经典类。对新式类和内置类型的实例，它们的类型要更加明确。

再来看新式类在python 2 中的

```python
#python2
>>> class A(object):pass
...
>>> class B(object):pass
...
>>> a = A()
>>> b = B()
>>> type(a)
<class '__main__.A'>
>>> type(b)
<class '__main__.B'>
>>> a.__class__
<class '__main__.A'>
>>> b.__class__
<class '__main__.B'>

#与经典类不同了，type(经典类) == <type 'classobj'>
>>> type(A)
<type 'type'>
>>> type(B)
<type 'type'>
#类和类型合并
```
类型（types）和类（class）统一，是什么意思？
上面说的是 _**类实例** 的类型_ 是它创建的类 那类的类型是什么？
`python2`中的经典类中的`type(经典类) == <type 'classobj'>` 新式类是`<type 'type'>`, `python3`中的类的类型是`<class 'type'>` ，而且python3中所有类都是显式或
隐式的继承object类


> Type objects represent the various object types. An object’s type is accessed by the built-in function type(). There are no special operations on types. The standard module types defines names for all standard built-in types.
Types are written like this: <class 'int'>.

可以认为 **类是Type类的实例** 或着所有的类型都是type类，所有的新式类，都是由type类实例化创建而来，并且显式或隐式继承自object。

```python
>>> type([1,2,3])
<type 'list'>
#能说明什么，首先类和类型的统一说明[1,2,3]这是一个类，进一步证实python中一切皆对象
#[1,2,3]是一个列表对象的实例，它的类型是list
>>>type(list)
<type 'type'> #list是type类的实例
```
---
**那type类和object类** 什么关系

[鸡生蛋，蛋生鸡的关系](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html) **一定要看**

```python
#A来自上面python2新式类
>>> a.__bases__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__bases__'
#说法是'A' object
>>> A.__bases__
>>> type(A)
<type 'type'>
(<type 'object'>,)
>>> isinstance(type,object)
True
>>> isinstance(object,type)
True
```

---
经典类中，一个最大的问题是，不能对标准类型进行子类化。
