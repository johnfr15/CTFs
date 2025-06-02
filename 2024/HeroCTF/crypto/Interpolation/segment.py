import hashlib


# Hash function - replace with actual hash function if known
def hash_string(input_string):
    # Use SHA-256 and convert to an integer
    hashed = hashlib.sha256(input_string).hexdigest()
    print("HEX Hero => ", hashed)



# Hash the prefix "Hero" and compare
prefix_hash = hash_string(b"Hero")


# hashlib.sha256(b"Hero").hexdigest() => 72a9345fb29494a4e9667d7bd68f37e8fe1df384270553f17b4c4a06b1f2b5e0