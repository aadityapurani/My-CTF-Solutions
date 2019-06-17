from itertools import *

f = open('one.txt', 'r')
x = f.readline().strip('\n')
x = x.split(' ')
f1 = open('two.txt', 'r')
xx = f1.readline().strip('\n')
xx = xx.split(' ')
finale = []


for i,j in zip(x, xx):
	finale.append(chr(int(i[2:],16)+int(j[2:],16)))

print ''.join(finale)

#bcactf{1_h0p3_y0u_us3_pyth0n}
