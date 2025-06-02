from crypto_implementations import *

def test_all_ciphers(text):
    print(f"\nTesting text: {text}\n")
    
    # Caesar Cipher
    print("\nCaesar Cipher:")
    for shift in range(1, 26):
        encrypted = caesar_cipher(text, shift)
        decrypted = caesar_cipher(encrypted, shift, 'decrypt')
        print(f"Shift {shift}: {encrypted} -> {decrypted}")
    
    # Vigenère Cipher
    print("\nVigenère Cipher:")
    keys = ["key", "planet", "apes", "cipher", "test"]
    for key in keys:
        encrypted = vigenere_cipher(text, key)
        decrypted = vigenere_cipher(encrypted, key, 'decrypt')
        print(f"Key '{key}': {encrypted} -> {decrypted}")
    
    # ROT13
    print("\nROT13:")
    encrypted = rot13(text)
    decrypted = rot13(encrypted)
    print(f"Encrypted: {encrypted} -> {decrypted}")
    
    # Atbash Cipher
    print("\nAtbash Cipher:")
    encrypted = atbash_cipher(text)
    decrypted = atbash_cipher(encrypted)
    print(f"Encrypted: {encrypted} -> {decrypted}")
    
    # A1Z26
    print("\nA1Z26:")
    encrypted = a1z26(text, 'encrypt')
    decrypted = a1z26(encrypted, 'decrypt')
    print(f"Encrypted: {encrypted} -> {decrypted}")
    
    # Bacon's Cipher
    print("\nBacon's Cipher:")
    encrypted = bacon_cipher(text, 'encrypt')
    decrypted = bacon_cipher(encrypted, 'decrypt')
    print(f"Encrypted: {encrypted} -> {decrypted}")
    
    # Morse Code
    print("\nMorse Code:")
    encrypted = morse_code(text, 'encrypt')
    decrypted = morse_code(encrypted, 'decrypt')
    print(f"Encrypted: {encrypted} -> {decrypted}")
    
    # Base64
    print("\nBase64:")
    encrypted = base64_encode(text)
    decrypted = base64_decode(encrypted)
    print(f"Encrypted: {encrypted} -> {decrypted}")
    
    # XOR Cipher
    print("\nXOR Cipher:")
    keys = ["key", "planet", "apes", "cipher", "test"]
    for key in keys:
        encrypted = xor_cipher(text, key)
        decrypted = xor_cipher(encrypted, key)
        print(f"Key '{key}': {encrypted} -> {decrypted}")
    
    # Affine Cipher
    print("\nAffine Cipher:")
    pairs = [(5, 8), (7, 13), (9, 11), (11, 15), (13, 17)]
    for a, b in pairs:
        encrypted = affine_cipher(text, a, b)
        decrypted = affine_cipher(encrypted, a, b, 'decrypt')
        print(f"Pair ({a}, {b}): {encrypted} -> {decrypted}")
    
    # Polybius Square
    print("\nPolybius Square:")
    encrypted = polybius_square(text, 'encrypt')
    decrypted = polybius_square(encrypted, 'decrypt')
    print(f"Encrypted: {encrypted} -> {decrypted}")

if __name__ == "__main__":
    test_text = "a1/.e1//14.1ed.f220e.1416e06/6dc"
    test_all_ciphers(test_text)
