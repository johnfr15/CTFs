from math import gcd, isqrt
import random

def generate_challenge(c):
    random.seed()
    a = random.randint(2, c - 1)
    while gcd(a, c) != 1:
        a = random.randint(2, c - 1)
    k = random.randint(2, c - 1)
    return (a, pow(a, k, c), k)

def mod_inverse(a, c):
    """ Compute the modular inverse of a modulo c using Extended Euclidean Algorithm """
    t, newt = 0, 1
    r, newr = c, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError("a is not invertible")
    if t < 0:
        t = t + c
    return t

def discrete_log(a, b, c):
    """ Find the discrete logarithm k such that a^k ≡ b (mod c) using Baby-step Giant-step algorithm """
    m = isqrt(c) + 1

    # Baby steps
    baby_steps = {}
    value = 1
    for j in range(m):
        if value not in baby_steps:
            baby_steps[value] = j
        value = (value * a) % c

    # Giant steps
    a_inv_m = pow(mod_inverse(a, c), m, c)
    value = b
    for i in range(m):
        if value in baby_steps:
            return i * m + baby_steps[value]
        value = (value * a_inv_m) % c

    return None

if __name__ == '__main__':
    C = 561
    (a, b, k) = generate_challenge(C)

    print("a: ", a)
    print("b: ", b)
    print("k (generated): ", k)

    k_found = discrete_log(a, b, C)
    print(pow(a, k, C))
    print("k (found): ", k_found)
