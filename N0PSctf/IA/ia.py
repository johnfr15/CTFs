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

def send_secret(plaintext, host):
    try:
        # 1.
        # Start the sc command with subprocess
        # Establish connection with the server
        process = subprocess.Popen(
            ["sc", f"{host}"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Read the initial welcome message
        welcome_message = process.stdout.readline()
        print(f"Received welcome message:\n{welcome_message}")

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





if __name__ == "__main__":
    host = "sc nopsctf-ask-for-it.chals.io"
    # Connect to the server and save ciphertexts to file
    secret = send_secret("Hello, world", host)


