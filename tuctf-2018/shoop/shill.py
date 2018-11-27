#!/usr/bin/python
stage1=""
stage2=""
final = ['*']*21
goal="jmt_j]tm`q`t_j]mpjtf^"
for k in xrange(0,21):
    stage1+= goal[(k+10)%21]
print "stage 1 done"
for j in xrange(0,21):
    stage2 += chr(ord(stage1[j])+5)
print "stage 2 done"
for i in xrange(20, -1,-1):
    final[21-i-1] = stage2[i]
if len(final) == 21:
    print "all shilled"
print "".join(final)
#everybodyrockyourbody
