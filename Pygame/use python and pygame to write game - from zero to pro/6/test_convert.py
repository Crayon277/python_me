#!/usr/bin/env python
# coding=utf-8

import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('test convert')

test_surface = pygame.Surface((256,256))
pygame.image.load('../1/sushiplate.jpg').convert(test_surface)

while 1 :
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(test_surface,(0,0))

    pygame.display.update()