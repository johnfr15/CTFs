def caesar_cipher(text, shift):
    decrypted = ''
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            decrypted += shifted.upper() if char.isupper() else shifted
        else:
            decrypted += char
    return decrypted

original_text = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"  # The text decrypted with key (a=1, b=0)

for b in range(26):
    key = (1 + 2 * b, 0)
    decrypted_text = caesar_cipher(original_text, b)
    print(f"Decryption with key {key}: {decrypted_text}")
