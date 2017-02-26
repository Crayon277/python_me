#!/usr/bin/env python
# coding=utf-8

#实现讲一个画面的不同部分画到屏幕上

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

pygame.display.set_caption('test blit')

background = pygame.image.load('../1/sushiplate.jpg').convert()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    for frame_x in xrange(0,321):
        screen.blit(background,(160,120),(frame_x,0,320,240))
        pygame.display.update()
    for frame_y in xrange(1,241):
        screen.blit(background,(160,120),(frame_x,frame_y,320,240))
        pygame.display.update()
    for frame_x in xrange(319,0,-1):
        screen.blit(background,(160,120),(frame_x,frame_y,320,240))
        pygame.display.update()
    for frame_y in xrange(239,0,-1):
        screen.blit(background,(160,120),(frame_x,frame_y,320,240))
        pygame.display.update()

    #pygame.display.update()
"""
不管什么blit，blit之后要马上update，不然没有画面反应出来的

还有一个问题就是，我这四个for循环在event.get()后面，相当于要等四个for循环全部结束之后才能获取事件
这个怎么解决
可以每次都检查一下。最low的办法了
""" 