import numpy as np
from Crypto.Util.number import long_to_bytes

Flag = [
    [504280474484, 0, 0, 0, 0],
    [0, 440157893172, 0, 0, 0],
    [0, 0, 426031081311, 0, 0],
    [0, 0, 0, 163852545397, 0],
    [0, 0, 0, 0, 465806107005],
]

l_flag = [504280474484,440157893172,426031081311,163852545397,465806107005]

flag = b""
for long in l_flag:
    flag += long_to_bytes(long) 

print( flag )