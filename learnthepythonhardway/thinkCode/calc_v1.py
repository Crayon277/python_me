#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: calc_v1.py

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

# def add(a,b):
#     return a+b
#
# def subtract(a,b):
#     return a-b
#
# def multiply(a,b):
#     return a*b
#
# def divide(a,b):
#     return a/b


print "Welcome to calculation version1!"
print "choose an manipulation"
print "1.addition"
print "2.subtraction"
print "3.multiplation"
print "4.divition"
print "5.Quit"

while 1:
    choose = int(raw_input("> "))
    if choose == 5:
        break

    print "Input two operand"
    op1 = float(raw_input("OP1: "))
    op2 = float(raw_input("OP2: "))

    if choose == 1:
        print "%f + %f = %f"%(op1,op2,op1+op2)
    elif choose == 2:
        print "%f - %f = %f"%(op1,op2,op1-op2)
    elif choose == 3:
        print "%f * %f = %f"%(op1,op2,op1*op2)
    else:
        print "%f / %f = %f"%(op1,op2,op1/op2)


print "Thank you for using calc v1. See you next time"
