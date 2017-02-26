#!/usr/bin/env python
# coding=utf-8

my_name = 'Crayon Chaney'
import pygame
pygame.init()
# my_font = pygame.font.SysFont('arial',64) # 返回一个font对象
# name_surface = my_font.render(my_name,True,(0,0,0),(255,255,255))
# """
# font对象中的render方法，返回一个surface对象吧，应该。面向对象的思维！！！
# """
# pygame.image.save(name_surface,'name.png')


"""
如何显示中文。
简单的来说，首先你得有一个可以使用中温的字体，宋体，黑体什么的，或者直接使用中文ttf文件，然后文字使用
unicode，即u'中文'这种，最后不要忘了源文件里加上一句文件编码的魔法注释，也就是第2行代码。
"""

from pygame.locals import *
from sys import exit

screen = pygame.display.set_mode((640,480),0,32)

font = pygame.font.Font('haipai.ttf',40)
text_surface = font.render(u'你好',True,(0,0,255))

x=0
y=(480-text_surface.get_height())/2
# print y #218
# print text_surface.get_width() #80
# print text_surface.get_height() #44
"""
y的设置是让字体在中间显示，这个中间，是字体的中间在窗口中间线上，那也就是字体最上面的是在窗口中线240
再减去字体高度的一半，22，（因为从上到下是递增的，坐标），218，这和上面y的算出来的一样。
"""

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0,0,0))
    x-=2
    if x<-text_surface.get_width():
        # x=640-text_surface.get_width()
        # x+=640 #这两个效果一样的。为什么最终效果会跳一下，因为其实当x<-宽度的时候再加上640，
                 #其实也就是移到右边的离边框一个宽度的距离，跟上面的效果一样。
        x = 640 #这个跟上面不一样的地方就是从右边出来的时候不会那么突兀
    """
    实现横向滚动的效果
    实验：
    加上功能，用方向键改变滚动方向。
    """

    screen.blit(text_surface,(x,y))
    pygame.display.update()