#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 16_output_given_format_date.py
# Created Time: Tue May 17 15:08:04 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#输出指定格式的日期

import time
import datetime

if __name__ == '__main__':
    print time.strftime("%Y-%m-%d %H:%M:%S")

    print (datetime.date.today().strftime('%Y/%m/%d'))
    
    year = int(raw_input("> "))
    month = int(raw_input("> "))
    day = int(raw_input("> "))
    createBirthdate = datetime.date(year,month,day)

    print createBirthdate.strftime('%m/%d/%Y')

    createBirthNextDate = createBirthdate+datetime.timedelta(days=1)
    print createBirthNextDate.strftime('%m/%d/%Y')



