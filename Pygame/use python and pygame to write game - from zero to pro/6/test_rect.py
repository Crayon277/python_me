#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen =pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("rect")

rect1 = Rect(0,0,200,150)
rect2 = Rect((0,150),(200,150))

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    """
    screen.blit(rect1)
    screen.blit(rect2)
    TypeError: argument 1 must be pygame.Surface, not pygame.Rect
    """
    pygame.display.update()