#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: draw.py
# Created Time: Tue Feb 21 10:51:56 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit
from random import *
from math import pi
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('mix draw demo')

pointlist = []
def random_color():
    return randint(0,255),randint(0,255),randint(0,255)
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == ACTIVEEVENT:
            if event.gain == 0:
                screen.fill((255,255,255))
                pointlist=[]
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            x,y = event.pos
            pointlist.extend(((x,y),(x,y)))
            rect_x,rect_y = randint(0,640),randint(0,480)
            rect_width = randint(0,640)
            rect_height = randint(0,480)
            pygame.draw.rect(screen,random_color(),(rect_x,rect_y,rect_width,rect_height))
            circle_x,circle_y = randint(0,640),randint(0,480)
            circle_radius = randint(0,240)
            pygame.draw.circle(screen,random_color(),(circle_x,circle_y),circle_radius)
            pygame.draw.ellipse(screen,random_color(),((0,0),(x,y)))
            pygame.draw.arc(screen,random_color(),((-1,0),(640,480)),uniform(0,2*pi),uniform(0,2*pi))
            pygame.draw.line(screen,random_color(),(0,0),(x,y))
            pygame.draw.line(screen,random_color(),(x,y),(640,480))
            pygame.draw.lines(screen,random_color(),0,pointlist)
        
    pygame.display.update() 
    # screen.fill((0,0,0))
    # x,y,width,height = randint(0,640),randint(0,480),
    # pygame.draw.rect(screen,(255,255,255),)

