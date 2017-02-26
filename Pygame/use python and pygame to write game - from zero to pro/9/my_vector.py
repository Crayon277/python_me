#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: my_vector.py
# Created Time: Thu Feb 23 21:42:42 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

"""
什么时候能从问题出发，想到解决方案
"""

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load('../1/sushiplate.jpg').convert()
mouse = pygame.image.load('../1/fugu.png').convert_alpha()
clock = pygame.time.Clock()
position = Vector2(100.0,100.0)
heading = Vector2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))
    screen.blit(mouse,position)
    
    time_passed_seconds = clock.tick()/1000.0

    x,y = pygame.mouse.get_pos()
    destination = Vector2(x,y) - Vector2(mouse.get_size())/2
    """
    这里说一下这个Vector2的参数，本来是要接受两个参数的，应该写成(*mouse.get_size())，但是看了一下代码
    if hasattr(x,"__getitem__"):
        x,y = x
    也就是接受了一个元组，自己会处理
    """
    vector_to_mouse = Vector2.from_points(position,destination)
    vector_to_mouse.normalize()
    heading += vector_to_mouse*0.7

    position += heading*time_passed_seconds

    pygame.display.update()

