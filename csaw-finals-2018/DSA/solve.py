import binascii
from MTRecover import *     #https://github.com/eboda/mersenne-twister-recover
import random
import json
import struct
import hashlib
import requests
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.rsa import _modinv
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric.dsa import *

'''
Solved by knapstack(@aaditya_purani) with theKidOfArcrania & c4pkirk
'''

q = 113682110273511993305117595002439707655399899191032492320097175281224216825509L
p = 16383739159776510143045518259689957604328868221586457207558055594442367557299259814084302024147970846423646628270733146558598493252800563058880387772765353151309886431380681712930948311011652809907860782451771375486702026822424601435746560856969583139070452116860969875276720072120496365787614603256846643073045448039324635734805124148830027581007195698809646465908524882892134810627218422202081127537234414771114823606172581273064386500248695295693846257097545078656729305004923464492472745004046595899677068327153315990502418761852352615570540647096382249960114318351762156536021243281812989274186614608763536446159L
y = 10932552827951492371518759727132943213569841508349909426502107635446347219345301565626282301284331327391741647317160801581899076429946361897351907054818314108404952692521782798003121300929331858600628453955108511216237686338172899090494187962345988719005708059369719026341320421147617883021618903286575591912791935979766959023304406551142467505926295853202873971480287617865928509266703526267394008179952493342709646595256765963244181196103346487820161576302142662564836048645755757583545229955660085447903160165838197885278436346801591152064904169305343150923471333067459686716708975726439855817037022332423860984063L
g = 10675097325257559738713775402182145091139368238328681175728542764092347116878144969928877946586736343442152741965211779516496089532912359935302652161077038338224019580917586106523101981264523867719811183555905170908839350043827346694689800787773527890625298392273719601076737408746095059109776728820647681730116352321802195361856854210365511006128969513911694539844312193693667539083511065812029610796210949453479930983400430688331183342737254963541805793946290885139569574302953806893910945713865291143970553245270512852489652301822481682024996995381213706535474506737905868028431239269748655331747355342878624921979L

hardcoded_message = "love"

def divide_bit(outputs):
	for i in range(313):
		bit64_num = struct.unpack(">Q", outputs[i])
		lower_32 = bit64_num[0] & 0xffffffff
		higher_32 = bit64_num[0] >> 32 & 0xffffffff
		divided_outputs.append(lower_32)
		divided_outputs.append(higher_32)

# random seeds in hex
outputs_from_server = []

for i in range(0, 313):
	print "[+] Getting hash "+str(i)
	r = requests.get("http://crypto.chal.csaw.io:1000/forgotpass")
	outputs_from_server.append(str(r.text.split('/')[-1]))

# hex decoded seeds
bytes_of_data= []

for i in xrange(0, len(outputs_from_server)):
	bytes_of_data.append(binascii.unhexlify(outputs_from_server[i]))

# 312 requests needed

divided_outputs = []

divide_bit(bytes_of_data)

print len(divided_outputs)

mtr = MT19937Recover()
r2 = mtr.go(divided_outputs)		# our state

# Testomg
r = requests.get("http://crypto.chal.csaw.io:1000/forgotpass")
boo = binascii.unhexlify(str(r.text.split('/')[-1]))
bit64_num = struct.unpack(">Q", boo)
print "From server the next number is: " + str(bit64_num[0])

our_gen =  r2.getrandbits(64)
print "Our next number is: " + str(our_gen)

if our_gen == bit64_num[0]:
	print "[+] Owned!"

k = r2.randrange(2, q)
r_int = pow(g, k, p) % q
kinv = _modinv(k, q)


r1 = requests.get("http://crypto.chal.csaw.io:1000/sign/"+hardcoded_message)
s = json.loads(str(r1.text))['s']
r_server = json.loads(str(r1.text))['r']

print r_int
print r_server

# r^-1 (s.k -H(m)) % q

h_ourend = hashlib.sha1(hardcoded_message).digest()
h = int(h_ourend.encode('hex'), 16)
x =(s*k)-h
x = x * _modinv(r_int, q) % q
print x

# p,g,q,x will be private key

param = DSAParameterNumbers(p,q,g)
pub = DSAPublicNumbers(y, param)
pri_key = default_backend().load_dsa_private_numbers(DSAPrivateNumbers(x,pub))

r4 = requests.get("http://crypto.chal.csaw.io:1000/challenge")
b64_chall = str(r4.text)
#print b64_chall
sig = pri_key.sign(b64_chall, hashes.SHA256())
final_sig = binascii.hexlify(sig)

r4 = requests.post("http://crypto.chal.csaw.io:1000/capture", data={'challenge':b64_chall, 'signature':final_sig})
print r4.text

#flag{NowyourereadytocrackthePS3YeahSonydidthiswithECDSA}
