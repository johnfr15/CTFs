import pwn
import threading

PORT = 10502
HOST = "challs.n00bzunit3d.xyz"

s = '4761058239'

def connect_and_flag(s: str) -> str:

    # Establish a connection to the remote host
    c = pwn.remote(HOST, PORT, timeout=5)
    print("[+] Connected to the server")

    c.sendline(s + '\n')

    # Receive and print any further data from the server
    response = c.recv(1024).decode().strip()  # Increase buffer size if necessary
    response2 = c.recv(1024).decode().strip()  # Increase buffer size if necessary

    return response2

def connect_and_interact() -> str:

    # Establish a connection to the remote host
    c = pwn.remote(HOST, PORT, timeout=5)
    print("[+] Connected to the server")

    c.sendline(s + '\n')

    # Receive and print any further data from the server
    response = c.recv(1024).decode().strip()  # Increase buffer size if necessary
    return response



res = connect_and_interact()

print("\n\n\nres: ", res, '\n\n\n')

s2 = ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(s)):
    s2[int(res[i])] = chr(i)
s2 = ''.join(s2)

print("\n\n\ns2: ", s2, '\n\n\n')

flag = connect_and_flag("".join(s2))

print(flag)