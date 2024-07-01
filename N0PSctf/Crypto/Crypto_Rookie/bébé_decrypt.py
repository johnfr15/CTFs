import random as rd
import math

e_message = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def modular_inverse(a, n):
    # Extended Euclidean Algorithm
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("a is not invertible")
    if t < 0:
        t = t + n
    return t


def decrypt(message,a,b,n):
    decrypted = ""
    a_inv = (n - a) % n

    for char in message:
        if char.isalpha():
            x = charset.index(char)
            x = (a_inv * (x - b)) % n
            decrypted += charset[int(x)]
        else:
            decrypted += ' '

    return decrypted

n = len(charset)

for a in range(2,26):
    for b in range(1, 26):
        d_message = decrypt(e_message,a,b,n)
        print( "a:", a, "b: ", b, d_message )
 
# DECRYPTED FLAG : STSABEAOE OEIEALGSETRHNCOI MMFITTAK






