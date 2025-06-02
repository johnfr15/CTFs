# decode.py

# XOR value used in the encoding
XOR_VALUE = 3

# Read the encoded data
with open('output.txt', 'r') as file:
    encoded_data = file.read()

# Decode the data
decoded_bytes = [chr(ord(char) ^ XOR_VALUE) for char in encoded_data]
decoded_string = ''.join(decoded_bytes)

print(decoded_string)

