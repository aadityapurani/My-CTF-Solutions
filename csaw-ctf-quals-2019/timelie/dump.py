import requests
from bs4 import BeautifulSoup

for i in xrange(1, 1001):
    print "Trying "+str(i)
    s = requests.Session()
    api ="http://crypto.chal.csaw.io:1005/"
    filename='input.xml'
    up = {'file':(filename, open(filename, 'rb'), "multipart/form-data")}
    r = s.post(api+"musicin", files=up)
    oo = r.text
    soup = BeautifulSoup(oo, "html.parser")
    for a in soup.find_all('a', href=True):
        x= a['href']

    xx= x.split('/')[2]
    r = s.get(api+x)
    with open('output_'+str(i)+'.xml','w') as f:
        f.write(r.text)
    f.close()
