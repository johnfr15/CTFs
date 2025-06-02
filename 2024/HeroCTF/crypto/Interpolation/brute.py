import hashlib
import itertools
import time
from multiprocessing import Pool, cpu_count, Manager

# The target hash to match
target_hash = int("16795951457632967907260395488972679537699281420039600914133493294730174311338")

# Define the character set used in CTF challenges
charset = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'  # 62 characters
charset_size = len(charset)

# Function to check if a generated hash matches the target hash
def matches_target_hash(byte_combination):
    # Convert the byte combination to bytes
    byte_string = bytes(byte_combination)
    
    # Compute the SHA-256 hash
    hash_result = hashlib.sha256(byte_string).hexdigest()
    
    # Convert the hex result to an integer
    hash_as_int = int(hash_result, 16)
    
    return hash_as_int == target_hash, byte_combination  # Return tuple

def parallel_bruteforce(start, end, progress_dict, total_combinations):
    """Brute-force hash checks for a specific range of combinations."""
    for i in range(start, end):
        # Generate the byte combination for the index
        combination = tuple(charset[(i >> (6 * j)) % charset_size] for j in range(4))  # 4 bytes, 6 bits each
        
        # Check if the combination matches the target hash
        match_found, combination = matches_target_hash(combination)
        if match_found:  # Unpack the tuple
            return f"Match found: {combination} -> {bytes(combination)}"
        
        # Update progress
        progress_dict.value += 1
        
        # Calculate and print progress
        if progress_dict.value % (total_combinations // 100) == 0:  # Update every 1%
            progress = (progress_dict.value / total_combinations) * 100
            print(f"Progress: {progress:.2f}%")
    
    return None  # No match found in this range

def main():
    # Total combinations for 4 bytes with the charset
    total_combinations = charset_size ** 4

    # Calculate number of CPU cores
    num_cores = cpu_count()
    
    # Split the total combinations across the available cores
    chunk_size = total_combinations // num_cores
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_cores)]
    
    # Handle the last chunk to include any remaining combinations
    ranges[-1] = (ranges[-1][0], total_combinations)

    # Use a Manager to share progress between processes
    manager = Manager()
    progress_dict = manager.Value('i', 0)  # Shared variable for progress

    # Start the multiprocessing pool
    with Pool(processes=num_cores) as pool:
        results = pool.starmap(parallel_bruteforce, [(start, end, progress_dict, total_combinations) for start, end in ranges])

    # Print results
    for result in results:
        if result:
            print(result)
            break
    else:
        print("No match found.")

if __name__ == "__main__":
    start_time = time.time()  # Start timing
    main()  # Run the main function
    end_time = time.time()  # End timing
    print(f"Execution time: {end_time - start_time:.2f} seconds")
