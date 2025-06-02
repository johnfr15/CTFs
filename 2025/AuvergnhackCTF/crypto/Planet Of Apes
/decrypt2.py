def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # Calculate new character
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            # Shift non-alphabetic characters
            if ord(char) >= 32:  # Only shift printable characters
                new_char = chr((ord(char) - 32 - shift) % 95 + 32)  # 95 = number of printable ASCII chars
                result.append(new_char)
            else:
                result.append(char)
    return ''.join(result)

# Read the encrypted text
with open('poa7.txt', 'r') as f:
    encrypted_text = f.read()

# Try different shifts
for shift in range(26):
    decrypted = caesar_decrypt(encrypted_text, shift)
    print(f"Shift {shift}:")
    print(decrypted[:200])  # Show first 200 characters
    print("---")
