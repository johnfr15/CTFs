def atbash_decrypt(ciphertext):
    def decrypt_char(c):
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            decrypted_char = chr(90 - (ord(c) - offset)) if c.isupper() else chr(122 - (ord(c) - offset))
            return decrypted_char
        else:
            return c

    decrypted_text = ''.join(decrypt_char(char) for char in ciphertext)
    return decrypted_text

def brute_force_atbash(ciphertext):
    for char_code in range(65, 65 + 26):
        char = chr(char_code)
        decrypted_text = atbash_decrypt(ciphertext)
        print(f"Substitution for '{char}': {decrypted_text}")

ciphertext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
brute_force_atbash(ciphertext)
