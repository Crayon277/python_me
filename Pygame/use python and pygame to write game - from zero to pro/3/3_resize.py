#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((640,480),RESIZABLE,32)
pygame.display.set_caption('640,480')

background = pygame.image.load('../1/sushiplate.jpg').convert()
newsize = (640,480)
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == VIDEORESIZE:
            newsize = event.size
            screen = pygame.display.set_mode(newsize,RESIZABLE,32)
            pygame.display.set_caption(str(newsize))
    new_width ,new_height = newsize
    for y in range(0,new_height,480):
        for x in range(0,new_width,640):
            screen.blit(background,(x,y))
    """
    出现一个问题，窗口拉大后，理应效果是平铺，但是拉大的空间被黑色填充。
    bug：
        for y in range(0,480,new_height):
            for x in range(0,640,new_width):
    range()后面两个参数位置写反了，应该是(0,new_height,480)
    还有，应该避免使用硬编码480
    """
        
    pygame.display.update()
    """
    还有一个问题，就是拉大的时候，没有放开鼠标的时候背景是白色的。
    自己用那些应用，肯定是一遍拉大，然后里面跟着一起变，不会说是，我拉大到哪里，然后再给我显示出来
    这里怎么弄？？？？？？？？？
    """



