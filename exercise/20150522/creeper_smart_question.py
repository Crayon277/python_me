#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: creeper_smart_question.py
# Created Time: Fri May 22 10:00:10 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import urllib2,re,os

def save_html(path):
    main_url = "http://www.catb.org/~esr/faqs/smart-questions.html"
    main_dir = "/Users/Crayon_277/Develop/Project/python/exercise/20150522/downloadWeb"

    req = urllib2.urlopen(main_url +path)
    with open(main_dir+'/'+path.split("#")[1],'w') as save_dir:
        save_dir.write(req.read())


patter = re.compile(r'''<span class=".+?"><a href = "(.+?)">.+?</a></span>''')

