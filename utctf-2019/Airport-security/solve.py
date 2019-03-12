from pwn import *
import math
import cmath

# Credits to my colleague for the automation.

r = remote("quantumbomb.live", 1337)

def apply_gate(a1, a2, b1, b2):
    r.readuntil("Measure and decide\n")[:-1]
    r.writeline("1")
    print r.readuntil("4, .4j\n")[:-1]
    r.writeline(",".join([str(a1),str(b1),str(a2),str(b2)]))
    print r.readline()[:-1]


def apply_rotation(div):
    angle = math.pi/(2*div)
    a1 = math.cos(angle)
    b1 = -math.sin(angle)*1j
    a2 = -math.sin(angle)*1j
    b2 = math.cos(angle)
    apply_gate(a1, a2, b1, b2)

def apply_initial(c1, c2):
    a1 = 1 / c1
    b1 = 0
    a2 = 0
    b2 = 0 / c2
    apply_gate(a1, a2, b1, b2)

for i in range(1, 36):
    r.readline()[:-1]
    print r.readuntil("This is bomb "+str(i)+"\n")[:-1]
    qubit_line = r.readline()[:-1]
    splt = qubit_line.split(': ')[1].split(' + ')

    # angle = 22.5/365 * 2 * math.pi

    n1 = eval(splt[0][:-4])
    n2 = eval(splt[1][:-4])
    print qubit_line
    apply_initial(n1, n2)
    trial = 32
    for rrr in range(1,trial):
        apply_rotation(trial)
    print r.readuntil("Measure and decide\n")[:-1]
    r.writeline("2")
    ss = r.readline()[:-1]
    print r.readline()[:-1]
    print ss
    if "[[1.]] |0>" in ss:
        print "y"
        r.writeline("y")
    else:
        print "n"
        r.writeline("n")

r.interactive()
