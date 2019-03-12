# -*- encoding: utf-8 -*-

mand=u"㐾㐻㐌㐟㐀㐏㑖㐄㐓㐀㐴㐀㐄㐻㐉㐴㐷㐻㐾㐇㑎㑟"
codepts =[]

offset = 0x3400

for m in mand:
    ans = int(hex(ord(m)),16) - offset
    codepts.append(ans)

hashmap_char= {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
    '{':26,
    '|':27,
    '}':28
}

oeis = [ 0, 1, 2, 4, 5, 7, 9, 12, 13, 15, 17, 20, 22, 25, 28, 32, 33, 35, 37, 40, 42, 45, 48, 52, 54, 57, 60, 64, 67, 71, 75, 80, 81, 83, 85, 88, 90, 93, 96, 100, 102, 105, 108, 112, 115, 119, 123, 128, 130, 133, 136, 140, 143, 147, 151, 156, 159, 163, 167, 172, 176, 181, 186]

f_dict = {}

for k,v in hashmap_char.items():
    f_dict[k] = v + oeis[v]

flag=""

for i in xrange(0, len(codepts)):
    flag+=f_dict.keys()[f_dict.values().index(codepts[i])]

print flag
#utctf{characterstudy}
