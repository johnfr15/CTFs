from random import randint
from math import gcd
from Crypto.Util.number import *
from sage.all import *

k = 261476204452329860198550276341831436116033346106686
p,q,r = (6*k + 1), (12*k + 1), (18*k + 1)
c = p*q*r
phi = (p-1)*(q-1)*(r-1)

def generate_challenge(c):
    a = randint(2, c - 1)
    while gcd(a, c) != 1:
        a = randint(2, c - 1)
    k = randint(2, c - 1)
    return (a, pow(a, k, c), k)

a, b, k = generate_challenge(c)

def solve_dlog(a,b,c,phi):
    mods, rems = [], []
    for p,e in list(factor(phi)):
        pe = p**e
        aa = pow(a, phi//pe, c)
        bb = pow(b, phi//pe, c)
        assert pow(aa, pe, c) == 1
        rem = discrete_log(Zmod(c)(bb), Zmod(c)(aa), ord=pe)
        mods.append(pe)
        rems.append(rem)
        print(f'{rem} % {pe}')
    return crt(rems, mods)

res = solve_dlog(a,b,c,phi)
print()
print(res)
print(k)