def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            decrypted_char = (a * ((ord(char)-ord('A'))) + b) % 26
            decrypted_text += chr(decrypted_char + ord('A'))
        else:
            decrypted_text += char

    return decrypted_text

def brute_force_affine(ciphertext):
    for a in range(1, 26):
        for b in range(1, 26):
            decrypted_text = affine_decrypt(ciphertext, a, b)
            print(f"(a={a}, b={b}): {decrypted_text}")

ciphertext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
brute_force_affine(ciphertext)
