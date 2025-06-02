# XOR with a known flag format (e.g., "udctf{...}")
XFLAG = "11010210041e125508065109073a11563b1d51163d16060e54550d19"
flag_bytes = bytes.fromhex(XFLAG)

# Define a known flag format (partially or fully)
known_flag_format = b"deadbeef"  # We know it starts with "udctf{"

# XOR the bytes to match the known format
decrypted_flag = bytes([b ^ known_flag_format[i % len(known_flag_format)] for i, b in enumerate(flag_bytes)])

# Print the decrypted flag as a string
print("Decrypted Flag:", decrypted_flag.decode('utf-8', 'ignore'))
