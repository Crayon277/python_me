#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # screen.fill((0,0,0))
    # x,y=randint(0,640),randint(0,480)
    # screen.set_at((x,y),(255,255,255))
    # pygame.display.update()

    rand_col = (randint(0,255),randint(0,255),randint(0,255))
    # start = time.clock()
    # screen.lock()
    for _ in xrange(100):
        rand_pos = (randint(0,639),randint(0,479))
        screen.set_at(rand_pos,rand_col)
    """
    这个相比自己写的那段，就是一下子形成好几个点。
    """
    # screen.unlock()
    pygame.display.set_caption('%.f'%(time.clock()-start))
    # print time.clock()-start
    pygame.display.update()