import socketserver
import random
import signal
import time
import gmpy2
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

random.seed()

lb = 1568412828.8400000
st = 0.0000001
# 1568412828.8534966
# flag{ooo000_f4ul7y_4nd_pr3d1c74bl3_000ooo}

t = time.time()


def gen_prime():
    base = random.getrandbits(1024)
    off = 0
    while True:
        if gmpy2.is_prime(base + off):
            break
        off += 1
    p = base + off

    return p, off



def s2n(s):
    return bytes_to_long(bytearray(s, 'latin-1'))


def n2s(n):
    return long_to_bytes(n).decode('latin-1')


class RSA(object):
    def __init__(self):
        pass

    def generate(self, p, q, e=0x10001):
        self.p = p
        self.q = q
        self.N = p * q
        self.e = e
        phi = (p - 1) * (q - 1)
        self.d = inverse(e, phi)

    def encrypt(self, p):
        return pow(p, self.e, self.N)

    def decrypt(self, c):
        return pow(c, self.d, self.N)

    # ===== FUNCTIONS FOR PERSONAL TESTS, DON'T USE THEM =====
    def TEST_CRT_encrypt(self, p, fun=0):
        ep = inverse(self.d, self.p - 1)
        eq = inverse(self.d, self.q - 1)
        qinv = inverse(self.q, self.p)
        c1 = pow(p, ep, self.p)
        c2 = pow(p, eq, self.q) ^ fun
        h = (qinv * (c1 - c2)) % self.p
        c = c2 + h * self.q
        return c

    def TEST_CRT_decrypt(self, c, fun=0):
        dp = inverse(self.e, self.p - 1)
        dq = inverse(self.e, self.q - 1)
        qinv = inverse(self.q, self.p)
        m1 = pow(c, dp, self.p)
        m2 = pow(c, dq, self.q) ^ fun
        h = (qinv * (m1 - m2)) % self.p
        m = m2 + h * self.q
        return m


while True:
    random.seed(lb)
    lb2 = lb + st
    if lb2 == lb:
        lb2 = lb + 0.0000002
    lb = lb2
    r = RSA()
    p, x = gen_prime()
    q, y = gen_prime()
    r.generate(p, q)
    # print(lb)
    # print(p)
    # print(q)
    k = n2s(r.decrypt(int(
        "4FB8706DBE784D0299131BF9EBE010AE1A3B869DC327E6B78754967BFAB719FB927871DA49752D4BA2F67B278621C6882B189CE67671553CE48F08E604620171BF9E3AE53F8EB662B378889565F72666AFAD015B6781A9172F4C89F20234963DAA48A2F8AC7E234B9F5104B36ED3BAB324AC540F60E715B3D4BA93D9FD562E3E803FB996EA08ADAE7033E975024868E1CD5CEEBE450EA4D27447CCD7249922ED1B020CDBFC9902437FFE0468DE2779C9220602D3F6BD0584035813CE2D23E5E9DA795B748B4D3364C78876801265E81301D776A8A877F7D24845A610DEFA1A07BE38CB16A2C7AB814A268B5F847CD9B9D0AC2EBC32C539DA90A217F90659EAF9",
        16)))
    if "flag{" in k:
        print(lb)
        print(k)
        exit()
    print(lb)
