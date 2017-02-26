# 理解事件

事件是什么，其实从名称来看我们就能想到些什么，而且你所想到的基本就是事件的真正意思了。在1.py的程序中
回一个运行下去，直到关闭窗口而产生了一个QUIT事件，pygame会接受用户的各种操作（比如按键盘，移动鼠标等）产生事件。
事件随时可能发生，而且量也可能会很大，pygame的做法是把一系列的事件存放在一个**队列**里，逐个的处理

# 事件检索
上一个程序中，使用了pygame.event.get()来处理所有的事件，这好像打开大门让所有的人进入。如果我们使用
pygame.event.wait(),pygame就会等到发生一个事件才继续下去，就好像你在门的猫眼上顶着外面一样，来一个
放一个，一般游戏中不实用，因为游戏往往是需要动态运作的。 而另一个方法pygame.event.poll()就好一些，
一旦调用，他会根据现在的情形返回一个真实的事件，或者一个什么都没有


事件 | 产生途径 | 参数
---|------|---
QUIT | 用户按下关闭按钮 | none
ATIVEEVENT | Pygame被激活或者隐藏 | gain, state
KEYDOWN | 键盘被按下 | unicode, key, mod
KEYUP | 键盘被放开 | key, mod
MOUSEMOTION | 鼠标移动 | pos, rel, buttons
MOUSEBUTTONDOWN | 鼠标按下 | pos, button
MOUSEBUTTONUP | 鼠标放开 | pos, button
JOYAXISMOTION | 游戏手柄(Joystick or pad)移动 | joy, axis, value
JOYBALLMOTION | 游戏球(Joy ball)?移动 | joy, axis, value
JOYHATMOTION | 游戏手柄(Joystick)?移动 | joy, axis, value
JOYBUTTONDOWN | 游戏手柄按下 | joy, button
JOYBUTTONUP | 游戏手柄放开 | joy, button
VIDEORESIZE | Pygame窗口缩放 | size, w, h
VIDEOEXPOSE | Pygame窗口部分公开(expose)? | none
USEREVENT | 触发了一个用户事件 | code

---

# 我自己的实验，打印event发现

当鼠标离开窗口时：`<Event(1-ActiveEvent {'state': 1, 'gain': 0})>`
当鼠标进入窗口时：`<Event(1-ActiveEvent {'state': 1, 'gain': 1})>`

现在总共见到这么几件event： (但上表显示了远不止，可能常用的事下面的)
1. ActiveEvent
2. KeyUp
3. KeyDown
4. ~~keyLeft~~
5. ~~KeyRight~~ `没有这两个`
6. MouseMotion
7. Quit

当我点缩小的时候：`<Event(1-ActiveEvent {'state': 4, 'gain': 0})>`
当我从下面还原的时候：
```python
<Event(1-ActiveEvent {'state': 4, 'gain': 1})>
<Event(1-ActiveEvent {'state': 2, 'gain': 1})>
#下面这个其实是失去窗口这个句柄跳到其他应用时反应的。
<Event(1-ActiveEvent {'state': 3, 'gain': 0})>
```

---

# 处理鼠标事件

`MOUSEMOTION`事件会在鼠标动作的时候发生，他有三个参数：
* buttons - 一个含有三个数字的元祖，三个值分别代表左键，中键和右键，1就是按下了
* pos - 就是位置
* rel - 代表了现在距离上一次产生鼠标事件时的距离

`<Event(4-MouseMotion {'button':(0,0,0),'pos':(428,140),'rel':(-2,2)})>`
`<Event(4-MouseMotion {'button':(0,0,0),'pos':(426,140),'rel':(-2,0)})>`
rel其实就是下面那个pos减去上面的pos
如果按下左键移动鼠标，就是移动窗口的应用，反应是
`<Event(4-MouseMotion {'button':(1,0,0),'pos':(428,140),'rel':(-2,2)})>`
`button`第一个0变成1

很多时候，我们只需要知道鼠标殿下就可以了，那就可以不同上面参数那么复杂的那么强大的事件了。
和`MOUSEMOTION`类似，有`MOUSEBUTTONUP`和`MOUSEBUTTONDOWN`两个事件
参数为：
* button - 这里相比上面少了一个s，这个值代表了哪个按键被操作
* pos - 和上面一样

_？？？？怎么获取这些参数，具体的代码实现？？？？_

---

# 处理键盘事件

键盘和游戏手柄的事件比较类似，为`KEYDOWN`和`KEYUP`
上面两个基本上同时出现的，除非你一直按着不放

```python
<Event(2-KeyDown {'scancode': 125, 'key': 274, 'unicode': u'\uf701', 'mod': 8192})>
----------
{'scancode': 125, 'key': 274, 'unicode': u'\uf701', 'mod': 8192}
274
8192
2
125
----------
<Event(3-KeyUp {'scancode': 125, 'key': 274, 'mod': 8192})>
```
上面中间部分是我打印出来的
因为我打印`dir(event)`的时候，发现
```python
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '_
_gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dict', 'key', 'mod', 'scancode', 'type', 'unicode']
```
然后，可以直接打印
```python
        if event.type == KEYDOWN:
            print '-'*10
            print event.dict
            print event.key
            print event.mod
            print event.type
            print event.scancode
            print '-'*10
```
说明这些属性直接是值，那就有办法写代码了
上下左右键的key值不一样，（其他值也不一样），**上是273，下是274，右是275，左是276**

KEYDOWN和KEYUP的参数描述如下：
* key - 按下活着放开的简直，是一个数字，估计地球上很少有人记住，所以pygame中你可以使用K_XXX来表示，
* 比如字母a就是K\_a,还有K\_SPACE和K\_RETURN等。
* mod - 包含了组合键信息，如果 mod & KMOD\_CTRL是真的话，表示用户同时按下了CTRL键，类似的还有KMOD\_SHIFT,KMOD\_ALT
* unicode - 代表了按下键的unicode值

---

# 事件过滤

并不是所有的事件都需要处理的，就好像不是所有登门造访的人都是我们欢迎的一样。比如，俄罗斯方块就无视你的鼠标，
而在游戏场景切换的时候，你按什么都是徒劳的。我们应该又一个方法来过滤掉一些我们不感兴趣的事件（当然我们可以不处理
这些没兴趣的事件，但最好的方法还是让它们根本不进入我们的事件队列，就好像在门上贴上"XXX免进"一样）,来处理所有的事件，
这好像打开大门让所有的人进入。我们使用`pygame.event.set_blocked(事件名)`来完成。如果有好多事件需要过滤，可以传递一个
列表，比如`pygame.event.set_blocked([KEYDOWN，KEYUP])`,如果你设置参数`None`,那么所有的事件又被打开了。
与之相对的，我们使用`pygame.event.set_allowd()`来设定允许的事件

# 产生事件

通常玩家做什么，pygame就产生对应的事件就可以了，不过有的时候我们需要模拟出一些事件来，
**比如录像回放的时候，我们就要把用户的操作再现一遍**

为了产生事件，必须先造一个出来，然后再传递它：
```python
my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')
#你也可以像下面这样写，看起来比较清晰（但字变多了……）
my_event = pygame.event.Event(KEYDOWN, {"key":K_SPACE, "mod":0, "unicode":u' '})
pygame.event.post(my_event)
```

你甚至可以产生一个完全自定义的全新事件

```python
CATONKEYBOARD = USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD,message="Bad cat!")
pygame.event.post(my_event)
#然后获得它
for event in pygame.event.get()
    if event.type == CATONKEYBOARD:
        print event.message
```



