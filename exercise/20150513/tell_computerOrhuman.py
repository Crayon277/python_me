#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: tell_computerOrhuman.py
# Created Time: Wed May 13 16:09:04 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import Image,ImageFont,ImageDraw,ImageFilter
import random


def rndchr():
    return chr(random.randint(64,95))

def rndcolor1():
    return (random.randint(60,255),random.randint(60,255),random.randint(60,255))

def rndcolor2():
    return (random.randint(12,50),random.randint(12,50),random.randint(12,50))


width = 240
heigh = 60

image = Image.new("RGB",(width,heigh),(255,255,255))

font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(heigh):
        draw.point((x,y),fill = rndcolor1())


for x in range(4):
    draw.text((60*x + 10,10),rndchr(),font = font,fill = rndcolor2())

image = image.filter(ImageFilter.BLUR)
image.save('/Users/Crayon_277/Pictures/code_damn.jpg','jpeg')

