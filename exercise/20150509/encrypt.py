#!/usr/bin/python

#alpha = [chr(i) for i in range(97,123)]

def encrypt(alpha):
    #return chr(ord(alpha)+13)
    return alpha
def encode(msg):
    return map(encrypt,msg)

def transmit(source,dest):
    dest = source
    return dest

def decode(msg):
    for i in range(len(msg)):
        msg[i] = chr(ord(msg[i])+2)

msg = raw_input("You want to send: ")
dest = []

print "Encrypt The msg"
confidential = encode(msg)

print 'The encrypt msg is',confidential

print 'Now transmitting:'
dest = transmit(confidential,dest)
print dest
print 'Destination decode the msg now.'

decode(dest)
type(dest)

print 'Receive msg from source is',' '.join(dest)
    
