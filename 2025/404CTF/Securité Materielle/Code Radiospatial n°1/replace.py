f = open("out.txt", "rb")
d = f.readlines()
f.close()

# Replace null bytes and 0x01 with ASCII '0' and '1'
d[0] = d[0].replace(b'\x00', b'0')
d[0] = d[0].replace(b'\x01', b'1')

# Convert to string and strip whitespace/newlines
bitstream = d[0].strip().decode()  # decode from bytes to string

def bits_to_ascii(bit_list):
    """
    bit_list: string of 8 bits, e.g. '01100101'
    Returns the ASCII character for these 8 bits.
    """
    byte_value = int(bit_list, 2)
    return chr(byte_value)

final = ""
for i in range(0, len(bitstream), 8):
    chunk = bitstream[i:i+8]
    if len(chunk) == 8:
        final += bits_to_ascii(chunk)

print(final)
