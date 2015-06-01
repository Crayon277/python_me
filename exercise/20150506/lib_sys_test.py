#!/usr/bin/python

import sys

def readfile(filename):
    """print a file to the standard output"""
    f = file(filename)
    while 1 :
        line = f.readline()
        if len(line) == 0:
            break
        print line
    f.close()

if (len(sys.argv) < 2):
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print 'version 1.2'
    elif option == "help":
        print '''This program print files to the standard output.
                Any number of files can be specified
                oOptions include:
                --version: Prints the version nubmer
                --help : Display this help'''
    else:
        print 'Unknown option.'
        sys.exit()
else:
    for filename in sys.argv[1:]:
        print '==========%s============'%filename
        readfile(filename)
        print '==========%s============'%filename
