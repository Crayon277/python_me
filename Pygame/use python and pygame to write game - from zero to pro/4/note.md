# 显示文字
我们想着显示文字，就写上去就好了么，但是没那么简单。你看，如果在其他地方，可以用一个label，来显示，那这个label是怎么显示的
远远没有这么简单，

pygame可以直接调用系统字体，或者也可以使用TTF字体
这里说到了字体，那么就意味着，先要有一个字体？然后知道这个字是什么形状的，然后在渲染出来？点阵
为了使用字体，**你得先创建一个Font对象**,对于系统自带的字体：
`my_font = pygame.font.SysFont('arial',16)`
第一个参数是字体名，第二个自然是大小，因为一半arial字体在很多系统都是存在的，如果找不到的话，就会使用一个默认的字体，
这个默认的字体和每个操作系统相关，你也可以使用pygame.font.get_fonts()来获得当前系统所有可用字体

或者使用TTF的字体：
`my_font = pygame.font.Font("my_font.ttf",16)`

这个语句使用了一个叫做`my_font.ttf`,这个方法之所以好是因为你可以吧字体文件随游戏一起分发，避免用户机器上没有需要的字体。
**一旦创建了一个font对象，你就可以用render方法来写字了，然后就能blit到屏幕上**

`text_surface = my_font.render('pygame is cool',True,(0,0,0),(255,255,255))`
第一个参数是写的文字；
第二个参数是不二之，以为这是否开启抗锯齿，就是说True的话字体会比较平滑，不过相应的速度有一点点影响
第三个参数是字体的颜色
第四个参数是背景色，如果想没有背景色，也就是透明，那么可以不加这第四个参数


# pygame的错误处理
程序总会出错的，比如当内存用尽的时候pygame就无法再加载图片，或者文件根本就不存在，比如下下例
```python
>>> import pygame
>>> screen = pygame.display.set_mode((640, -1))
---------------------------------
Traceback (most recent call last):
  File "<interactive input>", line 1, in ?
pygame.error: Cannot set 0 sized display mode
----------------------------------
```
对付这种错误其实也就是标准的python捕捉方法
```python
try:
    screen = pygame.display.set_mode(SCREEN_SIZE)
except pygame.error,e:
    print "can't create the display :-("
    print e
    exit()
```
错误捕捉实在太重要了。