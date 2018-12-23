import requests
from bs4 import BeautifulSoup
import re

sesx = requests.session()

def xgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = xgcd(b % a, a)
        return (g, x - (b // a) * y, y)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def solve(s):
    nrand = len(s)
    t = []
    for x in range(nrand-1):
        t.append(s[x+1]-s[x])
    u = []
    for x in range(nrand-3):
        u.append(abs(t[x+2]*t[x]-t[x+1]**2))
    m = reduce(gcd, u)
    r4 = s[-4]
    r3 = s[-3]
    r2 = s[-2]
    r1 = s[-1]
    x = r2-r4
    b = r1-r3
    if x<0:
        x*=-1
        b*=-1
    if b<0:
        b=b%m
    g,x2,y2 = xgcd(x, m)
    if g==1:
        xi = x2%m
        a=(b*xi)%m
        c=(r1-r2*a)%m
        return [m,a,c]
    else:
        return None

'''
# Altho didn't used
def missingcalc(s):
    seed = s[0]
    for m in xrange(seed, 10*seed):
        for a in xrange(2, m):
            c = s[3] - ((s[2]*a)%m)
            if c < 0:
                c+=m
            my_x2 = (s[2]*a+c)%m
            assert my_x2 == s[3]
            my_x3 = (s[3]*a+c)%m
            my_x4 = (s[4]*a+c)%m
            my_x5 = (s[5]*a+c)%m 
            if my_x3 == s[4]:
                return m,a,c
'''

goal = 20
s = []

print "[+] Collecting samples"

for i in xrange(0, goal):
    r = sesx.get("http://45.76.90.207:12000/?guess=1")
    so = BeautifulSoup(r.text, "lxml")
    meh = so.find_all('p')[1]
    meh = str(meh)
    num = int(re.findall("/>(.+?)<", meh)[1])
    s.append(num)

print "[+] Samples collected"
print "[+] Trying to break"
m, a, c = solve(s)
if not m or not a or not c:
    print "[-] Retry"
print m,a,c
print "[+] Pwned!"
nextNum = (a*s[-1]+c)%m
for i in xrange(0, 50):
    r1 = sesx.get("http://45.76.90.207:12000/?guess="+str(nextNum))
    nextNum = ((a*nextNum)+c)%m
    print r1.text
    
# X-MAS{Bru73_F0rc3_1s_gr34t_bu7_LCG_1s_b3tt3r___}
