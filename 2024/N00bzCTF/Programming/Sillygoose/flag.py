import pwn

PORT = 41199
HOST = "24.199.110.35"


# Establish a connection to the remote host
try:
    c = pwn.remote(HOST, PORT, timeout=5)
    print("[+] Connected to the server")

    # Try receiving the prompt; use recv() to capture any unexpected data
    #prompt = c.recv(1024).decode().strip()  # Increase buffer size if necessary
    #print(prompt)  # Print the decoded prompt

except Exception as e:
    print(f"[-] Connection failed: {e}")
    exit()

TOO_LARGE = "your answer is too large you silly goose"
TOO_SMALL = "your answer is too small you silly goose"
START_FLAG = "n00bz{"


min = 0
max = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
n = "5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" # We start with the middle (max / 2)

while True:
    try:

        print(n)
        c.sendline(n)  # Send the response

        # Receive and print any further data from the server
        response = c.recv(1024).decode().strip()  # Increase buffer size if necessary
        print(response)

        if TOO_LARGE in response:
            mid = min + ((int(n) - min) // 2)
            max = int(n)
            n = str( mid )
        if TOO_SMALL in response:
            mid = int(n) + ((max - int(n)) // 2)
            min = int(n)
            n = str(mid)
        if START_FLAG in response:
            print(f"FLAG {response}")
            break

    except EOFError:
        print("[-] The connection was closed by the server before receiving any data.")
    except TimeoutError:
        print("[-] Timeout: No data received from the server.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    
c.close()
