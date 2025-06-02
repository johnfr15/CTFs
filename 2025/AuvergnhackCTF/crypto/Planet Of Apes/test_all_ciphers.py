from crypto_implementations import *

FLAG = "a1/.e1//14.1ed.f220e.1416e06/6dc"

print("\nTesting all ciphers with flag:", FLAG)

# Caesar Cipher
print("\nCaesar Cipher:")
for shift in range(26):
    encrypted = caesar_cipher(FLAG, shift)
    decrypted = caesar_cipher(encrypted, shift, 'decrypt')
    print(f"Shift {shift}: {encrypted} -> {decrypted}")

# Vigenère Cipher
print("\nVigenère Cipher:")
keys = ["key", "planet", "apes", "cipher", "test", "movie", "space", "time"]
for key in keys:
    encrypted = vigenere_cipher(FLAG, key)
    decrypted = vigenere_cipher(encrypted, key, 'decrypt')
    print(f"Key '{key}': {encrypted} -> {decrypted}")

# ROT13
print("\nROT13:")
encrypted = rot13(FLAG)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {rot13(encrypted)}")

# Atbash Cipher
print("\nAtbash Cipher:")
encrypted = atbash_cipher(FLAG)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {atbash_cipher(encrypted)}")

# A1Z26
print("\nA1Z26:")
encrypted = a1z26(FLAG, 'encrypt')
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {a1z26(encrypted, 'decrypt')}")

# Bacon's Cipher
print("\nBacon's Cipher:")
encrypted = bacon_cipher(FLAG, 'encrypt')
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {bacon_cipher(encrypted, 'decrypt')}")

# Morse Code
print("\nMorse Code:")
encrypted = morse_code(FLAG, 'encrypt')
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {morse_code(encrypted, 'decrypt')}")

# Base64
print("\nBase64:")
encrypted = base64_encode(FLAG)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {base64_decode(encrypted)}")

# XOR Cipher
print("\nXOR Cipher:")
keys = ["key", "planet", "apes", "cipher", "test", "movie", "space", "time"]
for key in keys:
    encrypted = xor_cipher(FLAG, key)
    print(f"Key '{key}': {encrypted}")
    print(f"Decrypted: {xor_cipher(encrypted, key)}")

# Affine Cipher
print("\nAffine Cipher:")
pairs = [(5, 8), (7, 13), (9, 11), (11, 15), (13, 17), (15, 19), (17, 21), (19, 23)]
for a, b in pairs:
    encrypted = affine_cipher(FLAG, a, b)
    print(f"Pair ({a}, {b}): {encrypted}")
    print(f"Decrypted: {affine_cipher(encrypted, a, b, 'decrypt')}")

# Polybius Square
print("\nPolybius Square:")
encrypted = polybius_square(FLAG, 'encrypt')
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {polybius_square(encrypted, 'decrypt')}")
