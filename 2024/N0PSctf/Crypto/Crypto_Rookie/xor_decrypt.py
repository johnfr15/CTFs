def xor_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        decrypted_char = chr(ord(char) ^ ord(key[i % key_length]))
        decrypted_text += decrypted_char
    return decrypted_text

ciphertext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
key = "ROOKIE"
decrypted_text = xor_decrypt(ciphertext, key)
print(decrypted_text)
