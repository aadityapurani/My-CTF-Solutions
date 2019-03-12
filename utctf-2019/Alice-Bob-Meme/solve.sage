max_val = 84442469965344
M = 108453893951105886914206677306984937223705600011149354906282902016584483568647
# long weierstrass format
EE = EllipticCurve(GF(M),[0,829,0,512,0]) 
P = EE((88610873236405736097813831550942828314268128800347374801890968111325912062058, 76792255969188554519144464321650537182337412449605253325780015124365585152539))
# Q = Pn
Pn = EE((27543889954945113502256551007964501073506795938025836235838339960818915950890, 75922969573987021583641685217441284832467954055295272505357185824478295962572))
order = EE.order()
subresults = []
factors = []
modulus = 1
# Find partial solutions per each factor
for prime, exponent in factor(order):
        if prime > 10**9:
                break
        _factor = prime ** exponent
        factors.append(_factor)
        P2 = P*(order//_factor)
        Pn2 = Pn*(order//_factor)
        subresults.append(discrete_log_lambda(Pn2, P2, (0,_factor), '+'))
        modulus *= _factor

# Join partial solutions
n = crt(subresults,factors)
while n < max_val:
        if P*n==Pn:
                print("n=%d"%n)
                break
        n+=modulus
# 1213123123131
