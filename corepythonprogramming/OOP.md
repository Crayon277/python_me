# 面向对象编程

从简单控制流中按步的指令序列进入到更有组织的方式中，依靠代码快可以形成命名子程序和完成既定的功能。

一个例子：
模拟一台汽车维修店，可以让你停车进行维修。我们需要建**_两个一般实体_**：
处在一个“系统”中并与其交互的人类，和一个修理店，它定义了物理位置，用于人类活动。因为
前者有更多不同的类型，我将首先对它进行描述，然后描述后者。在此类活动中，_**一个名为 Person
的类被创建以用来表示所有的人。Person 的实例可以包括消费者(Customer)，技工(Mechanic)，还
可能是出纳员(Cashier)。**_这些实例具有相似的行为，也有独一无二的行为。**比如，他们能用声音进
行交流，都有 talk()方法，还有 drive_car()方法。不同的是，技工有 repair_car()方法，而出纳
有 ring_sale()方法。技工有一个 repair_certification 属性，而所有人都有一个 drivers_license
属性。**
最后，所有这些实例都是一个检查(overseeing)类 RepairShop 的参与者，后者具有一个叫
operating_hours 的数据属性，它通过时间函数来确定何时顾客来修车，何时职员技工和出纳员来上
班。RepairShop 可能还有一个 AutoBay 类，拥有 SmogZone,TireBrakeZone 等实例，也许还有一个叫
GeneralRepair 的实例。
我们所编的 RepairShop 的一个关键点是要展示类和实例加上它们的行为是如何用来对现实生活
场景建模的。同样，你可以把诸如机场，餐厅，晶蕊，医院，其至一个邮订音乐公司想像为类，它
们完全具备各自的参与者和功能性。

---

## 类

类是一种数据结构，可以用它来定义对象，对象是把数据值和行为特性融合在一起

![类和实例](http://a2.qpic.cn/psb?/V10X9IqN05vrJi/H7QZ2K1pChsOVNTB547sz5Alyk36zTmjI3gTxlkVkTg!/b/dLIAAAAAAAAA&bo=mAFVAQAAAAADB.8!&rf=viewer_4)

![类和实例2](http://a2.qpic.cn/psb?/V10X9IqN05vrJi/pzuM0HjDCbPJBfDsXXr8PYQ7bkJXO1b32rQxAA.Klf0!/b/dLIAAAAAAAAA&bo=mQFRAQAAAAADAO0!&rf=viewer_4)

从上面两幅图可以看出，这个生产玩具工厂的玩具模型就是一个一个类，然后生产出来的一个一个玩具就是一个实例，而一个一个实例我又可以给涂上不一样的颜色，各自的颜色可以更改。那就是一个一个实例是相互可以自己定制了。这就好比实例的属性

类是对象的定义，实例是“真正的实物”，他存放了类中所定义的对象的具体信息。对象只是一个我们心中的一个想描述的客观事物。

`myObject = myClass()`这是是实例化一个类，如果没有把实例保存在一个变量中，`myClass()`它就没有用了，会被_**自动垃圾收集器回收**_，因为没有任何引用指向这个实例。也就是刚刚分配了一个内存，随即便释放了。

```python
def mydata():
  pass

myobj = mydata()
myobj.x = 5
```
上面的例子说明类可以拿来当作命名空间用。这样更好的组织代码中的逻辑关系。注意myobj.x是实例属性，不是类属性，是实例对象myobj独有的属性。

有个概念叫新式类和经典类，新式类最大的不同在于，所有新式类必须继承至少一个父类

```python
>>> type(newClass)
<type 'type'>
>>> type(classicClass)
<type 'classobj'>
>>> myNewClass = newClass()
>>> myClassicClass = classicClass()
>>> type(myNewClass)
<class '__main__.newClass'>
>>> type(myClassicClass)
<type 'instance'>
```
---

## 类方法

### 函数和方法之间的区别是什么

函数是一段代码，通过名字来进行调用。它能将一些数据（参数）传递进去进行处理，然后返回一些数据（返回值），也可以没有返回值。

所有传递给函数的数据都是显式传递的。

方法也是一段代码，也通过名字来进行调用，但它跟一个对象相关联。方法和函数大致上是相同的，但有两个主要的不同之处：

1. 方法中的数据是隐式传递的；
2. 方法可以操作类内部的数据（请记住，对象是类的实例化–类定义了一个数据类型，而对象是该数据类型的一个实例化）
以上只是简略的解释，忽略了作用域之类的问题。

对于 1），你应当再加上“ 方法在 C++ 中是被称为成员函数”。因此，在 C++ 中的“方法”和“函数”的区别，就是“成员函数”和“函数”的区别。此外，诸如 Java 一类的编程语言只有“方法”。所以这时候就是“静态方法”和“方法”直接的区别。

对于2），你应当补上方法可以操作已在类中声明的私有实例（成员）数据。其他代码都可以访问公共实例数据。

方法和对象相关；

函数和对象无关。

Java中只有方法，C中只有函数，而C++里取决于是否在类中。

## 绑定，未绑定什么意思

### 类的数据属性
```python
>>> class C(object):
...     foo = 100
...
>>> C.foo
100
>>> C.foo = C.foo + 1
>>> C.foo
101
```
这个例子表示了没有任何类实例的引用，foo属性表示_**静态变量**_，他们表示这些数据食欲他们所属的累对象绑定的，不依赖于任何类实例。

静态成员通常仅用来跟踪与类相关的值。大多数情况下，会考虑用实力属性。

### 方法

```python
>>> class myclass(object):
...     def myNoActionMethod(self):
...             pass
...
>>> mc = myclass()
>>> mc.myNoActionMethod()
>>> myNoActionMethod()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myNoActionMethod' is not defined
#myNoActionMethod不是属于全局空间中的名字，如果它在顶层作为函数被定义，调用成功
>>> myclass.myNoActionMethod()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unbound method myNoActionMethod() must be called with myclass instance as first argument (got nothing instead)
#由类对象调用此方法失败
```
Python严格规定，没有实例，方法是不能被调用的。这种限制即python所描述的绑定概念。
**方法必须绑定（到一个实例）才能直接被调用**。非绑定的方法可能可以被调用，但实例对象一定要明确给出，才能确保调用成功，不管是否绑定，方法都是他所在的类的固有属性，即使他们几乎总是通过实例来调用的。

### 绑定和方法的调用

**方法仅仅是类内部定义的函数（这意味着方法是类属性而不是实例属性）**
方法只有在其所属的类拥有实例的时候，才能被调用。当存在一个实例时，方法才被认为是绑定到那个实例了，没有实例时方法就是未绑定的。

任何一个方法定义中的第一个参数都是变量self，他表示调用此方法的实例对象。

#### 调用绑定方法

```python
>>> myclass.myNoActionMethod(mc)
>>> mc.myNoActionMethod()
```
当在一个实例中调用一个绑定的方法时，self不需要明确的传入了，这算是‘必须声明self作为第一个参数’对你的报酬。当还没有一个实例并且需要调用一个非绑定方法的时候必须显示的传递self参数。

#### 调用非绑定方法

需要调用一个还没有任何实例的类中的方法的一个主要的场景就是：_**你在派生一个子类，而你要覆盖父类的方法**_。

```python
>>> class A(object):
...     def __init__(self,a):
...             self.name = a
...
>>> class B(A):
...     def __init__(self,b):
...             A.__init__(self,b) #调用A的init，这里的A是类对象，需要传入self参数，
...             self.age = 0

```

```python
class A(object):
    def __init__(self,a):
        self.name = a
    def wts_name(self):
        print self.name

class B(A):
    def __init__(self,b,c):
        A.__init__(self,b)
        self.age = c
    def info(self):
        A.wts_name(self)
        print self.age

lily = B('lily',23)
lily.info()
```
![上面的python内构图](http://a3.qpic.cn/psb?/V10X9IqN05vrJi/4Tq9efpEi9hf45NAeZYSTEkNut6WNOf*IysInFq9iac!/b/dB8BAAAAAAAA&bo=6wH8AgAAAAADBzY!&rf=viewer_4)

### 静态方法和类方法

通常的方法需要一个实例（self）作为第一个参数，并且对于（绑定的）方法调用来说，self是自动传递给这个方法的。而对于_**累方法**_而言，需要类而不是实例作为第一个参数，它是由解释器传给方法。类不需要特别的命名，类似self，不过很多人使用cls作为变量的名字

``` python

>>> class TestStaticMethod():
...     @staticmethod
...     def foo():
...             print 'calling static method foo()'
...     foo = staticmethod(foo)
...
>>> class TestClassMethod():
...     @classmethod
...     def foo(cls):
...             print 'calling class method foo()'
...             print 'foo() is part of class:',cls.__name__
...     #foo = classmethod(foo)
...

>>> tsm = TestStaticMethod()
#既可以通过类实例访问，又可以通过类对象访问
>>> tsm.foo()
calling static method foo()
>>> TestStaticMethod()
<__main__.TestStaticMethod instance at 0x103228200>
>>> TestStaticMethod.foo()
calling static method foo()
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined

>>> tcm = TestClassMethod()
#既可以通过类实例访问，又可以通过类对象访问
>>> tcm.foo()
calling class method foo()
foo() is part of class: TestClassMethod
>>> TestClassMethod.foo()
calling class method foo()
foo() is part of class: TestClassMethod
>>>
```

#### 静态方法、类方法使用区别或者说使用场景
1. 类方法用在模拟java定义多个构造函数的情况。
由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。

```python
class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

book1 = Book("python")
book2 = Book.create("python and django") # 可以用来当作构建函数
print(book1.title)
print(book2.title)
```
2. 类中静态方法方法调用静态方法的情况。
下面的代码，静态方法调用另一个静态方法，如果改用类方法调用静态方法，可以让cls代替类，
让代码看起来精简一些。也防止类名修改了，不用在类定义中修改原来的类名。

```python
class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method(): #静态方法
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls): #类方法
        return cls.averag(cls.X, cls.Y)

foo = Foo()
print(foo.static_method())
print(foo.class_method())
```
静态方法用类名，类方法有一个传递的参数cls当作类名。

3. 继承类中的区别

```python
class Foo:
    x= 1
    y = 2
    @staticmethod
    def average(*args):
        return sum(args)/float(len(args))

    @staticmethod
    def static_method():
        return Foo.average(Foo.x,Foo.y)

    @classmethod
    def class_method(cls):
        return cls.average(cls.x,cls.y)

class Son(Foo):
    x = 3
    y = 5

    @staticmethod
    def average(*args):
        '''
        重载父类的average函数
        '''
        return sum(args)/float(3)


p = Son()
print p.static_method() #1.5
#在子类实例中调用继承下来的父类静态方法，用的还是父类的x，y以及父类的average函数

print p.class_method()  #2.66666666667
#调用继承下来的类方法，因为有cls，是将Son类对象传递进去，所以用的子类的x,y以及子类的average函数

print Son.static_method() #1.5
print Son.class_method()  #2.66666666667
print Foo.static_method() #1.5
print Foo.class_method() #1.5

```
