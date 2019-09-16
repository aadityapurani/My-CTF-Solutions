from Crypto.Cipher import DES
import binascii
import itertools
import sys

# Low data-set
'''
combinatory=[
"011F011F010E010E",
"1F011F010E010E01",
"01E001E001F101F1",
"E001E001F101F101",
"01FE01FE01FE01FE",
"FE01FE01FE01FE01",
"1FE01FE00EF10EF1",
"E01FE01FF10EF10E",
"1FFE1FFE0EFE0EFE",
"FE1FFE1FFE0EFE0E",
"E0FEE0FEF1FEF1FE",
"FEE0FEE0FEF1FEF1"
]
'''

# wiki data-set
'''
combinatory=[
"011F011F010E010E",
"1F011F010E010E01",
"01E001E001F101F1",
"E001E001F101F101",
"01FE01FE01FE01FE",
"FE01FE01FE01FE01",
"1FE01FE00EF10EF1",
"E01FE01FF10EF10E",
"1FFE1FFE0EFE0EFE",
"FE1FFE1FFE0EFE0E",
"E0FEE0FEF1FEF1FE",
"FEE0FEE0FEF1FEF1",
"E1E1E1E1F0F0F0F0",
"1E1E1E1E0F0F0F0F",
"0000000000000000",
"FFFFFFFFFFFFFFFF",
"1F1F1F1F0E0E0E0E",
"E0E0E0E0F1F1F1F1",
"FEFEFEFEFEFEFEFE",
"0101010101010101"]
'''

# NIST weak key list

combinatory=[
"0101010101010101",
"01011F1F01010E0E",
"01011F1F01010E0E",
"0101E0E00101F1F1",
"0101FEFE0101FEFE",
"011F011F010E010E",
"011F1F01010E0E01",
"011FE0FE010EF1FE",
"011FFEE0010EFEF1",
"01E001E001F101F1",
"01E01FFE01F10EFE",
"01E0E00101F1F101",
"01E0FE1F01F1FE0E",
"01FE01FE01FE01FE",
"01FE1FE001FE0EF1",
"01FEE01F01FEF10E",
"01FEFE0101FEFE01",
"1F01011F0E01010E",
"1F011F010E010E01",
"1F01E0FE0E01F1FE",
"1F01FEE00E01FEF1",
"1F1F01010E0E0101",
"1F1F1F1F0E0E0E0E",
"1F1FE0E00E0EF1F1",
"1F1FFEFE0E0EFEFE",
"1FE001FE0EF101FE",
"1FE01FE00EF10EF1",
"1FE0E01F0EF1F10E",
"1FE0FE010EF1FE01",
"1FFE01E00EFE01F1",
"1FFE1FFE0EFE0EFE",
"1FFEE0010EFEF101",
"1FFEFE1F0EFEFE0E",
"E00101E0F10101F1",
"E0011FFEF1010EFE",
"E001E001F101F101",
"E001FE1FF101FE0E",
"E01F01FEF10E01FE",
"E01F1FE0F10E0EF1",
"E01FE01FF10EF10E",
"E01FFE01F10EFE01",
"E0E00101F1F10101",
"E0E01F1FF1F10E0E",
"E0E0E0E0F1F1F1F1",
"E0E0FEFEF1F1FEFE",
"E0FE011FF1FE010E",
"E0FE1F01F1FE0E01",
"E0FEE0FEF1FEF1FE",
"E0FEFEE0F1FEFEF1",
"FE0101FEFE0101FE",
"FE011FE0FE010EF1",
"FE01E01FFE01F10E",
"FE01FE01FE01FE01",
"FE1F01E0FE0E01F1",
"FE1F1FFEFE0E0EFE",
"FE1FE001FE0EF101",
"FE1FFE1FFE0EFE0E",
"FEE0011FFEF1010E",
"FEE01F01FEF10E01",
"FEE0E0FEFEF1F1FE",
"FEE0FEE0FEF1FEF1",
"FEFE0101FEFE0101",
"FEFE1F1FFEFE0E0E",
"FEFEE0E0FEFEF1F1",
"FEFEFEFEFEFEFEFE"
]


# preparing bruter
prep = [p for p in itertools.product(combinatory, repeat=2)]

# known IV
IV = '13371337'

# Hashmap because offset is known
known = {
	'09133337':'0',
	'09133338':'1',
	'09133339':'2',
	'09133340':'3',
	'09133341':'4',
	'09133342':'5',
	'09133343':'6',
	'09133344':'7',
	'09133345':'8',
	'09133346':'9',
	'09133348':'a',
	'09133349':'b',
	'09133350':'c',
	'09133351':'d',
	'09133352':'e',
	'09133353':'f'

}

def isprintable(s, codec='utf8'):
    try: s.decode(codec)
    except UnicodeDecodeError: return False
    else: return True

# Always returns 8, because offset is known
def getNibbleLength(offset):	
	if str(offset)[0]=="9":						# If first byte is '9', then increment length of input
		return len(str(offset))+1
	return len(str(offset))						# Else just return length of input

def duck(aChr):
	try:
		return int(aChr)
	except:
		return "abcdef".index(aChr)+11

# Encode text will have 8 blocks of output too
def encodeText(plainText,offset):
	hexEncoded = plainText.encode("hex")		# hex it again
	nibbleLen = getNibbleLength(offset)			# Always 8
	output = ""									# Nothing for now
	for i in range(0,len(hexEncoded),2):		
		hexByte = hexEncoded[i:i+2]				# club 2 bytes of hexEncoded
		try: 
			output += str(duck(hexByte[0]) + offset).rjust(nibbleLen,"0")
			output += str(duck(hexByte[1]) + offset).rjust(nibbleLen,"0")
		except:
			continue
	return output

# My hacky decoder ;)
def decodeText(cipherText, offset):
	output = ""
	for i in range(0, len(cipherText), 8):
		shitByte = cipherText[i:i+8]
		try:
			output += known[shitByte]
		except Exception as e:
			print e
			print "Broke"
			continue
	hexDecoded = output.decode("hex")
	return hexDecoded

# pads to make sure a block remains multiple of 8 bytes
def padInput(input):
	bS = len(input)/8
	if len(input)%8 != 0:
		return input.ljust((bS+1)*8,"_")	
	return input
	
# Simple encryptor
def desEncrypt(input,key):
	cipher = DES.new(key, DES.MODE_OFB, IV)
	msg = cipher.encrypt(padInput(input))			# pads input to fulfil block size
	return msg

# Simple decryptor
def desDecrypt(input, key):
	cipher = DES.new(key, DES.MODE_OFB, IV)
	msg = cipher.decrypt(input)
	return msg
		
# unhex the key and saving it
def createKey(hex,fileName):
	with open(fileName, 'wb') as f:
		f.write(binascii.unhexlify(hex))

# crux of the challenge
def createChallenge(key1, key2):
	createKey(key1,"key1_test")			# key should be in hex
	createKey(key2,"key2_test")			# key should be in hex

	key1 = open('key1_test').read()

	key2 = open('key2_test').read()

	# Decrypt shit
	with open('FLAG.enc', 'r') as f1:
		cts = f1.readlines()[0]

	prefinal_ct = decodeText(cts, 9133337)
	final_ct = binascii.unhexlify(prefinal_ct)

	ct_step1 = desDecrypt(final_ct, key2)
	ct_step0 = desDecrypt(ct_step1, key1)
	
	if isprintable(ct_step0):
		print ct_step0


	#if "__" in ct_step0:
	#	print ct_step0
		#sys.exit(0)

	#if 'flag' in ct_step0:
	#	print ct_step0
	print "Nope"


print len(prep)
for i in prep:
	createChallenge(i[0], i[1])
