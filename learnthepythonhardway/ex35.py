#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex35.py
# Created Time: Sat May  7 22:36:45 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import exit
import re
prog = re.compile('^\d+$')

def gold_room():
    print "This room is full of gold. How much do you want?"
    next = raw_input("> ")

    if prog.match(next) != None:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")
        if "take honey" in next:
            dead("The bear looks at you then slaps your face off.")
        elif 'taunt bear' in next and not bear_moved:
            print "The bear has moved from the door. You can go throug it now."
            bear_moved = True
        elif 'open door' in next:
            if bear_moved:
                gold_room()
            else:
                dead("The bear won't let you go and swallow you.")
        else:
            print "I got no idea what that means"

            

def cthulhu_room():
    print "you can choose answer a question or play 1024"
    next = raw_input('question or 1024? ')
    second_judge = next.isdigit() and int(next) == 1024
    if next.lower() == 'question':
        question()
    elif second_judge:
        play1024()
    else:
        dead("Don't you listen to me!! you are dead. Man.")

def question():
    pass

def play1024():
    print "Soon..."

def dead(msg):
    print msg,"you are dead piece! Sorry"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble aroud the room until you starve.")

start()
