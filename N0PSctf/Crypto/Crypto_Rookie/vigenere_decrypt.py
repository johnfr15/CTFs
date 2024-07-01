def vigenere_decrypt(ciphertext, key, offset):
    plaintext = ''
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Shift the character backwards using the key
            shift = ord(key[key_index % key_length])
            decrypted_char = chr(((ord(char) - ord('A') + shift + offset) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            # If the character is not a letter, keep it unchanged
            plaintext += char
    
    return plaintext

ciphertext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
key = "ROOKIE"

for offset in range(0, 26):
    plaintext = vigenere_decrypt(ciphertext, key, offset)
    print("offset:", offset, "=>", plaintext)
