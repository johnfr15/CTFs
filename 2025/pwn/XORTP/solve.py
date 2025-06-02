from pwn import *

# context.log_level = 'debug'

payload = cyclic(300)

p = process('./xortp')

recv = p.recvline()
print(recv)

p.sendline(payload)

recv = p.recvline()

print(recv)