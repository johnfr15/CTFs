import socket
import time
from randcrack import RandCrack

rc = RandCrack()


def get_secret(s, host, port):
    # 1 Connect to the server
    s.connect((host, port))
    s.recv(4096)

    # 2 answer the question
    s.sendall(b"2\n")

    # Receive the response from the server
    response = s.recv(4096)
    secret = response.decode().split(" ")[-1]
    return secret

def send_secret(s, host, port, predict):
    # 1 Connect to the server
    s.connect((host, port))
    s.recv(4096)

    # 2 answer the question
    s.sendall(b"1\n")
    s.recv(4096)

    # 3 send secret
    s.sendall(predict)

    # Receive the response from the server
    response = s.recv(4096)
    print(response)
    return response.decode().split(" ")[-1]

def train_rand(buffer):
    return
    
def connect_to_server(host, port):
    count = 2496 # need to train on that amount of byte
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        flag = send_secret(s, host, port, b"Hello world\n")

        print(flag)

        # Close the connection
        s.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Connect to the given server and port
    connect_to_server('0.cloud.chals.io', 33731)
