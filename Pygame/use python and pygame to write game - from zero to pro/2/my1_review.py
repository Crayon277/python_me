#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('mouse move review')


background_image = '../1/sushiplate.jpg'
mouse_image = '../1/fugu.png'

background = pygame.image.load(background_image).convert()
mouse = pygame.image.load(mouse_image).convert_alpha()

pygame.mouse.set_pos(320,240)
#自己加上去的，设置鼠标初始位置，下面get_pos就是接受的这个坐标。

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2

    screen.blit(mouse,(x,y))

    pygame.display.update()
