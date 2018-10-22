import json

'''
Instruction opInput_Device (CMD, …) 
Opcode 0x99
Now here we are looking at the read values from the sensor sent from ev3 to localhost ethernet
It seems like # for black and <space> for white will recreate the image
Example payload:  99 1d 00 02 00 02 01 60
length = 8 Bytes
99 = Opcode
1d = READY_SI 
00 = Layer number 0
02 = Port Number of Sensor
00 = Type (default)
02 = Mode (default)
01 = Returned values (eh?)
Seems this payload is send as a request to read the values from sensor I think and the ev3 will respond it.
Hence, the communication weill be from LegoSyst -> localhost ethernet this case as values taken from robot will be sent of.
The response data variantions are minute :
00 c0 80 
00 80 3f
+   +  45       (1st + is faster, 2nd is increment)
00 c0 80
00 80 3f
-  -  45
00 c0 40
00 80 3f
+   +  45     (1st + is faster, 2nd is increment)
This looks like the  ++45 means robot is making 180 degree U-Turn towards Right hand side
- - 45 is to nullify I think, making 180 degree U-Turn towards Left hand side
and c0 80 , c0 40 means White color read
80 3f means black color read
>>> int('c0', 16), int('80',16)
(192, 128)
>>> int('80', 16), int('3f',16)
(128, 63)
So, if the color is black then seems sensor value will be down 
----> 1
<----- 2
-------> 3
............
--------> 11
So, robot will traverse 11 times on the mattress.
'''

with open('ev3-scanner.json') as f:
	data = json.load(f)

alert = 0
total_turn = 0

first_round = ""
second_round = ""
third_round = ""
fourth_round =""
fifth_round = ""
six_round =""
seven_round=""
eight_round = ""
nine_round = ""
ten_round = ""
eleven_round = ""

for i in xrange(0, len(data)):
	tmp = "".join(data[i]["_source"]["layers"]["data"]["data.data"].split(":"))
	if len(tmp) == 18:
		i = 1
		identifier1 = tmp[12:][0:2]
		identifier2 = tmp[12:][2:4]
		identifier3 = tmp[12:][4:6]

		if identifier3 == '45':		# Likely 180 U Turn
			alert = 1
		#	break					# start of the fucking turn
			continue

		elif identifier2 == 'c0' or identifier3 == '40' and identifier1 == '00':	# Likely white
			if alert == 1:		# Turn has been taken
				print "[+] Turn was taken"
				alert = 0
				total_turn += 1
				if total_turn == 0:
					first_round += " "
				elif total_turn == 1:
					second_round += " "
				elif total_turn == 2:
					third_round += " "
				elif total_turn == 3:
					fourth_round += " "
				elif total_turn == 4:
					fifth_round += " "
				elif total_turn == 5:
					six_round += " "
				elif total_turn == 6:
					seven_round += " "
				elif total_turn == 7:
					eight_round += " "
				elif total_turn == 8:
					nine_round += " "
				elif total_turn == 9:
					ten_round += " "	
				elif total_turn == 10:
					eleven_round += " "																																												
			if total_turn == 0:
				first_round += " "
			elif total_turn == 1:
				second_round += " "
			elif total_turn == 2:
				third_round += " "
			elif total_turn == 3:
				fourth_round += " "
			elif total_turn == 4:
				fifth_round += " "
			elif total_turn == 5:
				six_round += " "
			elif total_turn == 6:
				seven_round += " "
			elif total_turn == 7:
				eight_round += " "
			elif total_turn == 8:
				nine_round += " "
			elif total_turn == 9:
				ten_round += " "
			elif total_turn == 10:
				eleven_round += " "				

		elif identifier2 == '80' and identifier1 == '00':    # Likely black 
			if alert == 1:
				print "[+] Turn was taken"
				alert = 0
				total_turn += 1
				if total_turn == 0:
					first_round += "#"
				elif total_turn == 1:
					second_round += "#"
				elif total_turn == 2:
					third_round += "#"
				elif total_turn == 3:
					fourth_round += "#"
				elif total_turn == 4:
					fifth_round += "#"
				elif total_turn == 5:
					six_round += "#"
				elif total_turn == 6:
					seven_round += "#"
				elif total_turn == 7:
					eight_round += "#"
				elif total_turn == 8:
					nine_round += "#"
				elif total_turn == 9:
					ten_round += "#"
				elif total_turn == 10:
					eleven_round += " "			
			if total_turn == 0:
				first_round += "#"
			elif total_turn == 1:
				second_round += "#"
			elif total_turn == 2:
				third_round += "#"
			elif total_turn == 3:
				fourth_round += "#"
			elif total_turn == 4:
				fifth_round += "#"
			elif total_turn == 5:
				six_round += "#"
			elif total_turn == 6:
				seven_round += "#"
			elif total_turn == 7:
				eight_round += "#"
			elif total_turn == 8:
				nine_round += "#"
			elif total_turn == 9:
				ten_round += "#"
			elif total_turn == 10:
				eleven_round +="#"			


print "[+] Total turn taken was "+str(total_turn)
print first_round
print second_round[::-1]
print third_round
print fourth_round[::-1]
print fifth_round
print six_round[::-1]
print seven_round
print eight_round[::-1]
print nine_round
print ten_round[::-1]
print eleven_round

print "*************************************************************************************"
print len(first_round)
print len(second_round)
print len(third_round)
print len(fourth_round)
print len(fifth_round)
print len(six_round)
print len(seven_round)
print len(eight_round)
print len(nine_round)
print len(ten_round)
print len(eleven_round)
#hitcon{EV3GYROSUCKS}
