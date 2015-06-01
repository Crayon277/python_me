#!/usr/bin/python
#-*-coding: utf-8 -*-

print len(u'中文测试') #4
print len('中文测试')  #12

# print len('中文测试'.encode('utf-8'))
#// UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

print len(u'中文测试'.encode('utf-8')) #12
print len('中文测试'.decode('utf-8'))  #4

#print len(u'中文测试'.decode('utf-8'))
#  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/utf_8.py", line 16, in decode
#    return codecs.utf_8_decode(input, errors, True)
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-3: ordinal not in range(128)

