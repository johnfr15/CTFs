from pwn import *
import sympy
import re

def cubic_roots_from_sums(s1, s2, s3):
    sigma2 = (s1**2 - s2)//2
    sigma3 = (s3 - (s1**3 - 3*s1*sigma2))//3
    t = sympy.symbols('t')
    roots = sympy.solve(t**3 - s1*t**2 + sigma2*t - sigma3, t)
    roots = [int(r) for r in roots]
    roots.sort()
    return roots

def main():
    r = remote('challenges.404ctf.fr', 30069)

    r.recvuntil(b'?')
    r.sendline(b'john')
    for _ in range(100):
        s1 = int(re.search(rb'= ([0-9]+)', r.recvline()).group(1))
        s2 = int(re.search(rb'= ([0-9]+)', r.recvline()).group(1))
        s3 = int(re.search(rb'= ([0-9]+)', r.recvline()).group(1))
        print(r.recvuntil(b'?'))

        nx, ny, nz = cubic_roots_from_sums(s1, s2, s3)

        r.send_raw(f"{nx},{ny},{nz}".encode() + b'\n')

    print(r.recvline())
    print(r.recvline())

if __name__ == "__main__":
    main()
