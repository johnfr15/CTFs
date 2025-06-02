import random

# Define the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define the plaintext
plaintext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"

# Define the substitution key
def generate_key():
    key = list(alphabet)
    random.shuffle(key)
    return ''.join(key)

def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.upper() in alphabet:
            index = alphabet.index(char.upper())
            if char.isupper():
                encrypted_text += key[index].upper()
            else:
                encrypted_text += key[index].lower()
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.upper() in key:
            index = key.index(char.upper())
            if char.isupper():
                decrypted_text += alphabet[index].upper()
            else:
                decrypted_text += alphabet[index].lower()
        else:
            decrypted_text += char
    return decrypted_text

# Generate a random key
key = "ROOKIEROOKIEROOKIEROOKIEROOKIERO"
plaintext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
print("Generated Key:", key)

# Decrypt the ciphertext using the same key
decrypted_text = decrypt(plaintext, key)
print("Decrypted Text:", decrypted_text)
