import itertools


def decrypt_vigenere_alpha(encrypted_text, key):
    decrypted_text = []
    repeated_key = itertools.cycle(key)

    for e, k in zip(encrypted_text, repeated_key):
        # Calculate the index of the current character and key character
        ei = ord(e) - ord('a')
        ki = ord(k) - ord('a')
        
        # Calculate the shifted index
        shifted_index = (ei - ki) % 26
        
        # Append the resulting character to the decrypted text
        decrypted_text.append(chr(shifted_index + ord('a')))

    # Join the list of characters into a string
    return ''.join(decrypted_text)


with open("enc.txt", 'r') as f:
    flag = f.readline().strip().split(' ')[-1]
    key = f.readline().strip().split(" ")[-1]


repeated_key = itertools.cycle(key)

xorpt = ''.join([ chr(ord(k) ^ ord(e)) for k,e in zip(flag, repeated_key) ])

print(decrypt_vigenere_alpha(flag, key))