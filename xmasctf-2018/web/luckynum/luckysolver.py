import re
from bs4 import BeautifulSoup
import requests

brute_guess = 'X-MAS{'.encode('hex')
brute_guess_p = 'X-MAS'
url = "http://199.247.6.180:12005/?page="

for i in xrange(1000, 3000):
	r = requests.get(url+str(i))
	soup = BeautifulSoup(r.text, 'lxml')
	g = str(soup.find_all('p')[1])
	goal = re.findall(">\n(.+?)<", g)[0]
	if goal.find(brute_guess) != -1:
		print "[+] Candidate Found "+str(i)
		print goal
		break
	elif goal.find(brute_guess_p) != -1:
		print "[+] Candidate Found (plain) "+str(i)
		print goal
		break
	else:
		print "[!] "+str(i)+" got "+goal
