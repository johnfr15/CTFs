from hashlib import sha256

print(sha256(bytes.fromhex("00000000000000000000000000000000")[::-1]).digest())