print 
variable name 
print "", 
print " " + ""
%r
raw_input("> ")
int(raw_input())
float(raw_input())
from sys import argv
argv is a list

from os.path import exists
exists("filename") is judge if filename is exist in current path

open(filename) default mode is read

open(filename , "{mode}") 
{mode} is r,w,a,+,U, r+ is reading and writing

file.read()
file.readline()

file.write()
file.truncate([number]) cut file like initiate file to empty if number is not given, otherwise, number bytes of file is remind.
 

def fun(*argv):
	argv is a list if the argument is given by format like *argv


