#!/usr/bin/env python
# coding=utf-8

background_image_filename = '../1/sushiplate.jpg'
sprite_image_filename = '../1/fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加*意味着把列表或元组展开
    destination = Vector2( *pygame.mouse.get_pos() ) - Vector2( *sprite.get_size() )/2
    #sprite中心位置为准
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, destination)
    # 向量规格化
    vector_to_mouse.normalize()

    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
    heading = heading + (vector_to_mouse * .6)    
    """
    最主要的是这句代码，vector_to_mouse已经是步进向量了，0.6估计是要再缩放一下
    因为实现运动就是不断的计算位置，变更位置，重新在新位置上画图
    如果要实现变速，那么速度要变，heading一直加上那个向量，因为向量是有方向的，也就是由(*,*)决定了
    这样超过了，那时的position一开始与鼠标位置（假如没动），是由近到远，随着vector_to_mouse的值增加，但因为
    是负的，方向变了，所以减去的会越来越大，这样就实现了超过鼠标后越来越慢
    """
    position += heading * time_passed_seconds
    pygame.display.update()
