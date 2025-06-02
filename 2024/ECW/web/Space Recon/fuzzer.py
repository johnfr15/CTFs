import requests
import random
import urllib.parse
import string

# Constants
HOST = "challenges.challenge-ecw.eu"
PORT = "38693"
ENDPOINT = "/api/search"
LENGTH = 10  # Length of the random string

def fuzz_random():
    # Define the character set for random generation
    char_set = string.ascii_letters + string.digits + string.punctuation

    while True:  # Infinite fuzzing loop
        # Generate a random string of the specified length
        random_string = ''.join(random.choices(char_set, k=LENGTH))
        value = random_string  # Append random string to the query parameter
        
        # URL-encode the value
        encoded_value = urllib.parse.quote(value)
        
        # Send request to the endpoint with the fuzzed, URL-encoded value
        try:
            url = f"http://{HOST}:{PORT}{ENDPOINT}?q={encoded_value}"
            response = requests.get(url)
            
            # Print the response status and content (limit output for readability)
            print(f"Value: {repr(value)} - Response: {response.status_code}, {response.text[:100]}...")
        except requests.RequestException as e:
            print(f"Error with value '{repr(value)}': {str(e)}")

if __name__ == "__main__":
    fuzz_random()
