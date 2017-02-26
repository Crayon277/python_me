#!/usr/bin/env python
# coding=utf-8

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
#指定图像文件名称

import pygame
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块接一个exit函数来推出程序

pygame.init()
#初始化pygame。 为使用硬件做准备

# screen = pygame.display.set_mode((640,480),0,32)
screen = pygame.display.set_mode((640,480),HWSURFACE | FULLSCREEN,32)
"""
太可怕了，全屏的时候不知道怎么退出，只能重启，
吓得老子赶紧加上退出的另一种方式
"""
#创建一个窗口
"""
set_mode会返回一个surface的对象，代表了在桌面上出现的那个窗口。参数意义见note.md
"""
pygame.display.set_caption("hello , world")
#设置窗口标题

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#因为鼠标的标记是有一部分是透明的，所以我们需要用alpha通道来显示我们只需要那一部分
"""
convert函数是将图像数据都转化成surface对象，每次加载完图像以后就应该做这件事件（事实上因为
太常用了，如果你不写pygame也会帮你做）；convert_alpha相比convert,保留了alpha通道信息，这样
我们的光标才可以是不规则的形状。
"""

while True:
    # event = pygame.event.wait()
    # """
    # 如果我们使用pygame.event.wait()，Pygame就会等到发生一个事件才继续下去，就好像你在门的猫眼上盯着外面一样，来一个放一个……一般游戏中不太实用，因为游戏往往是需要动态运作的
    # 但打印出event还是挺管用的
    # """
    # print event
    # if event.type == QUIT:
    #     exit()
    # print type(event)
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    """
    游戏的主循环是一个无限循环，直到用户跳出。在这个主循环里做的事情就是不停的画背景和更新光标位置。
    虽然背景是不动的，我们还是需要每次都画它！！！否则鼠标覆盖过的位置就不能恢复正常了。
    """
    #将背景图画上去，background_image_filename只是存储了图像文件的物理位置
    #background是我们用pygame的组件读取出来这个图片文件
    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()
    #获取鼠标位置
    """
    这里发现一个有趣的现象，就是鼠标如果不在整个窗口里面的话，鼠标的图片还是会显示，显示一半，根据下面的以
    鼠标为中心显示的鼠标图片，那样这个get_pos()的函数内部应该是将超出窗口的鼠标坐标设立边界，归零或归最大。
    """
    x-=mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    #计算光标的左上角位置. 原来的x,y当成鼠标图像的中心，

    screen.blit(mouse_cursor,(x,y))
    # 那这样就知道的后面参数的坐标是什么意思了，就是以这个坐标为左上角开始铺图片。整个边框左上角是（0，0）
    """
    blit是一个重要函数，第一个参数为一个surface对象，第二个为左上角位置，
    画完以后一定记得要用update更新一下，否则画面一片漆黑
    经过我的实验，将下面这一个语句注释掉的话，没有任何显示，白色的。标题正常显示。
    """
    pygame.display.update()
    #刷新画面 
    
    