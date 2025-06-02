import socket
import ssl

hostname = 'nopsctf-outsiders.chals.io'  # Replace with your target hostname
port = 443
context = ssl.create_default_context()

# Connect to the server
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        # Properly formatted HTTP GET request
        request = (
            "GET / HTTP/1.1\r\n"
            "Host: {}\r\n"
            "Connection: close\r\n"  # Ensure the connection is closed after the response
            "\r\n"
        ).format(hostname)
        ssock.send(request.encode())

        # Receive the response
        response = b''
        while True:
            data = ssock.recv(4096)
            if not data:
                break
            response += data
        
        # Print the response
        print(response.decode())

