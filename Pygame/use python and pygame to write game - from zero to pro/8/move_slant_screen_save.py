#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: move_slant_screen_save.py
# Created Time: Wed Feb 22 10:28:56 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit
import random
from math import pi
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load('../1/sushiplate.jpg').convert()
sprite = pygame.image.load("../1/fugu.png") #不用convert_alpha()不用不规则的

clock = pygame.time.Clock()
x = 320.0
y = 240.0
speed = 250
sign_x = 1
sign_y = 1
k = 2
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background,(0,0))
    screen.blit(sprite,(x,y))
    
    time_passed = clock.tick()
    
    x += sign_x * time_passed * speed / 1000.0
    y += sign_y * k * time_passed*speed/1000.0
    if x > 640-sprite.get_width():
       sign_x = -1
    if x < 0:
        sign_x = 1
    if y > 480 - sprite.get_height():
        sign_y = -1
    if y < 0:
        sign_y = 1
    """
    为什么这样就行了？成功了，看我原来想的那么复杂，其实主要就是上面四个比较，但是我之前想复杂了，为什么呢
    我之前想复杂了是因为想到斜率，然后触壁之后，斜率要对称了，速度不变就是触壁之后方向要变，我原本是想根据斜率来
    计算出下一步的x,y，但是首先这里坐标系是倒过来，还不怎么好看，

    然后还有一个问题，是先触到哪个壁，其实这个也没有那么复杂，上面四个if都是独立的，假如碰到棱角，但是两个if可以进
    去，这样两个方向都改了。

    为什么符号反过来就行了，因为，触壁反弹，比如触到下面的边，那就是y最大了，反弹之后只能变小了，我不管你x怎么变
    因为x保持原样就行了，这和考虑很复杂的，从左边过来，从右边过来，斜率方向还不一定的好多了。
    往左上方运动，触到上边，因为，往左么，触壁之后y增大，x还是往左减少。往右下方运动的话，触到右边，因为还没有
    触到下边，所以y再继续增加，x触壁反弹减少。这样就行了。
    """
    pygame.display.update()

"""
x,y = 320.0,240.0
speed = 250.
sign_x = 1
sign_y = 1
flag = 1
k = random.randint(0,100) #斜率，暂定往右下方走，因为左上角是(0,0)
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            flag = 1
    screen.blit(background,(0,0))
    screen.blit(sprite,(x,y))
    
    clock = pygame.time.Clock()
    time_passed = clock.tick()
    
    
"""
    #先判断先碰到宽边，还是高边
"""
    if flag:
        if k > (480 - y ) / (640 - x):
            end_y = 1
        else:
            end_y = 0
        flag = 0
    x += sign_x * time_passed * speed / 1000.0
    y += k*x*sign_y
    
"""
    #有一个问题，很有可能物体的某一部分超出了边界，我们是需要触壁就反弹，但是毕竟不是连续的，这里更像是离散的，这就不一定刚好触壁
"""
    # if end_y:
        # if 
    if y >= 480 and x < 640:
        sign_y = -1
    elif y < 480 and x >= 640:
        sign_x = -1

    if y <= 0 and x > 0:
        sign_y = 1
    elif y >
"""


