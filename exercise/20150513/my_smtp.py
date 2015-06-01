#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: my_smtp.py
# Created Time: Thu May 14 00:13:40 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from email.mime.text import MIMEText

msg = MIMEText('Hello, send by python...','plain','utf-8')

from_addr = raw_input("From:")
password = raw_input("Password:")

smtp_server = raw_input("SMTP server: ")

to_addr = raw_input("To: ")

import smtplib

server = smtplib.SMTP(smtp_server,587)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr,],msg.as_string())
server.quit()

