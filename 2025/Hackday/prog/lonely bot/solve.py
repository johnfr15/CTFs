import socket
import base64
import binascii

import hashlib

# Remote connection setup
remote_host = 'challenges.hackday.fr'
remote_port = 41525


def hash_answers(q, *answers):
    a1, a2, a3, a4 = answers
    joined_answers = "".join(map(str, answers)) 

    if "md5" in q: return hashlib.md5(joined_answers.encode()).hexdigest()
    if "sha256" in q: return  hashlib.sha256(joined_answers.encode()).hexdigest()
    if "sha1" in q: return  hashlib.sha1(joined_answers.encode()).hexdigest()


def find_encoding_base(encoded_str):
    # Try base64
    try:
        decoded_base64 = base64.b64decode(encoded_str)
        if decoded_base64.isascii():
            return 'base64'
    except Exception:
        pass

    # Try base32
    try:
        decoded_base32 = base64.b32decode(encoded_str)
        if decoded_base32.isascii():
            return 'base32'
    except Exception:
        pass

    # Try base16 (hexadecimal)
    try:
        decoded_base16 = bytes.fromhex(encoded_str)
        if decoded_base16.isascii():
            return 'base16'
    except ValueError:
        pass

    # Try rot13 (shifting letters by 13 places)
    try:
        decoded_rot13 = encoded_str.encode().decode('rot_13')
        if decoded_rot13.isascii():
            return 'rot13'
    except Exception:
        pass

    # Try binary (assumes 1s and 0s)
    try:
        decoded_bin = ''.join(chr(int(encoded_str[i:i+8], 2)) for i in range(0, len(encoded_str), 8))
        if decoded_bin.isascii():
            return 'binary'
    except ValueError:
        pass
    
    return 'unknown'




def main():
    # Create a socket object
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the remote host and port
    conn.connect((remote_host, remote_port))
    print(f"[+] Connected to {remote_host}:{remote_port}\n\n")


    # Receive the initial response from the server
    print(conn.recv(222).decode())
    conn.send(b"yes")

    print(conn.recv(1024).decode())
    conn.send(b"yes")

    print(conn.recv(1024).decode())
    print(conn.recv(1024).decode())



    res = conn.recv(1024).decode()
    print(res)
    temp = b"900" if "Celsius" in res else None
    temp = b"1700" if "Fahrenheit" in res else temp
    temp = b"1173" if "Kelvin" in res else temp
    conn.send(temp)     
    print(conn.recv(1024).decode())



    res = conn.recv(1024).decode()
    print(res)
    train = b"1984" if "magnetic" in res else None
    train = b"1912" if "diesel" in res else train
    train = b"1879" if "electric" in res else train
    train = b"1804" if "vapor" in res else train
    conn.send(train)     
    print(conn.recv(1024).decode())



    res = conn.recv(1024).decode()
    print(res)
    r = find_encoding_base(res)
    print(r)
    conn.send(r.encode())     
    print(conn.recv(1024).decode())



    res = conn.recv(1024).decode()
    print(res)
    h = hash_answers(res, b"", temp, train, r.encode())
    conn.send(bytes.fromhex(h))     
    print(conn.recv(1024).decode())
    print(conn.recv(1024).decode())
    print(conn.recv(1024).decode())


    conn.close()
    print("[+] Connection closed.")


if __name__ == "__main__":
    main()
