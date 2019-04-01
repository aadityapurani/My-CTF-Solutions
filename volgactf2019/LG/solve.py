import random
import gmpy2
from Crypto.Cipher import AES
import sys
import os
from pwn import *

context.log_level='DEBUG'  

def calc_det(i,j,X):
    """ Calculate the values for the matrix[lattice] """
    a1 = X[i] - X[0]
    b1 = X[i+1] - X[1]
    a2 = X[j] - X[0]
    b2 = X[j+1] - X[1]

    """ Calculate the determinant """
    det = a1*b2 - a2*b1
    return abs(det)

def GCD(a,b):
    """ Euclidean Algo"""
    a = abs(a)
    b = abs(b)
    while a:
            a,b = long(b%a),a
    return b


r = remote('95.213.235.103','8801')
r.recvline()
r.recvline()
X=[]
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))
X.append(int(r.recvline().strip('\n')))

Det_X = []
Det_X.append(calc_det(1,2,X))
print Det_X
Det_X.append(calc_det(2,3,X))
print Det_X
Det_X.append(calc_det(3,4,X))
print Det_X
Det_X.append(calc_det(4,5,X))
print Det_X

found_p = GCD(Det_X[0], Det_X[1])
found_p = GCD(found_p, Det_X[2])
found_p = GCD(found_p, Det_X[3])
print found_p
mod_inv_a = gmpy2.invert((X[2]-X[3]), found_p)
print (X[2]-X[3])%found_p
found_a = ((X[3] - X[4])*mod_inv_a)%found_p
print found_a

found_c = (X[4] - found_a*X[3])%found_p
print found_c

nextNum = (found_a*X[-1]+found_c)%found_p
print str(nextNum)
#print "Next Num seems "+str(nextNum)
r.sendline(str(nextNum))
r.recvall()
