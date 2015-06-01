#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: pagesource.py
# Created Time: Wed May 13 14:32:47 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import urllib2
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = None

    def handle_starttag(self,tag,attrs):
        if tag == 'time':
            self.flag = 'time'
    def handle_data(self,data):
        if self.flag == 'time':
            print data




url = "https://www.python.org/events/python-events/"
page = urllib2.urlopen(url)

data = page.read()

#print data

hp = MyHTMLParser()
hp.feed(data)


