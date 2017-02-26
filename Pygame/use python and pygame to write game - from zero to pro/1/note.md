# pygame 模块表

模块名 | 功能
----|---
pygame.cdrom | 访问光驱
pygame.cursors | 加载光标
pygame.display | 访问显示设备
pygame.draw | 绘制形状、线和点
pygame.event | 管理事件
pygame.font | 使用字体
pygame.image | 加载和存储图片
pygame.joystick | 使用游戏手柄或者 类似的东西
pygame.key | 读取键盘按键
pygame.mixer | 声音
pygame.mouse | 鼠标
pygame.movie | 播放视频
pygame.music | 播放音频
pygame.overlay | 访问高级视频叠加
pygame | 就是我们在学的这个东西了……
pygame.rect | 管理矩形区域
pygame.sndarray | 操作声音数据
pygame.sprite | 操作移动图像
pygame.surface | 管理图像和屏幕
pygame.surfarray | 管理点阵图像数据
pygame.time | 管理时间和帧信息
pygame.transform | 缩放和移动图像

-----
-----
# set_mode
`set_mode` 三个参数第一个为元祖，代表分 辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深。

标志位 | 功能
----|---
FULLSCREEN | 创建一个全屏窗口
DOUBLEBUF | 创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用
HWSURFACE | 创建一个硬件加速的窗口，必须和FULLSCREEN同时使用
OPENGL | 创建一个OPENGL渲染的窗口
RESIZABLE | 创建一个可以改变大小的窗口
NOFRAME | 创建一个没有边框的窗口

-----
-----
# 画背景代码放在主循环外面效果图
```python
screen.blit(background,(0,0))
#把画背景的这个代码放到外面，看看效果。
#因为虽然背景是不动的，我们还是需要每次都画它， 否则鼠标覆盖过的位置就不能恢复正常了。
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
```
![画背景代码放在主循环外面效果图](http://a1.qpic.cn/psb?/V10X9IqN05vrJi/24QBycwbpw4IaEg61U*WI*T.C.68hdhfs5rVnsIZbiY!/b/dCABAAAAAAAA&bo=MgOAAgAAAAADB5E!&rf=viewer_4)

---
---

设置标题的语句是`pygame.display.set_caption()` ，记住不是screen.set_caption
如果没有设置标题这个语句的话，就没有那个有带放大，关闭选项的那个。可以推测，set_caption就是要生成这个
所以不是在screen下也说的通的，screen只管窗口显示部分。

![无标题栏](http://a2.qpic.cn/psb?/V10X9IqN05vrJi/9y8C*NTR0njKotZSeWYsvB4qg8e.6sTqic1W3ejSac4!/b/dB4BAAAAAAAA&bo=SwOAAgAAAAADB.g!&rf=viewer_4)

犯了一个错误，❌ ！！！ 上面的原因是我创建了一个无边框的窗口！！！
我在set_mode中的第二个参数设置的是NOFRAME，所以才会出现这样的情况！！！
还有如果在第二个参数是0，没有设置标题的话，默认的标题是pygame window

