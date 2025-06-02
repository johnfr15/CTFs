def shift_right(text, shift=26):
    result = []
    for char in text:
        if char.isalpha():
            # Get ASCII value and add shift
            ascii_val = ord(char) + shift
            
            # Keep the character within the ASCII range
            if char.isupper():
                # For uppercase letters (A-Z)
                if ascii_val > ord('Z'):
                    ascii_val = ((ascii_val - ord('A')) % 26) + ord('A')
            else:
                # For lowercase letters (a-z)
                if ascii_val > ord('z'):
                    ascii_val = ((ascii_val - ord('a')) % 26) + ord('a')
            
            new_char = chr(ascii_val)
            result.append(new_char)
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    return ''.join(result)

# Read input text
input_text = """a1/.e1//14.1ed.f220e.1416e06/6dc"""

# # Shift the text
# shifted_text = shift_right(input_text)

# # Print the result
# print("Shifted Text:")
# print(shifted_text)


for c in input_text:
    print(f"{chr(ord(c) + 26)}", end="")