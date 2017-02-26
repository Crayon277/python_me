#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: draw_demo.py
# Created Time: Tue Feb 21 19:51:46 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit

from random import *
from math import pi

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            #按任意键清屏，并把点恢复到原始状态
            points = []
            screen.fill((255,255,255))
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255,255,255))



            #画随机矩形
            rc = (randint(0,255),randint(0,255),randint(0,255))
            rp = (randint(0,639),randint(0,479))
            rs = (639-randint(rp[0],639),479-randint(rp[1],479))
            """
            randint(rp[0],639)保证选择的矩形宽的最右边的坐标是在屏幕
            里面。但是这个数值是坐标！！数值很大。然而我们参数是要的
            宽和高，639再减去这个值，相当于宽取得是那个数值到屏幕最
            右侧的距离。画个图就知道了。
            """
            pygame.draw.rect(screen,rc,Rect(rp,rs))


            #画随机圆形
            rc = (randint(0,255),randint(0,255),randint(0,255))
            rp = (randint(0,639),randint(0,479))
            # rr = randint(1,200)
            # min_arg = min(rp[0],rp[1])
            # rr = randint(1,min_arg)
            #上面这个感觉还不行，因为没有比较到右边的距离

            if rp[0]>320:
                if rp[1]>240:
                    min_arg = min(640-rp[0],480-rp[1])
                else:
                    min_arg = min(640-rp[0],rp[1])
            else:
                if rp[1]>240:
                    min_arg = min(rp[0],480-rp[1])
                else:
                    min_arg = min(rp[0],rp[1])
            """
            上面的出现了bug了，
            因为min_arg是根据随机生成的rp计算的，不可控，万一min_arg
            最后为0,比1小，这样就会报错ValueError, empty range....
            """
            min_arg = min_arg or 7
            #当min_arg不为0的时候，返回自己，当min_arg为0的时候返回7
            rr = randint(0,min_arg)
            """ 
            还有一个问题，就是为什么出现比预期以rr为半径更大的圆，也
            就是这个实际rr更大？？？

            等等。我弄错了，我一直把鼠标点的那个坐标当作了rp的坐标了
            圆心是随机的。没错没错。
            """
            #保证在屏幕内
            pygame.draw.circle(screen,rc,rp,rr)




            #获得当前鼠标的位置
            x,y = pygame.mouse.get_pos()
            points.append((x,y))
            #根据点击画弧线
            angle = (x/639.0)*2*pi
            #其实越往左弧线越短，越往右弧线越长
            pygame.draw.arc(screen,(0,0,0),(0,0,639,479),0,angle,3)
            pygame.draw.ellipse(screen,(0,255,0),(0,0,x,y))
            pygame.draw.line(screen,(0,0,255),(0,0),(x,y))
            pygame.draw.line(screen,(255,0,0),(x,y),(640,480))
            #画点击轨迹图
            if len(points)>1:
                pygame.draw.lines(screen,(155,155,0),False,points,2)
            #把每个点画的明显一点
            for p in points:
                pygame.draw.circle(screen,(155,155,155),p,3)
    pygame.display.update()
            

