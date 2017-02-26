# 包装

？？？问题：包装和派生到底是什么区别？

从代码上看，包装本身是一个类，继承的是object（如果是新式类的话），而派生是父类子类的关系
概念其实是不一样的。

```python
class WrapMe(object):
	def __init__(self,obj):
		self.__data = obj
		"""
		包装体现在这里，obj是传入的一个类
		"""
	def get(self):
		return self.__data
		"""
		获取原数据
		"""
	def __str__(self):
		return str(self.__data)
	__repr == __str__
	def __getattr__(self,attr):
		return getattr(self.__data,attr)
		"""
		这里有一个概念授权
		对这个类调用的一切属性将终究调用原数据的属性
		"""
```

其实有点像给原来的对象穿上一件衣服，但内心还是原来的，只是外面的人看上去是新的人，但心智啊，脑子，器官还是原来的，就整容么。调用get()函数就返回原来的你，就这样。

**授权**, 书中用了一个词delegation，代理

包装类中定义了（覆盖）一个`__getattr__()`方法，当包装类`WrapMe`生成的实例通过点运算符号调用一个属性时，如果这个属性在类`WrapMe`生成的实例的`__dict__`和类`WrapMe`的`__dict__`和类`WrapMe`父类的`__dict__`中都找不到时，这个`__getattr__()`方法被调用

包装类`WrapMe`中覆盖了`__getattr__()`方法，她的返回值是调用内置方法`getattr()`，返回被包装对象的属性。通过这个`__getattr__()`方法的返回值，是返回的是被包装对象的属性，也就是说将被包装对象的属性**授权**给包装类使用。

如果被包装对象没有这个属性，那么就会报错误。

实例属性、类属性、类中定义的方法都是属性。

特殊行为没有在类型的方法列表中，不能被访问，因为他们不是属性。一个例子是，对列表的切片操作，他是内监狱类型中的。而不是像`append()`方法那样作为属性存在的。从另一个角度说，**切片操作符**是序列类型的一部分，并不是通过`__getitem__()`特殊方法来实现的。这句话没毛病，我给搞错了，`__getitem__()`是下标取值操作。切片是[1:4]这样的。

```python
def __getitem__(self,key):
	if isinstance(key,int):
		return self.__data[key]
	elif isinstance(key,slice):
		return self.__class__(self.__data[key])
```

如果key是一个整形的话就返回列表元素，如果是一个slice对象的话，就创建一个实例并返回。


？？？问题：哪里用到包装


```python
>>> class Test(object):
...     __slots__ = ('__data')
...     def __init__(self,obj):
...             self.__data = obj
...     def get(self):
...             return self.__data
...     def __getattr__(self,attr):
...             return getattr(self.__data,attr)
...
>>> a = Test(range(10))
>>> a.pop()
9
```

这个代码我想说明一个问题，就是，上面不是说当通过点运算符调用一个属性的时候，是在生成的实例的`__dict__`和类`__dict__`中以及父类的`__dict__`中找，都找不到才调用，但是上面的这段代码是用了`__slots__`属性，没有`__dict__`属性了，也就是应该是不是在`__dict__`中找了，而是在`__slots__`

更新：用了`__slots__`属性，实例，实例，实例是没有`__dict__`，但是类还是有的
```python
>>> Test.__dict__
dict_proxy({
'__module__': '__main__', 'get': <function get at 0x1028ba6e0>, '_Test__data': <member '_Test__data' of 'Test' objects>, '__getattr__': <function __getattr__ at 0x1028baa28>, '__slots__': '__data', '__doc__': None, '__init__': <function __init__ at 0x1028ba668>})
```


