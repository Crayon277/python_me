#!/usr/bin/env python
# coding=utf-8


import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('test fullscreen')

background = pygame.image.load('../1/sushiplate.jpg').convert()

FullScreen = False

while 1:
    for event in pygame.event.get(): #1
        if event.type == QUIT:#2
            exit()
        if event.type == KEYDOWN:#3
            """
            这个放在for循环外面有差吗？
            """
            if event.key == K_f:#4
                FullScreen = not FullScreen
        if FullScreen:
            screen = pygame.display.set_mode((640,480),FULLSCREEN,32)
        else:
            screen = pygame.display.set_mode((640,480),0,32)
        """ if FullScreen
        这个为什么要放在if#4里面，不能放在for循环外面，因为如果放在外面，就会闪屏，是因为，如果全屏模式的话
        他会一直pygame.display.set_mode，也就是每个循环都会执行一次，窗口模式也是，只是看不出来而已
        可以测试一下，放在与 K_f对比的这个语句平行位置都不行。这是为什么？？？第二次循环进来
        if event.type==KEYDOWN 这里就不会放进来了啊？？？？

        放在#4里面的话，意思是一单进入到了这个判断语句里面，那么就是按下了f键，这个时候FullScreen反置
        马上重置screen 

        最新测试结果：
        没问题，放在哪都没问题！！！那之前可能是因为其他的因素。反正这次测试是没问题。
        """
    
    screen.blit(background,(0,0))
    pygame.display.update()
            