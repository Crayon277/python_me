#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

"""
class defination
"""

class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        pygame.sprite.Sprite.__init__(self) #调用非绑定的方法，要传入self参数
        self.image = bullet_img
        self.rect = self.image.get_rect() 
        self.rect.midbottom = init_pos
        self.speed = 10
    
    def move(self):
        self.rect.top -= self.speed

class Player(pygame.sprite.Sprite):
    def __init__(self,plane_img,player_rect,init_pos):
       pygame.sprite.Sprite.__init__(self)
       self.image = []
       for i in range(len(player_rect)):
           self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
       self.rect = player_rect[0] #rect到底是什么？？？
       self.rect.topleft = init_pos
       self.speed = 8
       self.bullets = pygame.sprite.Group()
       self.img_index= 0
       self.is_hit = False

    def shoot(self,bullet_img):
        bullet =Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)
    
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
    def moveDown(self): #这里主要就是不让飞机出边框
        """
        有一个问题，就是self.rect.top没有超出边框减去自身的长度，以保证全部身子在游戏边框内，
        但是加上speed超出了呢？
        向上等其他动作也一样，这样会不会出现跳帧的情况，也就是超出了一点点，然后因为代码中是归位0
        （例如self.rect.top=0）,这样在循环updata display的时候，就会跳帧。 预测。
        """
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    
    def moveRight(self):
        """
        我还在想为什么一直只有top,和left,不能用right等其他属性，其实就是因为self.rect的四个参数是
        left, top , width, height，
        """
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH-self.rect.width
        else:
            self.rect.leftt += self.speed
 

class Enemy(pygame.sprite.Sprite):
     def __init__(self,enemy_img,enemy_down_imgs,init_pos):
         pygame.sprite.Sprite.__init__(self)
         self.image = enemy_img
         self.rect = self.image.get_rect()
         self.rect.topleft = init_pos
         self.down_imgs = enemy_down_imgs
         self.speed = 2
         self.down_index = 0
        
     def move(self):
         self.rect.top += self.speed 

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('飞机大战')

background = pygame.image.load('./resources/image/background.png')
plane_img = pygame.image.load('./resources/image/shoot.png') #2

#选择飞机在图片中的位置（因为图是所有的飞机的），然后生成subsurface， 然后初始化飞机开始的位置
player_rect = pygame.Rect(0,99,102,126) #2
player = plane_img.subsurface(player_rect) #2
player_pos = [200,600] #2


while 1:
    screen.fill(0)
    screen.blit(background,(0,0))

    screen.blit(player,player_pos) #2
    pygame.display.update()

    key_pressed = pygame.key.get_pressed() #3
    if key_pressed[K_UP]: #3
        player_pos[1] -= 3  #3
    if key_pressed[K_DOWN]:  #3
        player_pos[1] += 3   #3
    if key_pressed[K_LEFT]:  #3
        player_pos[0] -= 3   #3
    if key_pressed[K_RIGHT]: #3
        player_pos[0] += 3   #3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



