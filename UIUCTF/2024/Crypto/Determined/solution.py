from Crypto.Util.number import inverse, long_to_bytes
from server import main
import ssl
import socket

URL = "determined.chal.uiuc.tf"
PORT = 1337

# This function will attempt to exctract the "q" value hardcoded in the matrix of the server
#
def get_q():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Wrap the socket with SSL
    context = ssl.create_default_context()
    ssl_socket = context.wrap_socket(client_socket, server_hostname=URL)

    try:
        # Connect to the server
        ssl_socket.connect((URL, PORT))
        print(f"Connected to server {URL} on port {PORT}\n")

        # Loop over all the values asked by the server (see function "inputs" in server.py )
        inputs = ['0','1','0','1','0','1','0','1','0']
        for input in inputs:
            response = ssl_socket.recv(4096)
            answer = input + "\n"
            ssl_socket.sendall(answer.encode())

        # Get back the determinent of the matrix
        response = ssl_socket.recv(4096).decode()
        q = int(response.split(" ")[-1])

        return q

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    # Given values
    n = 158794636700752922781275926476194117856757725604680390949164778150869764326023702391967976086363365534718230514141547968577753309521188288428236024251993839560087229636799779157903650823700424848036276986652311165197569877428810358366358203174595667453056843209344115949077094799081260298678936223331932826351
    e = 65535
    c = 72186625991702159773441286864850566837138114624570350089877959520356759693054091827950124758916323653021925443200239303328819702117245200182521971965172749321771266746783797202515535351816124885833031875091162736190721470393029924557370228547165074694258453101355875242872797209141366404264775972151904835111

    # local: You can simulate the server side if official is down
    # q = main()
    # official server
    q = get_q()
    p = n // q

    # Compute ϕ(n)
    phi_n = (p - 1) * (q - 1)

    # Compute the private exponent d (AKA private key)
    # modular multiplicative inverse of 𝑒 modulo 𝜙(𝑛)
    d = inverse(e, phi_n)

    # Decrypt the ciphertext
    m = pow(c, d, n)

    # Convert m back to bytes to recover the FLAG
    flag = long_to_bytes(m)
    print(''.join([ chr(c) for c in flag ]))