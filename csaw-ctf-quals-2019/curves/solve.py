from pwn import *

#context.log_level='DEBUG'
r =remote('crypto.chal.csaw.io', 1000)
i=2000
while True:
	print i
	r.recvuntil("ret?")
	r.sendline(str(i))
	ftw=r.recvline()
	ftw1=r.recvline()
	#print ftw1.strip('\n')
	if not "WRONGGG" in ftw1:
		print ftw1
		break
	else:
		i = i+1
		#continue
# 
14 Sep
flag{use_good_params}
