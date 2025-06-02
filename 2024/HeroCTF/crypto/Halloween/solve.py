from pwn import *
import string

# Connection details
HOST = "crypto.heroctf.fr"
PORT = 9001

# Connect to the challenge
conn = remote(HOST, PORT)

# Retrieve the encrypted flag output from the initial print statement
conn.recvuntil(b"sp00")
encrypted_flag = conn.recvuntil(b"00ky").strip(b"00ky").decode()

print("\nEncrypted flag\n", encrypted_flag)

# Retrieve the initial Halloween message
_ = conn.recvuntil(b"!\n").decode('utf-8')

# Initialize an empty byte array for the plaintext flag
flag_length = int(len(encrypted_flag) / 2)
recovered_flag = ""

i = 0
while True:
    # Send 77 "0x00" bytes (as hex) to the server
    conn.sendline("00" * 77)  # Creates a string of "00" repeated 77 times
    response = conn.recvline().strip().decode()

    # Check if the encrypted response matches the corresponding byte in the flag
    print(f"{i}: {response[:154]}")  # Display the first 154 hex characters (77 bytes in hex is 154 characters)
    i += 77

# Close the connection
conn.close()

# Display the recovered flag
print("Recovered flag:", recovered_flag.decode('utf-8'))
