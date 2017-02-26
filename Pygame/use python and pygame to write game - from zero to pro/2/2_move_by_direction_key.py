#!/usr/bin/env python
# coding=utf-8


import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('move by direction key')

background_image = '../1/sushiplate.jpg'

background = pygame.image.load(background_image).convert()

x,y=0,0
move_x,move_y=0,0
while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        # print event
        # if event.type == KEYDOWN:
        #     print '-'*10
        #     print event.dict
        #     print event.key
        #     print event.mod
        #     print event.type
        #     print event.scancode
        #     print '-'*10
        
               
        if event.type == KEYDOWN:
            if 273 == event.key:
                y-=3
                # move_y = -1
            if 274 == event.key:
                y+=3
                # move_y = 1
            if 275 == event.key:
                x+=3
                # move_x = 1
            if 276 == event.key:
                x-=3
                # move_x = -1
        

        # if event.type == KEYDOWN:
        #     if event.key == K_LEFT:
        #         move_x = -1
        #     elif event.key == K_RIGHT:
        #         move_x = 1
        #     elif event.key == K_UP:
        #         move_y = -1        
        #     elif event.key == K_DOWN:
        #         move_y = 1
        # elif event.type == KEYUP:
        #     move_x = 0
        #     move_y = 0
        """
        这个逻辑相比上面那个，不同在于，如果一直按着上键，图片也就一直向上。上面那个不行。
        猜想：
        不是因为多了一个KEYUP的比较，而是因为move_x,move_y
        当一直按着键的时候，这个循环过去了，但是没有新的事件，因为move_x，y在上一次按下的时候设置了
        在下面代码中继续+=move_x，是这里起到了一直按着可以一直动的效果。
        测试：
        测试了一下，确实是达到了上面的效果，但是不确定是否是move_x的原因，因为没有KEYUP的这个因素，
        不过这样起到了另外一种效果，因为第一个逻辑里面没有比较KEYUP，所以当按下了一个键，就会一直往这个方向动，
        即使放开键。这是因为move_x,move_y没有被设置回0，所以x+=move_x中的move_x一直会使x减少或增加
        可以测试一下，
        主要是出现了这个情况的话，能看出，或者能解决这个问题，通过写KEYUP对比吗？
        """
        
        
    x+=move_x
    y+=move_y
    screen.fill((255,255,255))
    screen.blit(background,(x,y))
    pygame.display.update()
    """
    发现了一个问题，在移动图片的时候，移动过去的地方还是原来的背景，这样图片如果有明暗的话，移动的时候就有分界线
    背景填充的问题可能，增加了screen.fill就可以了，可以注释掉这条语句看看什么效果。对比一下
    """

