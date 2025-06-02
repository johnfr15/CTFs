def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char == ' ':
            # Keep spaces unchanged
            result.append(char)
        elif char.isalpha():
            # Handle uppercase and lowercase letters separately
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # Calculate new character
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            # Shift non-alphabetic characters (except space)
            new_char = chr((ord(char) - shift) % 128)  # Shift within ASCII range
            result.append(new_char)
    return ''.join(result)

# Read the encrypted text
with open('poa7.txt', 'r') as f:
    encrypted_text = f.read()

# Decrypt with shift 23
shift = 23
print("Decrypted text with shift 23:")
print(caesar_decrypt(encrypted_text, shift))
