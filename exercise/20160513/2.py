#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 2.py
# Created Time: Fri May 13 13:40:19 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖
#金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提
#成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元
#的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60
#万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超
#过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


def level_0_10(benefit):
    print 'level 0 - 10'
    return benefit*0.1

def level_10_20(benefit):
    print 'level 10 -20'
    return level_0_10(100000) + (benefit-100000)*0.075

def level_20_40(benefit):
    print "level 20 - 40"
    return level_10_20(200000) + (benefit-200000)*0.05

def level_40_60(benefit):
    print "level 40 - 60"
    return level_20_40(400000) + (benefit-400000)*0.03

def level_60_100(benefit):
    print "level 60 - 100"
    return level_40_60(600000) + (benefit-600000)*0.015

def level_100_infinite(benefit):
    print "level 100 - infinite"
    return level_60_100(1000000) + (benefit-1000000)*0.01

mon_benefit = int(raw_input("> "))

if mon_benefit <= 100000:
    print 'pass 0-10'
    print level_0_10(mon_benefit)
elif 100000<mon_benefit<=200000:
    print 'pass 10-20'
    print level_10_20(mon_benefit)
elif 200000<mon_benefit<=400000:
    print 'pass 20-40'
    print level_20_40(mon_benefit)
elif 400000<mon_benefit<=600000:
    print 'pass 40-60'
    print level_40_60(mon_benefit)
elif 600000<mon_benefit<=1000000:
    print 'pass 60-100'
    print level_60_100(mon_benefit)
else:
    print 'pass 100-infinite'
    print level_100_infinite(mon_benefit)


