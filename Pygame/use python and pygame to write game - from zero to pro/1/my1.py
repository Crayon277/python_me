#!usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

pygame.display.set_caption('hello world')

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

background = pygame.image.load(background_image_filename).convert()
mouse = pygame.image.load(mouse_image_filename).convert_alpha()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background,(0,0))
    
    #显示鼠标，首先要获取光标的坐标
    x,y = pygame.mouse.get_pos()
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2

    screen.blit(mouse,(x,y))

    pygame.display.update()