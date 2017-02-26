# 向量
在单纯的数字运算中，居然就把方向也包含其中。想想一片叶子飘落，有他独特的轨迹，如果要人类计算出来哪个轨迹，即便可能，也是无比繁杂的，叶子懂我们的数学吗？不，他不懂，但他就是优雅的落下来了。自然有着我们尚无法理解的思考方式。

# 引入向量
(10,20)对坐标而言，就是一个固定的点，然而在向量中，它意味着x方向行进10，y方向行进20，所以坐标（0，0）加上向量（10，20）后，就达到了点（10，20）

![vector](http://eyehere.net/wp-content/uploads/2011/06/pygame-vector.jpg)

在python中，可以创建一个类来存储和获得向量！！（虽然向量的写法很想一个元组，但因为向量有很多中计算，必须使用类来完成）


```python

class Vector2(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "(%s,%s)"%(self.x,self.y)
	
	@classmethod
	def from_points(cls,P1,P2):
		return cls(P2[0]-P1[0],P2[1]-P1[1])
	
A = (10.0,20.0)
B = (30.0,40.0)
AB = Vector2.from_points(A,B)
print AB
```

# 向量的大小
向量的大小可以简单的理解为那根箭头的长度，

```python
def get_maginitude(self):
	return math.sqrt(self.x**2+self.y**2)
```
把这几句假如到刚刚的Vector2里，我们的向量类就多了计算长度的能力，但这里用到了math，一开始要import一下

# 单位向量
向量有着大小和方向两个要素。单位向量是大小为1的向量，还能把把任意向量方向不变的缩放（体现在数字上就是x和y等比例缩放）到一个单位向量，这叫向量的规格化，

```python
def normalize(self):
	magnitude = self.get_maginitude()
	self.x /= magnitude
	self.y /= magnitude
```

使用了normalize方法以后，向量就成了一个单位向量。
问题：
想想看怎么把原来的向量保存下来，也就是正规化的向量另外保存，不要覆盖原来的怎么写

```python
def normalize_save(self):
	magnitude = self.get_magnitude()
	return self.x/magnitude,self.y/magnitude
```

这样只是返回了坐标，如果要返回向量类呢？？
```python
#暂时只想到这一种
def normalize_save(self):
	magnitude = self.get_magnitude()
	return self.__class__(self.x/magnitude,self.y/magnitude)

```

# 向量运算
点B由A出发，通过向量AB到达，C则由B到达，通过BC：C直接由A出发的话，就得经由向量AC
![向量运算](http://eyehere.net/wp-content/uploads/2011/06/pygame-vector-addition.jpg)

向量AC = 向量AB + 向量BC
把各个方向分别想家，我们就得到了向量的加法运算法则，减法也是一样
```python
def __add__(self,other):
	return self.__class__(self.x+other.x,self.y+other.y)
def __sub__(self,other):
	return self.__class__(self.x-other.x,self.y-other.y)
```
其实向量跟坐标没什么大关系，因为可以平移，而且向量的(x,y)不变。
两个下划线`__`为首的函数，在python中一般就是重载的意思。

![向量乘法](http://eyehere.net/wp-content/uploads/2011/06/pygame-vector-multiply.jpg)
```python
def __mul__(self,scalar):
	return self.__class__(self.x * scalar,self.y*scalar)
def __div__(self,scalar):
	return self.__class__(self.x / scalar,self.y/scalar)
```
**向量运算被广泛的用来计算到达某个位置时间的中间状态，比如我们知道一辆坦克从A到B，中间由10帧，那么很显然，把步进向量通过(B-A)/10计算出来，每次在当前位置加上就可以了。**

# 更好的向量类
别人写的向量类库`gameobjects`

# 变速运动
用向量实现，因为向量有方向，所以在做加减的时候，可以按实际情况

# 动画总结
* 所谓的动画，不过是在每一帧上，相对前一阵把精灵的坐标在加减一些而已
* 使用时间来计算加减的量以在不同性能的计算机上获得一致的动画效果
* 使用向量来计算运动的过程来减轻我们的劳动，在3D的情况下，使用Vector3便可以了。

研究一下vector的这个类






