#!/usr/bin/env python
# coding=utf-8

"""
在1的程序里，是在控制台里打印出event，现在尝试着在窗口中显示
有种黑客帝国的感觉
"""


import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)


font = pygame.font.SysFont('arial',16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    #获得事件的名称
    event_text = event_text[-SCREEN_SIZE[1]/font_height:]
    #这个切片操作保证了event_text里面只保留一个屏幕的文字
    """
    SCREEN_SIZE[1] 是 480，相当于窗口的高度，font_height是字体的高度，除一下相当于一个窗口能放多少行。
    如果自己写的话能想到么？ 关键是这个语句没有的话是什么效果？
    """
    if event.type == QUIT:
        exit()
    
    screen.fill((255,255,255))
    #255，255，255是白色，0，0，0是黑色
    y =SCREEN_SIZE[1] - font_height
    #找一个合适的起笔位置，最下面开始但是要留一行的空
    """
    可以算一下的。问题是这个字体是在，比如y是450，字体也是有高度的，是中间部位开始在450，还是下边贴着450或者上面
    """
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        """
        看来这里是比较关键的一点
        """
        y-=font_height
        #把笔提一行
        """
        我还奇怪为什么reversed(event_text)，因为倒着写，在收到的事件列表中，从最后一行开始。
        """
    pygame.display.update()


