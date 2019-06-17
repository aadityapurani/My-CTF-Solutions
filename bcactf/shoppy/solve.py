import sys


def solver(inp):
    bro = inp.split(" ")
    got_b = 0
    got_c = 0
    got_d = 0
    cost = int(bro[-1])
    total_len = len(bro)
    for i in xrange(0, total_len-1):
        if bro[i] == 'A':
            cost = cost - 45
        elif bro[i] == 'B':
            if not got_b:
                cost = cost - 52
                got_b=1
            else:
                cost = cost - 46.8
                got_b=0
        elif bro[i] == 'C':
            if not got_c:
                cost = cost - 67
                got_c = 1
            else:    
                cost = cost - 33.5
                got_c = 0
        elif bro[i] == 'D':
            if got_d != 2:
                cost = cost - 75
                got_d += 1
            else:
                got_d = 0
                continue
    if cost < 0:
      return -1
    else:
      return cost

def round_up(x, place):
    return round(x + 5 * 10**(-1 * (place + 1)), place)

def main():
    ques = []
    for line in sys.stdin:
        if line != '' or line !='\n':
            ques.append(line.strip('\n'))
    ans = []
    for q in ques:
        if solver(q) == -1:
            ans.append(str(-1))
        else:
            ans.append(str(round_up(solver(q),2))[:-1])
    ans1=""
    for a in ans:
        ans1 += a
        ans1 +="\n"
    print ans1.rstrip("\n")

main()
