import random as rd
import math

e_message = "-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

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
        x = charset.index(char)
        x = (a_inv * (x - b)) % n
        decrypted += charset[int(x)]

    return decrypted

n = len(charset)

for i in range(10000):
    a = rd.randint(2,n-1)
    b = rd.randint(1,n-1)

    d_message = decrypt(e_message,a,b,n)
    if ( d_message.startswith('404') ):
        print( d_message )
 
# DECRYPTED FLAG : -4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_
