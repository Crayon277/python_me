>掌握了小小的像素，我们可以使用更加复杂一点的东西了，对，就是图像，无数的像素的集合~还记得上次我们为了生成的一张图片，花了无数时间，还好一般游戏不会在游戏的过程中动态生成图像，都是将画好的作为资源封装到游戏中。对2D游戏，图像可能就是一些背景、角色等，而3D游戏则往往是大量的贴图。
>虽然是基础，这里还是要罗嗦一下，之前说的RBG图像，在游戏中我们往往使用RGBA图像，这个A是alpha，也就是表示透明度的部分，值也是0~255，0代表完全透明，255是完全不透明，而像100这样的数字，代表部分透明。你可以使用多种软件创建含有Alpha通道的图片，具体的网上查查吧……

>这个世界上有很多存储图像的方式（也就是有很多图片格式），比如JPEG、PNG等，Pygmae都能很好的支持，具体支持的格式如下：

>* JPEG（Join Photograhpic Exper Group)，极为常用，一般后缀名为.jpg或者.jpeg。数码相机、网上的图片基本都是这种格式。这是一种有损压缩方式，尽管对图片质量有些损坏，但对于减小文件尺寸非常棒。优点很多只是不支持透明。
>* PNG（Portable Network Graphics）将会大行其道的一种格式，支持透明，无损压缩。对于网页设计，软件界面设计等等都是非常棒的选择！
>* GIF 网上使用的很多，支持透明和动画，只是只能有256种颜色，软件和游戏中使用很少
>* BMP Windows上的标准图像格式，无压缩，质量很高但尺寸很大，一般不使用
>* PCX
>* TGA
>* TIF
>* LBM, PBM
>* XPM
> 
# 使用Surface对象
对于pygame而已，加载图片就是pygame.image.load,给他一个文件名然后就还给你一个surface对象。
尽管读入的图像格式各不相同，surface对象隐藏了这些不同，你可以对一个Surface对象进行涂画，变形，复制等
操作，事实上，屏幕也只是一个surface，pygame.display.set_mode就返回了一个屏幕surface对象。

# 创建Surface对象
一种方法就是刚刚说的pygame.image.load,这个surface有着和图像相同的尺寸和颜色；另外一种方法是指定
尺寸创建一个空的surface，下面的语言创建一个256*256像素的surface
`bland_surface = pygame.Surface(256,256)`
如果不指定尺寸，那么就创建一个和屏幕一样大小的

还有两个参数可选，
第一个参数是flags
HWSURFACE - 类似于前面讲的，更快！不过最好不设定，Pygame可以自己优化
SRCALPHA - 有Alpha通道的surface,如果你需要透明，就要这个选项。这个选项的使用需要第二个参数为32

第二个参数是depth，和pygame.display.set_mode中的一样，可以不设定，pygame会自动设的和display一致。不过如果你使用了SRCALPHA，还是设置32吧：
`bland_alpha_surface = pygame.Surface((256,256),flags=SRCALPHA,depth=32)`

# 转换Surfaces
通常你不用在意surface里的具体内容，不过也许需要吧这些surface转换一下以获得更高的性能
`background = pygame.image.load(background_image_filename).convert()`
`mouse_cursor = pygame.image.load((mouse_image_filename).convert_alpha()`
第一句是普通的转换，相同与display；第二句是带alpha通道的转换，如果你给convert或者convert_alpha一个
surface对象作为参数，那么这个会被作为目标来转换。????这句话什么意思？？？

# 矩形对象
一般来说在制定一个区域的时候，矩形是必须的，比如在屏幕的一部分画东西。在pygame中矩形对象极为常用，
它的指定方法可以用一个四元素的元祖，或者两个元素的元祖，前两个为左上坐标，后两个为右下坐标。
```python
my_rect1 = (100,100,200,150)
my_rect2 = ((100,100),(200,150))
my_rect3 = Rect(my_rect1)
my_rect4 = Rect(my_rect2)
```
pygame中有一个Rect类，用来存储和处理矩形对象（包含在pygame.locals中)
一旦有了Rect对象，我们就可以对其做很多操作，比如调整位置和大小，判断一个点是否在其中等等。

# 剪裁（clipping）
通常游戏的时候你只需要绘制屏幕的一部分，比如魔兽上面是菜单，下面是操作面板，中间的小兵和英雄大的不可开交
的时候，上下的部分也是保持相对不动的。为了实现这一点，surface就有了一种叫做裁剪区域的东西，也是一个矩
形，定义了哪部分会被绘制，也就是说一旦定义了这个区域，那么只有这个区域内的像素会被修改，其他的位置保持不
变。默认情况下，这个区域是所有地方。我们可以使用`set_clip`来设定，使用`get_clip`来获得这个区域
```python
screen.set_clip(0,400,200,600)
draw_map()
screen.set_clip(0,0,800,60)
draw_panel()
```

# 子表面（subsurfaces)
subsurfaces就是一个在surface中再提取一个Surface，记住当你往Subsurface上画东西的时候，同时也向
父表面上操作。这可以用来绘制图形文字，尽管pygame.font可以用来写很不错的字，但只是单色，游戏可能需要
更丰富的表现，这时候你可以吧每个字母（中文的话有些吃力了）各自做成一个图片，不过更好的方法是在一张图片上
画满所有的字母。把整张图读入，然后再用subsurface把字母一个一个“抠出来”
```python
my_font_image = pygame.load('font.png')
letters = []
letters['a'] = my_font_image.subsurface((0,0),(80,80))
letters['b'] = my_font_image.subsurface((80,0),(80,80))
```

# 填充surface
填充有时候可以作为一种**清屏**的操作，把整个surface填上一种颜色：
`screen.fill((0,0,0))`
同样可以提供一个矩形来制定填充哪个部分（这也可以作为一种画矩形的方法）。

# 设置surface的像素
能对surface坐的最基本的操作就是设置一个像素的色彩了，虽然我们基本不会这么做，但还是要了解。
`set_at`方法可以做到这一点，它的参数是坐标和颜色，见`random_draw_dot.py`随机在屏幕上画点

# 获得Surface上的像素
`set_at`的兄弟`get_at`可以帮我们做这件事，它接受一个坐标返回指定坐标点上的颜色，不过记住`get_at`   
在对hardware surface操作的时候很慢，而全屏的时候总是hardware的，所以**慎用**这个方法！

# 锁定surface 
当pygame往surface上画东西的时候，首先会把surface锁住，以保证不会有其他的进程来干扰，画完之后再解锁。
锁和解锁是自动发生的。所以有时候可能不那么有效率，比如在`random_draw_dot.py`中，每次画100个点，那
么就得解锁100次。复杂的情况下会影响效率的
党手动加锁的时候`screen.lock()`，一定不要忘记解锁`screen.unlock()`否则pygame有可能会失去响应，
虽然上面的例子可能没问题，但是隐含的bug是我们一定要避免的。

# blitting

blit n.位块传送
意思是将一个平面的一部分或全部图像整块从这个平面复制到另一个平面
blit是对表面做的最多的操作，我们在前面的程序中已经多次用到，不多说了；blit还有一种用法，
往往用在对动画的表现上，比如下例通过对frame_no的值的改变，**我们可以把不同的帧（同一幅画的不同位置）**
画到屏幕上：
`screen.blit(ogre,(300,200),(100*frame_no,0,100,100))`
`blit(source, dest, area=None, special_flags = 0) -> Rect`
