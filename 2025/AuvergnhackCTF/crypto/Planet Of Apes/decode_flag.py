def decode_flag(flag, shift=23):
    result = []
    # Keep ZIFT prefix unchanged
    result.append("ZIFT")
    
    # Process the rest of the string
    for char in flag[4:]:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # Calculate new character
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        elif char == '{':
            result.append('a')
        elif char == '}':
            result.append('c')
        elif char.isdigit():
            # Keep digits unchanged
            result.append(char)
        else:
            # Keep other special characters unchanged
            result.append(char)
    return ''.join(result)

# The flag we want to decode
flag = "ZITFa1/.e1//14.1ed.f220e.1416e06/6dc"

# Try different shifts
for shift in range(26):
    decoded = decode_flag(flag, shift)
    print(f"Shift {shift}: {decoded}")
