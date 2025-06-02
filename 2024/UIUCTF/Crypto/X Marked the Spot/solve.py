from itertools import cycle

flag = b"uiuctf{????????????????????????????????????????}"
# len(flag) = 48
key  = b"????????"
# len(key) = 8
ct = bytes(x ^ y for x, y in zip(flag, cycle(key)))


# 1. Read encrypted flag as bytes array
with open("ct", "rb") as ct_file:
    cflag = ct_file.read()


# 2. Get original key
key_origin = b""
reverse_xor = [ fileb ^ flagb for fileb, flagb in zip(flag, cflag)]
# Above we are given the 7th first bytes but also the last of the flag which can complete the entire key
key_origin = bytes(reverse_xor[:7]) + bytes([reverse_xor[-1]])


# 3. Get flag
flag_origin = ''.join([ chr(k ^ f) for k, f in zip(cycle(key_origin), cflag )])

print("flag: ", flag_origin)