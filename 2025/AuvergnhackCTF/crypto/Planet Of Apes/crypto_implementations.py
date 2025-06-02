def caesar_cipher(text, shift, mode='encrypt'):
    """Caesar cipher implementation"""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:  # decrypt
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def vigenere_cipher(text, key, mode='encrypt'):
    """Vigenère cipher implementation"""
    result = []
    key_index = 0
    key = key.upper()
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'encrypt':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def substitution_cipher(text, key, mode='encrypt'):
    """Simple substitution cipher implementation"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    result = []
    for char in text.lower():
        if char.isalpha():
            if mode == 'encrypt':
                index = alphabet.index(char)
                new_char = key[index]
            else:
                index = key.index(char)
                new_char = alphabet[index]
            result.append(new_char.upper() if char.isupper() else new_char)
        else:
            result.append(char)
    return ''.join(result)

def rail_fence_cipher(text, rails, mode='encrypt'):
    """Rail Fence cipher implementation"""
    fence = [['\n' for col in range(len(text))] for row in range(rails)]
    rail = 0
    direction = False
    result = []
    
    # Create the fence
    for char in text:
        fence[rail].append(char)
        if rail == 0 or rail == rails - 1:
            direction = not direction
        rail += 1 if direction else -1
    
    # Read the fence
    for rail in fence:
        result.extend([char for char in rail if char != '\n'])
    
    if mode == 'decrypt':
        # For decryption, we need to reconstruct the fence
        rail = 0
        direction = False
        index = 0
        fence = [['\n' for col in range(len(text))] for row in range(rails)]
        
        # Mark positions
        for char in text:
            fence[rail][index] = '*'
            if rail == 0 or rail == rails - 1:
                direction = not direction
            rail += 1 if direction else -1
            index += 1
        
        # Place characters
        rail = 0
        direction = False
        index = 0
        for char in text:
            while fence[rail][index] != '*':
                index += 1
            fence[rail][index] = char
            if rail == 0 or rail == rails - 1:
                direction = not direction
            rail += 1 if direction else -1
            index += 1
        
        # Read diagonally
        rail = 0
        direction = False
        index = 0
        result = []
        for char in text:
            result.append(fence[rail][index])
            if rail == 0 or rail == rails - 1:
                direction = not direction
            rail += 1 if direction else -1
            index += 1
        
        return ''.join(result)
    
    return ''.join(result)

def rot13(text):
    """ROT13 cipher implementation"""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + 13) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def atbash_cipher(text):
    """Atbash cipher implementation"""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr(base + (25 - (ord(char) - base)))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def a1z26(text, mode='encrypt'):
    """A1Z26 cipher implementation"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    
    if mode == 'encrypt':
        for char in text.lower():
            if char.isalpha():
                index = alphabet.index(char) + 1
                result.append(str(index))
            else:
                result.append(char)
    else:  # decrypt
        current_num = ''
        for char in text:
            if char.isdigit():
                current_num += char
            else:
                if current_num:
                    try:
                        index = int(current_num) - 1
                        if 0 <= index < 26:
                            result.append(alphabet[index])
                        current_num = ''
                    except ValueError:
                        current_num = ''
                        result.append(char)
                result.append(char)
        if current_num:
            try:
                index = int(current_num) - 1
                if 0 <= index < 26:
                    result.append(alphabet[index])
            except ValueError:
                pass
    
    return ''.join(result)

def bacon_cipher(text, mode='encrypt'):
    """Bacon's cipher implementation"""
    bacon_dict = {
        'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb',
        'e': 'aabaa', 'f': 'aabab', 'g': 'aabba', 'h': 'aabbb',
        'i': 'abaaa', 'j': 'abaab', 'k': 'ababa', 'l': 'ababb',
        'm': 'abbaa', 'n': 'abbab', 'o': 'abbba', 'p': 'abbbb',
        'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
        'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb',
        'y': 'bbaaa', 'z': 'bbaab'
    }
    
    result = []
    if mode == 'encrypt':
        for char in text.lower():
            if char.isalpha():
                result.append(bacon_dict[char])
            else:
                result.append(char)
    else:  # decrypt
        current_code = ''
        for char in text:
            if char in 'ab':
                current_code += char
                if len(current_code) == 5:
                    for letter, code in bacon_dict.items():
                        if code == current_code:
                            result.append(letter)
                            current_code = ''
                            break
            else:
                if current_code:
                    for letter, code in bacon_dict.items():
                        if code == current_code:
                            result.append(letter)
                            break
                    current_code = ''
                result.append(char)
        if current_code:
            for letter, code in bacon_dict.items():
                if code == current_code:
                    result.append(letter)
                    break
    
    return ''.join(result)

def morse_code(text, mode='encrypt'):
    """Morse code implementation"""
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
        'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----'
    }
    
    result = []
    if mode == 'encrypt':
        for char in text.lower():
            if char.isalpha() or char.isdigit():
                result.append(morse_dict[char])
            else:
                result.append(char)
    else:  # decrypt
        morse_to_letter = {v: k for k, v in morse_dict.items()}
        current_code = ''
        for char in text:
            if char in '.-':
                current_code += char
            else:
                if current_code:
                    result.append(morse_to_letter.get(current_code, current_code))
                    current_code = ''
                result.append(char)
        if current_code:
            result.append(morse_to_letter.get(current_code, current_code))
    
    return ''.join(result)

def base64_encode(text):
    """Base64 encoding implementation"""
    import base64
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    """Base64 decoding implementation"""
    import base64
    return base64.b64decode(text).decode()

def xor_cipher(text, key):
    """XOR cipher implementation"""
    result = []
    key_index = 0
    for char in text:
        xor_result = ord(char) ^ ord(key[key_index % len(key)])
        result.append(chr(xor_result))
        key_index += 1
    return ''.join(result)

def affine_cipher(text, a, b, mode='encrypt'):
    """Affine cipher implementation"""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                new_char = chr(((a * (ord(char) - base) + b) % 26) + base)
            else:  # decrypt
                new_char = chr(((a * (ord(char) - base) - b) % 26) + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def polybius_square(text, mode='encrypt'):
    """Polybius Square cipher implementation"""
    square = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    result = []
    
    if mode == 'encrypt':
        for char in text.upper():
            if char.isalpha():
                if char == 'J':
                    char = 'I'
                for i in range(5):
                    for j in range(5):
                        if square[i][j] == char:
                            result.append(f"{i+1}{j+1}")
                            break
    else:  # decrypt
        current_num = ''
        for char in text:
            if char.isdigit():
                current_num += char
                if len(current_num) == 2:
                    row = int(current_num[0]) - 1
                    col = int(current_num[1]) - 1
                    result.append(square[row][col])
                    current_num = ''
            else:
                if current_num:
                    row = int(current_num[0]) - 1
                    col = int(current_num[1]) - 1
                    result.append(square[row][col])
                    current_num = ''
                result.append(char)
        if current_num:
            row = int(current_num[0]) - 1
            col = int(current_num[1]) - 1
            result.append(square[row][col])
    
    return ''.join(result)

FLAG = "a1/.e1//14.1ed.f220e.1416e06/6dc"

for i in range(26):
    print(f"{i}: {caesar_cipher(FLAG, i, 'encrypt')}")



"""
# Example usage:
if __name__ == "__main__":
    # Caesar cipher example
    text = "hello world"
    encrypted = caesar_cipher(text, 3, 'encrypt')
    decrypted = caesar_cipher(encrypted, 3, 'decrypt')
    print(f"\nCaesar Cipher:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Vigenère cipher example
    key = "key"
    encrypted = vigenere_cipher(text, key, 'encrypt')
    decrypted = vigenere_cipher(encrypted, key, 'decrypt')
    print(f"\nVigenère Cipher:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # ROT13 example
    encrypted = rot13(text)
    decrypted = rot13(encrypted)
    print(f"\nROT13:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Atbash cipher example
    encrypted = atbash_cipher(text)
    decrypted = atbash_cipher(encrypted)
    print(f"\nAtbash Cipher:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # A1Z26 example
    encrypted = a1z26(text, 'encrypt')
    decrypted = a1z26(encrypted, 'decrypt')
    print(f"\nA1Z26:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Bacon's cipher example
    encrypted = bacon_cipher(text, 'encrypt')
    decrypted = bacon_cipher(encrypted, 'decrypt')
    print(f"\nBacon's Cipher:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Morse code example
    encrypted = morse_code(text, 'encrypt')
    decrypted = morse_code(encrypted, 'decrypt')
    print(f"\nMorse Code:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Base64 example
    encrypted = base64_encode(text)
    decrypted = base64_decode(encrypted)
    print(f"\nBase64:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # XOR cipher example
    key = "secret"
    encrypted = xor_cipher(text, key)
    decrypted = xor_cipher(encrypted, key)
    print(f"\nXOR Cipher:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Affine cipher example
    a, b = 5, 8
    encrypted = affine_cipher(text, a, b, 'encrypt')
    decrypted = affine_cipher(encrypted, a, b, 'decrypt')
    print(f"\nAffine Cipher:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")

    # Polybius Square example
    encrypted = polybius_square(text, 'encrypt')
    decrypted = polybius_square(encrypted, 'decrypt')
    print(f"\nPolybius Square:\nOriginal: {text}\nEncrypted: {encrypted}\nDecrypted: {decrypted}")
"""