#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: move_by_time.py
# Created Time: Wed Feb 22 08:56:43 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load('../1/sushiplate.jpg').convert()
sprite = pygame.image.load('../1/fugu.png')

clock = pygame.time.Clock()

x=0.
speed = 250. # 像素／秒

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))
    screen.blit(sprite,(x,240-sprite.get_height()/2))
    time_passed = clock.tick()
    x += time_passed*speed/1000.0
    """
    一开始没有除以1000，单位没有换过来，出现了屏幕上偶尔闪现的鱼，原以为是速度太快额
    """

    if x > 640:
        x -= 640
    pygame.display.update()
