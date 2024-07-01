def decrypt_playfair(ciphertext, key):
    def generate_playfair_square(key):
        key = key.replace('J', 'I')  # Replace 'J' with 'I' for consistency
        key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates and maintain order
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Exclude 'J' from the alphabet
        key += ''.join(filter(lambda x: x not in key, alphabet))
        return [key[i:i+5] for i in range(0, 25, 5)]

    def find_position(square, letter):
        for row_idx, row in enumerate(square):
            if letter in row:
                return (row_idx, row.index(letter))
        return None

    def decrypt_digraph(square, digraph):
        (x1, y1), (x2, y2) = find_position(square, digraph[0]), find_position(square, digraph[1])
        if x1 == x2:  # Same row
            return square[x1][(y1 - 1) % 5] + square[x2][(y2 - 1) % 5]
        elif y1 == y2:  # Same column
            return square[(x1 - 1) % 5][y1] + square[(x2 - 1) % 5][y2]
        else:  # Forming rectangle
            return square[x1][y2] + square[x2][y1]

    key = key.upper().replace('J', 'I')  # Convert key to uppercase and replace 'J' with 'I'
    plaintext = ''
    square = generate_playfair_square(key)

    # Prepare ciphertext by removing spaces and converting to uppercase
    ciphertext = ciphertext.upper().replace(' ', '')

    # If the length of the ciphertext is odd, add a padding character
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'  # Padding character

    # Decrypt ciphertext digraph by digraph
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        plaintext += decrypt_digraph(square, digraph)

    return plaintext

# Example usage:
ciphertext = "STSABEAOE OEIEALGSETRHNCOI MMFITTAK"
key = "N0PS"
plaintext = decrypt_playfair(ciphertext, key)
print("Decrypted Message:", plaintext)
