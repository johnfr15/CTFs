def decode_custom(text):
    result = []
    for char in text:
        ascii_val = ord(char)
        
        if ascii_val >= 72 and ascii_val <= 74:  # H-J for /, -, +
            if ascii_val == 72:  # H
                result.append('-')
            elif ascii_val == 73:  # I
                result.append('/')
            elif ascii_val == 74:  # J
                result.append('+')
        elif ascii_val >= 75 and ascii_val <= 84:  # K-T for 0-9
            result.append(chr(ascii_val - 26))  # Subtract 26 to get back to 0-9 range
        elif ascii_val >= 95 and ascii_val <= 95:  # _ for .
            result.append('.')
        elif ascii_val >= 123 and ascii_val <= 128:  # {,|,},~,, for a-f
            result.append(chr(ascii_val - 26))  # Subtract 26 to get back to a-f range
        else:
            result.append(char)  # Keep other characters unchanged
    return ''.join(result)

# The encoded text
encoded_text = "{KIHKIIKNHK~HLLJHKNKPJPIP~}"

# Decode it
decoded_text = decode_custom(encoded_text)
print("Decoded Text:")
print(decoded_text)
