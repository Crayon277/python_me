#!/usr/bin/env python
# coding=utf-8

"""
这个程序其实最后的功能就是演示三原色怎么合成其他颜色
红绿蓝各占一行，从暗到明，然后通过点击不同的明暗度，在另一半窗口显示出组合出的颜色。

这里比较难理解的就是数值的计算。
"""

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

def create_scales(height):
    red_scales_surface = pygame.surface.Surface((640,height))
    green_scales_surface = pygame.surface.Surface((640,height))
    blue_scales_surface = pygame.surface.Surface((640,height))
    """
    上面的就是生成三个surface对象用来放颜色的。
    """
    for x in range(640):
        c = int((x/640.)*255.)
        """
        我现在不明白这个计算什么意思，其他大概都明白了。
        懂了！！！ 不是从暗到明吗，按照从左到右，位置占比例255，决定这个地方的颜色深浅
        red(c,0,0)
        """
        red = (c,0,0)
        green = (0,c,0)
        blue = (0,0,c)
        line_rect = Rect(x,0,1,height)
        #Rect(left, top, width, height) -> Rect
        #可以理解为以(left,top)为左上角的宽为width，高为height的矩形
        pygame.draw.rect(red_scales_surface,red,line_rect)
        pygame.draw.rect(green_scales_surface,green,line_rect)
        pygame.draw.rect(blue_scales_surface,blue,line_rect)
        """
        微积分似的，宽度为1的画
        pygame.draw.rect参数的意义应该是
        在哪画，画什么，画多少
        """
    return red_scales_surface,green_scales_surface,blue_scales_surface
"""
这个函数的功能应该是创建三个条，上面是红绿蓝，然后从暗到明
"""
red_scale,green_scale,blue_scale = create_scales(80)

color = [127,127,127]
"""
默认中间的
"""
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0,0,0))

    screen.blit(red_scale,(0,00))
    screen.blit(green_scale,(0,80))
    screen.blit(blue_scale,(0,160))
    """
    上三层
    """
    x,y = pygame.mouse.get_pos()
    """
    模拟点击不同的颜色产生不同混合色
    """
    if pygame.mouse.get_pressed()[0]:
        #被按下后
        for component in range(3):
            if y > component*80 and y < (component+1)*80:
                #在自己的框中
                color[component] = int((x/639.)*255.)
                """
                不明白的是这里为什么639，而不是640啊？？？？关键是会是问题吗？？？
                """
        pygame.display.set_caption('pygame color test - '+str(tuple(color)))
    
    for component in range(3):
        pos = (int((color[component]/255.)*639),component*80+40)
        """
        之前是知道位置计算该位置的颜色比例，那现在是换过来了么。已知x求y，现在已知y求x
        后一个参数，高度的中间
        """
        pygame.draw.circle(screen,(255,255,255),pos,20)
        """
        我觉得pos是圆心，20是半径
        在screen上画
        """
    pygame.draw.rect(screen,tuple(color),(0,240,640,240))
    """
    画出下半部分用来显示效果
    """
    pygame.display.update()