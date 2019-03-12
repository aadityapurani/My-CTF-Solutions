from pwn import *

f = open('flag.enc', 'r')
l = f.read()
final = ''
for m in l.strip().split(','):
    if not m:
        final+=''
    if m != '0':
        final+='0'
    else:
        final+='1'
print unbits(final)
