from math import isqrt
from random import randint

# Extended Euclidean Algorithm to find modular inverse
def mod_inverse(a, n):
    t, newt = 0, 1    
    r, newr = n, a    
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError("a is not invertible")
    if t < 0:
        t = t + n
    return t

# Baby-step Giant-step algorithm to solve a^x = b (mod n)
def baby_step_giant_step(a, b, n):
    m = isqrt(n) + 1
    # Baby steps
    baby_steps = {}
    value = 1
    print("\n\nm: ", m)
    for j in range(m):
        baby_steps[value] = j
        value = value * a % n

    # Giant steps
    inv_a_m = mod_inverse(pow(a, m, n), n)
    value = b
    for i in range(m):
        if value in baby_steps:
            return i * m + baby_steps[value]
        value = value * inv_a_m % n
    return None

if __name__ == '__main__':
    # Example usage
    c = 2887148238050771212671429597130393991977609459279722700926516024197432303799152733116328983144639225941977803110929349655578418949441740933805615113979999421542416933972905423711002751042080134966731755152859226962916775325475044445856101949404200039904432116776619949629539250452698719329070373564032273701278453899126120309244841494728976885406024976768122077071687938121709811322297802059565867

    # Assuming a and b are given
    a = randint(2, c - 1)
    k = randint(2, c - 1)
    b = pow(a, k, c)

    print(f"a = {a}\n, k = {k}\n, b = {b}\n, c = {c}\n")

    # Finding k
    k = baby_step_giant_step(a, b, c)
    print(f"Found k = {k}")
