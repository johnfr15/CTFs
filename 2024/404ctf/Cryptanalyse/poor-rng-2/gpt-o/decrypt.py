import random as rd
from LFSR import LFSR
from generator import CombinerGenerator

def xor(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# The provided polynomials
poly1 = [19, 5, 2, 1]
poly2 = [19, 6, 2, 1]
poly3 = [19, 9, 8, 5]

# Combine function
combine = lambda x1, x2, x3 : (x1 and x2) ^ (x1 and x3) ^ (x2 and x3)

# Load the known plaintext and ciphertext
with open('flag.png.part', 'rb') as f:
    known_plaintext = f.read()
with open('flag.png.enc', 'rb') as f:
    encrypted_flag = f.read()

# Brute-force initial state possibilities for recovery
def brute_force_initial_states(poly1, poly2, poly3, known_plaintext, known_ciphertext):
    max_poly = max(max(poly1), max(poly2), max(poly3))
    tot = 2**max_poly 
    j = 0
    for state_bits in range(2 ** max_poly):
        state1 = [(state_bits >> i) & 1 for i in range(max(poly1))]
        state2 = [(state_bits >> i) & 1 for i in range(max(poly2))]
        state3 = [(state_bits >> i) & 1 for i in range(max(poly3))]
        
        L1 = LFSR(fpoly=poly1, state=state1)
        L2 = LFSR(fpoly=poly2, state=state2)
        L3 = LFSR(fpoly=poly3, state=state3)
        
        generator = CombinerGenerator(combine, L1, L2, L3)
        
        extracted_keystream = bytearray()
        for i in range(len(known_plaintext)):
            extracted_keystream.extend(generator.generateByte())
        
        if xor(extracted_keystream, known_ciphertext) == known_plaintext:
            return state1, state2, state3

        j+=1
        print(round(j/tot*100,2),"%",end="\r")		# pour faire joli

    return None, None, None

# Known ciphertext (first 35 bytes)
known_ciphertext = encrypted_flag[:35]

# Perform brute-force attack to determine the initial states
initial_state1, initial_state2, initial_state3 = brute_force_initial_states(poly1, poly2, poly3, known_plaintext, known_ciphertext)

if initial_state1 is None:
    print("Failed to recover initial states")

# Create LFSRs with recovered initial states
L1 = LFSR(fpoly=poly1, state=initial_state1)
L2 = LFSR(fpoly=poly2, state=initial_state2)
L3 = LFSR(fpoly=poly3, state=initial_state3)

# Create generator
generator = CombinerGenerator(combine, L1, L2, L3)

# Decrypt the entire encrypted flag
decrypted_flag = b''
for i in range(len(encrypted_flag)):
    random_byte = generator.generateByte()
    decrypted_flag += xor(encrypted_flag[i:i+1], random_byte)

# Write the decrypted flag to a file
with open('recovered_flag.png', 'wb') as f:
    f.write(decrypted_flag)

print("Flag has been recovered and written to 'recovered_flag.png'")