import socket

def connect_to_server(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        s.connect((host, port))
        print(f"Connected to {host} on port {port}")

        response = s.recv(4096)
        print("Received:", response.decode())

        # Close the connection
        s.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    key = b'y\x9b\xbc,[:\xfa\xb1[\xe1q\xae\x01\x11\xac\x81\x18\xd0;'
    e_flag = bytes.fromhex("44cf14267a625939e57a098358c6bd1aefa8ec")
    flag = ''.join([ chr(e ^ k) for k, e in zip(key, e_flag)])
    print(flag)

    # print( ''.join([ ]))
