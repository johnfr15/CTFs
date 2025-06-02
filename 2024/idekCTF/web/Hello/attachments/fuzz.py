import requests
import itertools
import urllib.parse

# Define the base URL
base_url = "http://localhost:1337?name="

# Define the range of values to test (0 to 255 for each byte)
byte_range = range(126)

# Loop through all possible 6-byte combinations
for combination in itertools.product(byte_range, repeat=2):
    # Convert each combination to bytes
    byte_value = bytes(combination[::-1])
    
    # URL-encode the byte sequence
    name_value = urllib.parse.quote(byte_value)

    # Construct the full URL
    url = base_url + name_value

    try:
        # Send the GET request
        response = requests.get(url)
        
        if len(response.text) != len("Hello, 12"):
          print("Somethin strange hapenned")
          print(f'name_value: {name_value}')
          print(f'Response Text: {response.text}')
          print("\n")

    except Exception as e:
        print(f'Error with URL: {url}')
        print(f'Exception: {e}')
