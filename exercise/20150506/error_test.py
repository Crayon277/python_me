import sys

try:
        s = raw_input("Enter Something -->")
except EOFError:
        print '\nWhy did you do on EOF on me?'
        
except:
        print '\nSome error / exception occurred.'
else:
        print 'Done'


class ShortInputException(Exception):
        """A user-defined exception class."""
        def __init__(self,length,atleast):
                Exception.__init__(self)
                self.length = length
                self.atleast = atleast

try :
        s = raw_input("Enter something-->")
        if len(s) < 3:
                raise ShortInputException(len(s),3)

except EOFError:
        print "\nwhy did you do this to me?"

except ShortInputException ,x:
        print 'ShorInputException: The input was of length %d, was expecting at least %d'%(x.length,x.atleast)
        #print "Some error occurred."
else:
        print "No exception was raised."


import time

try:
        f =file('poem.txt')
        while 1:
                line  = f.readline()
                if len(line) == 0:
                        break
                time.sleep(2)
                print line
finally:
        f.close()
        print 'Cleaning up ... closed the file'


