#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: creeper_pydoc.py
# Created Time: Sat May 16 08:48:22 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import urllib2
import os
import re
import pdb

def save_html(urlname):
    main_url = r'https://docs.python.org/2/library'
    main_dir = os.getcwd()

    url = main_url + '/' + urlname + '.html'
    file_name = main_dir + '/' + urlname + '.html'
    try:
        print "try ...."
        req = urllib2.urlopen(url)
        urlfile = open(file_name,'w')
        urlfile.write(req.read())

    except IOError:
        print "file open fails"
    except:
        print url
    finally:
        urlfile.close()

save_html('index')
req = urllib2.urlopen(r'https://docs.python.org/2/library/index.html')
p = re.compile(r'''<li class="toctree-.+?"><a class="reference internal" href="(.+?).html">.+?</a></li>''')
matchs = p.findall(req.read())

for row in matchs:
    save_html(row)
