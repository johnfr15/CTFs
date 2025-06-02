#!/usr/bin/sage
import hashlib
import re

# with open("flag.txt", "rb") as f:
#     FLAG = f.read()
#     assert re.match(rb"Hero{[0-9a-zA-Z_]{90}}", FLAG)

H = lambda n: int(hashlib.sha256(n).hexdigest(), 16)

first = b'Hero'
print( H(first) )

first_polynomial_value = 83333617434192845616567795273380961636414036733866856584640402257709492844129
hex_first_value = hex(first_polynomial_value)[2:]  # Remove the '0x' prefix
print(hex_first_value)
