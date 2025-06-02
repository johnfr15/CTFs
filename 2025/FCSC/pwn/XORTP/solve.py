from pwn import *

# context.log_level = 'debug'

p = process('./xortp')


recv = p.recvuntil(b'Which file would like to encrypt?')
print(recv)

pause()
