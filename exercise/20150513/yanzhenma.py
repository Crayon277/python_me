#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: yanzhenma.py
# Created Time: Wed May 13 15:55:00 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import Image,ImageDraw,ImageFont,ImageFilter

import random

def rndchr():
    return chr(random.randint(65,90))

def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndcolor2():
    return (random.randint(32,125),random.randint(32,127),random.randint(32,127))


width = 240
height = 60

image = Image.new('RGB',(width,height),(255,255,255))

font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndcolor())

for t in range(4):
    draw.text((60*t + 10,10),rndchr(),font = font,fill = rndcolor2())

image = image.filter(ImageFilter.BLUR)

image.save('/Users/Crayon_277/Pictures/code.jpg','jpeg')
