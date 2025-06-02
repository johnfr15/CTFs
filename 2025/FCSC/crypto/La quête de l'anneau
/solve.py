from Crypto.Util.number import *
import json
from math import gcd
from functools import reduce

def compute_s(data):
    diffs = []
    for d in data:
        m = d["m"]
        iv = d["iv"]
        c = d["c"]
        diff = m * iv - c
        diffs.append(diff)
    
    # compute GCD of all differences
    s = reduce(gcd, diffs)
    return s

def decrypt(ciphertext, s):
    size = s.bit_length()
    bs = size // 8
    result = b""
    for d in ciphertext:
        iv = d["iv"]
        c = d["c"]
        m = c * pow(iv, -1, s) % s
        result += long_to_bytes(m, bs)
    return result

if __name__ == "__main__":
    with open("output.txt", "r") as f:
        data = json.load(f)

    s = compute_s(data["data"])
    print(f"[+] Recovered modulus s:\n{s}\n")

    flag = decrypt(data["C"], s)
    print(f"[🎉] Flag: {flag.decode()}")
