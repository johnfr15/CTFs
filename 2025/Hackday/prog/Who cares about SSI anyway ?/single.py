from pwn import *
import time
import string

# context.log_level = 'debug'

# Remote connection setup
remote_host = 'challenges.hackday.fr'
remote_port = 48118

choice = bytearray(b"abcdefghijklmnopqrstuvwxyz" +  # Lowercase
               b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" +  # Uppercase
               b"_" +                          # Underscore
               string.punctuation.encode()) 

def main():
    FLAG = bytearray(b"")
    # Establish connection
    conn = remote(remote_host, remote_port)
    print(f"[+] Connected to {remote_host}:{remote_port}\n\n")
    response = conn.recvline(timeout=1).decode()

    while len(FLAG) < 21:
        FLAG += b"\x00"
        
        # i = 0
        # average = 1
        # deltares = []
        # while True:
        #     FLAG[-1] = choice[i % len(choice)]
        #     print("Testing", chr(FLAG[-1]))

    b = time.time()
    conn.sendline(b"HAC" + b"A"*18)
    response = conn.recvline().decode()
    a = time.time()
    delta = a - b
    print("Delta", delta)
            # deltares.append(delta)

            # average = sum(deltares) / (i+1)
            # print(f"Average: {average}")
            # if  i > 5 and delta > average * 1.2:
            #     print(f"Average: {average}")
            #     print(f"Found: {FLAG}")
            #     break
            # i += 1

    print("\n\n")
    conn.close()


if __name__ == "__main__":
    main()
