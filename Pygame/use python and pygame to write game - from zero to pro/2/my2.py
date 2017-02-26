#!/usr/bin/env python
# coding=utf-8

#在窗口显示event信息
import pygame
from pygame.locals import *
from sys import exit


pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('event')

font = pygame.font.SysFont('arial',16)
font_height = font.get_linesize()
print font_height


event_list = []
while 1:
    for event in pygame.event.get():
        event_list.append(str(event))
        if event.type == QUIT:
            exit()
    screen.fill((0,0,0))
    event_list = event_list[-480/font_height:]
    
    y = 480-font_height    
    """
    为什么要-font_height，因为如果是480，那就相当于在窗口地下开始第一行。
    """

    for text in reversed(event_list):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y-=font_height
    
    pygame.display.update()
    