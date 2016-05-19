#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 21_money_eat_peach.py
# Created Time: Wed May 18 10:00:31 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


left = 1
for i in range(9):
    left = (left+1)*2

print left

