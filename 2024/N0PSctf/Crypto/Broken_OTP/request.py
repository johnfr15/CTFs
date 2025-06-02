import subprocess
import time

def send_command(command, host, port):
    try:
        # Start the sc command with subprocess
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
        process.stdin.write(command + "\n")
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

        print(f"Received response:\n{response}")

        # Close the process
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.terminate()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = "nopsctf-broken-otp.chals.io"
    port = "443"
    command = "2"  # The command you want to send

    send_command(command, host, port)
