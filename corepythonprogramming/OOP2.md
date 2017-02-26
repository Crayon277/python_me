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

> The type of this object is <type 'int'>. This <type 'int'> is another object, which we will now explore. Note that this object is also called just int and <type 'int'> is the printable representation.

---
# **那type类和object类** 什么关系

[鸡生蛋，蛋生鸡的关系](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html) **一定要看**

\_\_base\_\_类属性是什么，子类的这个属性值指向父类，（最上面的父类指向object）
其实也就道出了父子的关系

type()函数返回的是\_\_class\_\_的值，因为类和类型统一了

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

> So what exactly is a Python object? An object is an axiom in our system - it is the notion of some entity. We still define an object by saying it has:
>
> Identity (i.e. given two names we can say for sure if they refer to one and the same object, or not).
>
> A value - which may include a bunch of attributes (i.e. we can reach other objects through objectname.attributename).
>
> A type - every object has exactly one type. For instance, the object 2 has a type int and the object "joe" has a type string.
>
> One or more bases. Not all objects have bases but some special ones do. A base is similar to a super-class or base-class in object-oriented lingo.

 Keep in mind that the types and bases of objects just other objects

 Example 1.1. Examining an integer object
```python
>>> two = 2 #1
>>> type(two)
<type 'int'> #2
>>> type(type(two))
<type 'type'> #3
>>> type(two).__bases__
(<type 'object'>,) #4
>>> dir(two) #5
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__',
 '__delattr__', '__div__', '__divmod__', '__doc__', '__float__',
 '__floordiv__', '__format__', '__getattribute__', '__getnewargs__',
 '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__',
 '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__',
 '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__',
 '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
 '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
 '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
 '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
 'conjugate', 'denominator', 'imag', 'numerator', 'real']

```
>
> 1
>
> Here we give an integer the name two in the current namespace.
>
> 2
>
> The type of this object is <type 'int'>. This <type 'int'> is another object, which we will now explore. Note that this object is also called just int and <type 'int'> is the printable representation.
>
> 3
>
> Hmm.. the type of <type 'int'> is an object called <type 'type'>.
>
> 4
>
> Also, the __bases__ attribute of <type 'int'> is a tuple containing an object called <type 'object'>. Bet you didn't think of checking the __bases__ attribute ;).
>
> 5
>
> Let's list all the attributes present on this original integer object - wow that's a lot.

# <type 'object'> <type 'type'>

如果我们说type，就是说这是什么类，包括类本身，这个实例是什么类，这个实例的类是什么类，因为
在python中一切皆对象。所以到了最顶层，这是一个循环，type类本身是type类。那说起object是说
我这个类继承的是什么.最顶层的就是object，type类也是继承了object。

所以type类是继承了object类，但object类的类型是type类

就像B是A的父类，a是A的实例，a的类型是A，A的类型是type，B的类型也是type
A的bases是B，B的bases是object

```python
>>> object #1
<type 'object'>
>>> type #2
<type 'type'>

>>> type(object) #3
<type 'type'>
>>> object.__class__ #4
<type 'type'>
>>> object.__bases__ #5
()

>>>type(type)
<type 'type'>
>>> type.__class__ #6
<type 'type'>
>>> type.__bases__ #7
(<type 'object'>,)

```
>
> 1 2
>
> The names of the two primitive objects within Python. Earlier type() was introduced as a way to find the type of an object (specifically, the __class__ attribute). In reality, it is both - an object itself, and a way to get the type of another object.
>
> 3 4 5
>
> Exploring <type 'object'>: the type of <type 'object'> is <type 'type'>. We also use the __class__ attribute and verify it is the same as calling type().
>
> 6 7
>
> Exploring <type 'type'>: interestingly, the type of <type 'type'> is itself! The __bases__ attribute points to <type 'object'>.
Types and classes are really the same in Python. No wonder the type() function and the __class__ attribute get you the same thing.

# 内建类型

Types and (er.. for lack of a better word) non-types (ugh!) are both objects but only types can have subcasses. Non-types are concrete values so it does not make sense for another object be a subclass. Two good examples of objects that are not types are the integer 2 and the string "hello". Hmm.. what does it mean to be a subclass of 2?

```python

>>> list #1
<type 'list'>
>>> list.__class__  #2
<type 'type'>
>>> list.__bases__  #3
(<type 'object'>,)
>>> tuple.__class__, tuple.__bases__ #4
(<type 'type'>, (<type 'object'>,))
>>> dict.__class__, dict.__bases__ #5
(<type 'type'>, (<type 'object'>,))
>>>
>>> mylist = [1,2,3] #6
>>> mylist.__class__ #7
<type 'list'>
```


>
> 1
>
> The built-in <type 'list'> object.
>
> 2
>
> Its type is <type 'type'>.
>
> 3
>
> It has one base (a.k.a. superclass), <type 'object'>.
>
> 4 5
>
> Ditto for <type 'tuple'> and <type 'dict'>.
>
> 6
>
> This is how you create an instance of <type 'list'>.
>
> 7
>
> The type of a list is <type 'list>. No surprises here.
>
> When we create a tuple or a dictionary, they are instances of the respective types.
>
> So how can we create an instance of mylist? We cannot. This is because mylist is a not a type.

# New object

## by subclassing

```python
# In Python 2.x:
class C(object): #1
    pass

# In Python 3.x, the explicit base class is not required, classes are
# automatically subclasses of object:
class C: #2
    pass

class D(object):
    pass

class E(C, D): #3
    pass

class MyList(list): #4
    pass
```

>
> 1
>
> The class statement tells Python to create a new type by subclassing an existing type.
>
> 2
>
> Don't do this in Python 2.x or you will end up with an object that is an old-style class, everything you read here will be useless and all will be lost.
>
> 3
>
> Multiple bases are fine too.
>
> 4
>
> Most built-in types can be subclassed (but not all).
>
> After the above example, C.__bases__ contains <type 'object'>, and MyList.__bases__ contains <type 'list'>.

## by instantiating

```python
obj = object() #1

cobj = C() #2

mylist = [1,2,3] #3
```

>
> 1 2
>
> The call operator (()) creates a new object by instantiating an existing object. The existing object must be a type. Depending on the type, the call operator might accept arguments.
>
> 2
>
> Python syntax creates new objects for some built-in types. The square brackets create an instance of <type 'list'>; a numeric literal creates an instance of <type 'int'>.



# 总结

[The python objects map](http://www.cafepy.com/article/python_types_and_objects/images/types_map.png)
![python obejcts map](http://www.cafepy.com/article/python_types_and_objects/images/types_map.png)
1. Dashed lines cross spacial boundaries (i.e. go from object to meta-object). Only exception is <type 'type'> (which is good, otherwise we would need another space to the left of it, and another, and another...).

2. Solid lines do not cross space boundaries. Again, <type 'type'> -> <type 'object'> is an exception.

3. Solid lines are not allowed in the rightmost space. These objects are too concrete to be subclassed.

4. Dashed line arrow heads are not allowed rightmost space. These objects are too concrete to be instantiated.

5. Left two spaces contain types. Rightmost space contains non-types.

6. If we created a new object by subclassing <type 'type'> it would be in the leftmost space, and would also be both a subclass and instance of <type 'type'>.

7. Also note that <type 'type'> is indeed a type of all types, and <type 'object'> a superclass of all types (except itself).



---
