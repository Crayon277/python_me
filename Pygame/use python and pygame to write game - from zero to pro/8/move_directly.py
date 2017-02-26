#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: move_directly.py
# Created Time: Tue Feb 21 21:57:39 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

background_filename = '../1/sushiplate.jpg'
sprite_image_filename = '../1/fugu.png'

background = pygame.image.load(background_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

x = 0.

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))
    screen.blit(sprite,(x,100))
    """
    有一个问题就是为什么之前会消失？？？

    其实之前的画没有消失，只是又有新的覆盖上去了
    可以互换上面两行试试看，那就只显示一个背景了。互换两行ddp
    """

    x+=10

    if x > 640:
        x = 0.

    pygame.display.update()
