from pwn import *
import hashlib
import operator
from itertools import product
from string import printable
import re

#context.log_level='DEBUG'
r = remote('199.247.6.180', 14001)
op = 0
vals = {}
h = r.recvlines(2)[1][49:54]
print 'Got ', h
i = 1
z = 0
while True:
	for x in product(printable, repeat=i):
		st = ''.join(x)
		c = md5sumhex(st)
		if c[:5] == h:
			print 'GOT IT: ',md5sumhex(st)
			r.send(st)
			z = 1
			break

	if z:
		break
	i +=1
r.recvline()
r.recvline()
s = r.recvline()
bou = re.findall('\((.*?)\)',s)[0]
lower = bou.split(',')[0]
upper = bou.split(',')[1].strip(" ")
print "[+] Upper bound "+upper
print "[+] Lower bound "+lower
upper_int  = int(upper)
lower_int = int(lower)
r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()
for i in range(lower_int, upper_int+1, 1):
	r.sendline("1")
	r.recvuntil("t: ")
	r.sendline(str(i))
	x = r.recvline()
	x = x.split("=")[1].strip('\n').strip(' ')
	vals[i] = float(x)
	op = op+1
print "[+] Total operation until now: "+str(op)
print vals
print "[+] Finding maximum outta those "
bubu = sorted(vals.items(), key=operator.itemgetter(1))
print "[+] This "+str(bubu[-1][0])+" gave highest "+str(bubu[-1][1])
print "[+] Followed by "+str(bubu[-2][0])+" with "+str(bubu[-2][1])
print "[+] Followed by "+str(bubu[-3][0])+" with "+str(bubu[-3][1])
r.interactive()
#r.close()
