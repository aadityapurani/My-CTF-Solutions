import json
import operator

'''
Have to read documentation and see how opUI_DRAW worked
840501xxxxyyyyff
opcode text black xcord ycord char
Communication happens from localhost ethernet -> ev3 
'''


# Taken from https://stackoverflow.com/questions/10664856/make-dictionary-with-duplicate-keys-in-python
class DictList(dict):
    def __setitem__(self, key, value):
        try:
            # Assumes there is a list on the key
            self[key].append(value) 
        except KeyError: # if fails because there is no key
            super(DictList, self).__setitem__(key, value)
        except AttributeError: # if fails because it is not a list
            super(DictList, self).__setitem__(key, [self[key], value])

blk1=""
blk2=""
blk3=""
blk4=""
dict1 = DictList()
dict2 = DictList()
dict3 = DictList()
dict4 = DictList()

# btrfcomm && packetlogger.type==0x02 && data
with open('data_ev3_1.1') as f:
	data = json.load(f)

for j in xrange(0, 4):
	data_dump=""
	stack=""
	for i in xrange(0, len(data)):
		tmp = "".join(data[i]["_source"]["layers"]["data"]["data.data"].split(":"))
		if j ==0:
			#print "[+] Retrieving block 1"
			if '2884' in tmp:
				meh = tmp.find('2884')
				beep = tmp[meh+4:][:2]
				xcord = tmp[meh-4:][:4]
				if '00' in xcord[:2]:
					xcord = tmp[meh-6:][:6]
				xcord_int = int(xcord, 16)
				beep_nice = beep.decode('hex')
				if beep_nice in stack:
					beep_nice = beep_nice+"#"
				stack +=beep_nice
				dict1[beep_nice] = xcord_int
				#blk1 += beep_nice
				#print data_dump
		elif j == 1:
			#print "[+] Retrieving block 2"
			if '3684' in tmp:
				meh = tmp.find('3684')
				beep = tmp[meh+4:][:2]
				xcord = tmp[meh-4:][:4]
				if '00' in xcord[:2]:
					xcord = tmp[meh-6:][:6]
				xcord_int = int(xcord, 16)
				beep_nice = beep.decode('hex')
				if beep_nice in stack:
					beep_nice = beep_nice+"#"
				stack +=beep_nice
				dict2[beep_nice] = xcord_int
				#print data_dump
		elif j == 2:
			#print "[+] Retrieving block 3"
			if '4484' in tmp:
				meh = tmp.find('4484')
				beep = tmp[meh+4:][:2]
				xcord = tmp[meh-4:][:4]
				if '00' in xcord[:2]:
					xcord = tmp[meh-6:][:6]
				xcord_int = int(xcord, 16)
				beep_nice = beep.decode('hex')
				if beep_nice in stack:
					beep_nice = beep_nice+"#"
					count +=1
				stack +=beep_nice
				dict3[beep_nice] = xcord_int
				#print data_dump
		elif j == 3:
			#print "[+] Retrieving block 4"
			if '5284' in tmp:
				meh = tmp.find('5284')
				beep = tmp[meh+4:][:2]
				xcord = tmp[meh-4:][:4]
				if '00' in xcord[:2]:
					xcord = tmp[meh-6:][:6]
				xcord_int = int(xcord, 16)
				beep_nice = beep.decode('hex')
				if beep_nice in stack:
					beep_nice = beep_nice+"#"
				stack +=beep_nice
				dict4[beep_nice] = xcord_int
				#print data_dump

print dict1
sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(1))
for i in xrange(0, len(sorted_dict1)):
	blk1 += sorted_dict1[i][0]

sorted_dict2 = sorted(dict2.items(), key=operator.itemgetter(1))
for i in xrange(0, len(sorted_dict2)):
	blk2 += sorted_dict2[i][0]

sorted_dict3 = sorted(dict3.items(), key=operator.itemgetter(1))
for i in xrange(0, len(sorted_dict3)):
	blk3 += sorted_dict3[i][0]

sorted_dict4 = sorted(dict4.items(), key=operator.itemgetter(1))
for i in xrange(0, len(sorted_dict4)):
	blk4 += sorted_dict4[i][0]


x = blk1.replace("#", '')
y = blk2.replace("#", '')
z = blk3.replace("#", '')
zz = blk4.replace("#", '')

print x+y+z+zz
#hitcon{m1nd5t0rm_communication_and_firmware_developer_kit}
