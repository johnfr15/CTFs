# Given hex strings
CIPHERED = "2ae848a6f1644092de80a7b4b73f937f95f06bed576491e4c572daf2fe546ba11f740964e16b1ea10741010ae09bbef736c85280041e357d747ae6a22237d1ab636e78ba64521e00c1c802171a"
KEYSTREAM = "628d3ac98a5130a2eeebdeeb825ca70decaf0d816313a2809a11a88b8e635bfe2e197908d2062dcf3075363bd0f5cda803fb3ce45b2b5d4c024994977d53e1dc0d31018a11204135b1f96c2467"

# Convert hex to bytes
ciphered_bytes = bytes.fromhex(CIPHERED)
keystream_bytes = bytes.fromhex(KEYSTREAM)

# Ensure the lengths match
assert len(ciphered_bytes) == len(keystream_bytes), "CIPHERED and KEYSTREAM must be the same length."

# XOR operation
plaintext_bytes = bytearray(len(ciphered_bytes))
for i in range(len(ciphered_bytes)):
    plaintext_bytes[i] = ciphered_bytes[i] ^ keystream_bytes[i]

# Convert the result back to bytes
plaintext = bytes(plaintext_bytes)

# Print the resulting plaintext in hexadecimal format for easier inspection
print("Plaintext:", plaintext)
