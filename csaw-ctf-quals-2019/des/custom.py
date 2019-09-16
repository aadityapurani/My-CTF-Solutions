from Crypto.Cipher import DES
import binascii

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
def createChallenge():
	createKey("01fe01fe01fe01fe","key1_test")			# key should be in hex
	createKey("01fe01fe01fe01fe","key2_test")			# key should be in hex

	plainText = open('FLAG_test.txt').read()			    # Flag in plaintext
	key1 = open('key1_test').read()					# key1 i dunno

	byte = desEncrypt(plainText,key1)			# desEncryption function called with key1 & pt

	key2 = open('key2_test').read()					# key2 i dunno
	cipherText = desEncrypt(byte,key2)			# two times encryption leet

	# make hex of your pre-final ct and encode it :bigbrainenergy:
	cipherText = encodeText(binascii.hexlify(cipherText),9133337)	
	with open('FLAG_TEST.enc', 'w') as f:
		f.write(cipherText)
	f.close()

	# Decrypt shit
	with open('FLAG_TEST.enc', 'r') as f1:
		cts = f1.readlines()[0]

	prefinal_ct = decodeText(cts, 9133337)
	final_ct = binascii.unhexlify(prefinal_ct)

	ct_step1 = desDecrypt(final_ct, key2)
	ct_step0 = desDecrypt(ct_step1, key1)
	print "Finished: "
	print ct_step0

createChallenge()
