import os
import collections

tp = ""
zaje = []
flag = ""

def most_common(s):
	return collections.Counter(s).most_common(1)[0][0]

for i in xrange(0, 28):
	if tp != "":
		zaje.append(tp)
		tp = ""
	if i == 27:
		break
	for j in xrange(0, 100):
		finale = 0
		pathz = "/path/to/bcactf/bigdata/OUT/"+str(i)+"/"+str(j)
		f = open(pathz, 'r')
		xx = f.readline().strip('\n')
		lenz = len(xx)
		for x in xx:
			finale += ord(x)
		tp+=chr(finale//lenz)
#print zaje
for z in zaje:
	flag+=most_common(z)

print flag

#bcactf{crunch1ng_num5_c00l}
