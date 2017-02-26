#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test_position.py
# Created Time: Thu Feb 23 22:08:45 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pygame
from pygame.locals import *
from sys import exit
from math import sqrt

class Vector(object):
    def __init__(self,x=0.,y=0.):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)
    __repr = __str__
    def get_magnitude(self):
        return sqrt(self.x**2+self.y**2)
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
    def __add__(self,other):
        return self.__class__(self.x + other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(other.x-self.x,other.y-self.y)
    @classmethod
    def from_points(cls,v1,v2):
        return cls(v2.x-v1.x,v2.y-v1.y)
    
    # def __getitem__(self,index):
        # try:
            # return self.


pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load("../1/sushiplate.jpg").convert()
sprite = pygame.image.load("../1/fugu.png").convert_alpha()

clock = pygame.time.Clock()

position = Vector(100.0,100.0)
heading = Vector()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))
    screen.blit(sprite,position) # test if position work
    """
    这里不行。
    那到底是哪个起作用？？？
    """
    pygame.display.update()

