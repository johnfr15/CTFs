import binascii
from itertools import zip_longest

# Encrypted flag from the challenge
enc = "40f1b6e577b2bb6aa703387a15d2738ad50c795972342bdbb4b32946bcf7b72fbbdfb41884883df6589bf0e1e73a01f4f0d13a60146ac87c146de846bb98407d80000000000000000000000000000000000000000000000000000000000000000c4df9ca82064c5b97e3e5013732439d6139195456b94e581b7a22f1510f926c4117ca4ed6a10c5d37b5d400dca883d001564774dbbce5c198c5ff83fe7af851fc3820a17947e71689812f6113dd3893250a14320a8f49c46bde754a188efd3000000000000000000000000000000000000000000000000000000000000000000f6336ee243e9a18cd74b182ff23f87f8bbac8912b57cd3ab25faffcaa18ea3940d748f2696de5597ec5df6d12826fc2b37d8e926af7a39afe74cb0950460da1a33112d89029e1a9334ea4c19d36cab027d4b360f240139de4ebd58ebfb05681800000000000000000000000000000000000000000000000000000000000000029e03851f31bd96e478b63347dc9a369a5d0569dc00ffe07cc3ad2d8293a9bf0"
data = bytes.fromhex(enc)
blocks = [data[i*128:(i+1)*128] for i in range(3)]

def unpack_block(block):
    n = int.from_bytes(block, 'big')
    z = (n >> 1022) & 1
    abs_y = (n >> 511) & ((1 << 511) - 1)
    x = n & ((1 << 511) - 1)
    y = abs_y if z == 0 else -abs_y
    return x, y

triplets = [unpack_block(b) for b in blocks]
(x1, y1), (x2, y2), (x3, y3) = triplets

# Calculate d (b + c)
num = (x1**2 - x2**2) - (y1 - y2)
den = x1 - x2
d = num // den

# Calculate e (b * c)
e = y1 - x1**2 + d * x1

# Solve the quadratic: t^2 - d*t + e = 0 for t = b, c (b > c)
# Use integer sqrt for huge numbers (Python 3.8+)
def isqrt(n):
    if hasattr(int, "bit_length"):  # Python 3.8+
        return int(n ** 0.5)
    else:
        from sympy import isqrt
        return isqrt(n)

disc = d*d - 4*e
assert disc >= 0, "Discriminant negative, error in math!"

sq = int(disc ** 0.5)
if sq * sq != disc:
    import math
    sq = math.isqrt(disc)  # python >= 3.8

t1 = (d + sq) // 2
t2 = (d - sq) // 2
b, c = max(t1, t2), min(t1, t2)

# Convert back to bytes
# To find the correct length, take half the total flag length
l_b = (b.bit_length() + 7) // 8
l_c = (c.bit_length() + 7) // 8
even_bytes = b.to_bytes(l_b, 'big')
odd_bytes = c.to_bytes(l_c, 'big')

# Interleave bytes: flag[::2]=even_bytes, flag[1::2]=odd_bytes
flag_bytes = bytearray()
for e, o in zip_longest(even_bytes, odd_bytes, fillvalue=None):
    flag_bytes.append(e)
    if o is not None:
        flag_bytes.append(o)

try:
    flag = flag_bytes.decode()
except UnicodeDecodeError:
    flag = flag_bytes

print("Recovered flag:", flag)
