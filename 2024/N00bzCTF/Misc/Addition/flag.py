from pwn import *

PORT = 42189
HOST = "24.199.110.35"

# Establish a connection to the remote host
try:
    c = remote(HOST, PORT, timeout=5)
    print("[+] Connected to the server")
except Exception as e:
    print(f"[-] Connection failed: {e}")
    exit()

try:
    # Try receiving the prompt; use recv() to capture any unexpected data
    prompt = c.recv(1024).decode().strip()  # Increase buffer size if necessary
    print("Received prompt:", prompt)  # Print the decoded prompt

    # Respond to the prompt
    answer1 = b"-1"  # Example response; adjust based on what the server expects
    c.sendline(answer1)  # Send the response

    # Receive and print any further data from the server
    response = c.recv(1024).decode().strip()  # Increase buffer size if necessary
    print("Received response:", response)

except EOFError:
    print("[-] The connection was closed by the server before receiving any data.")
except TimeoutError:
    print("[-] Timeout: No data received from the server.")
except Exception as e:
    print(f"[-] An error occurred: {e}")
finally:
    # Close the connection
    c.close()
