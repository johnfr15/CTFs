import hashlib
import itertools
import sys  # Import sys to use sys.stdout.flush()

# Coefficients obtained from the original polynomial
coeffs = [
    37382279584575671665412736907293996338695993273870192478675632069138612724862, 
    91356407137791927144958613770622174607926961061379368852376771002781151613901
]

# Generate character set from ASCII 32 (space) to ASCII 126 (~)
charset = ''.join(chr(i) for i in range(32, 127))  # This creates a string of all printable characters

# Function to generate all possible 4-byte sequences
def generate_4_byte_sequences():
    for sequence in itertools.product(charset, repeat=4):
        yield ''.join(sequence)  # Joining characters

# Function to find the original flag chunks
def find_flag_chunks(hashes):
    found_chunks = []
    total_hashes = len(hashes)
    
    for i, h in enumerate(hashes):
        # Calculate and print the progress percentage
        progress = (i + 1) / total_hashes * 100
        print(f"\rProcessing hash {i+1}/{total_hashes} ({progress:.2f}%)", end='', flush=True)

        for seq in generate_4_byte_sequences():
            # Check if the hash matches
            if int(hashlib.sha256(seq.encode('utf-8')).hexdigest(), 16) == h:
                print(f" - Found chunk {i}: {seq}")  # Show the found chunk
                found_chunks.append(seq.encode('utf-8'))  # Append as bytes
                break
    
    print()  # Move to the next line after completing the loop
    return found_chunks

# Find the original flag chunks
flag_chunks = find_flag_chunks(coeffs)

# Print the discovered flag chunks
print("Recovered Flag Chunks:")
for chunk in flag_chunks:
    print(chunk.decode('utf-8'))

# Rebuild the full flag from chunks
full_flag = b''.join(flag_chunks)
print("Full Flag:", full_flag.decode('utf-8'))
