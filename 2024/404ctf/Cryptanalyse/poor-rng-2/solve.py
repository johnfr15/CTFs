import z3
from LFSR import LFSR
from generator import CombinerGenerator

# Took from encrypt.py
def xor(b1, b2):
	return bytes(a ^ b for a, b in zip(b1, b2))

# Took from encrypt.py
poly1 = [19,5,2,1] # x^19+x^5+x^2+x
poly2 = [19,6,2,1] # x^19+x^6+x^2+x
poly3 = [19,9,8,5] # x^19+x^9+x^8+x^5

def combine(x1, x2, x3):
    """Rewrite `combine` using arithmetic equivalent of `AND`: multiplication""" 
    return (x1 * x2) ^ (x1 * x3) ^ (x2 * x3)

with open("flag.png.part", "rb") as f:
    clear_partial_content = f.read()

with open("flag.png.enc", "rb") as f:
    encrypted_content = f.read()

# We now have our first bytes used to cipher the flag
key = xor(clear_partial_content, encrypted_content)


# Turn the bytes into bits
bits = [int(bit) for byte in key for bit in format(byte, "08b")]

solver = z3.Solver()

# Define our constraints, we are looking for 3 array of 19 bits
state_1 = [z3.BitVec(f"s1_{i}", 1) for i in range(19)]
state_2 = [z3.BitVec(f"s2_{i}", 1) for i in range(19)]
state_3 = [z3.BitVec(f"s3_{i}", 1) for i in range(19)]


L1 = LFSR(fpoly=poly1, state=state_1)
L2 = LFSR(fpoly=poly2, state=state_2)
L3 = LFSR(fpoly=poly3, state=state_3)

# Defining our equations
# Every bit in the key is the result of `combine(b1, b2, b3)`
for bit in bits:
    solver.add(bit == combine(L1.generateBit(), L2.generateBit(), L3.generateBit()))


assert solver.check() == z3.sat

print(solver.model())

#[s2_16 = 1,
# s3_10 = 1,
# s2_9 = 0,
# s1_6 = 1,
# s1_11 = 1,
#...
#]

# We successfully retrieve our states, we can simply copy/paste the source code we are given
# and reverse the operation
result = {
"s2_16": 1,
"s3_10": 1,
"s2_9": 0,
"s1_6": 1,
"s1_11": 1,
"s1_7": 1,
"s3_2": 0,
"s3_9": 0,
"s2_14": 1,
"s2_3": 0,
"s2_18": 0,
"s2_2": 0,
"s2_15": 0,
"s2_8": 1,
"s1_9": 0,
"s1_12": 0,
"s1_1": 0,
"s3_1": 1,
"s2_5": 1,
"s3_8": 0,
"s1_13": 0,
"s2_11": 0,
"s3_15": 1,
"s1_4": 1,
"s1_15": 1,
"s3_7": 0,
"s3_18": 1,
"s2_12": 1,
"s3_6": 1,
"s2_6": 1,
"s1_2": 1,
"s2_4": 0,
"s3_4": 0,
"s2_1": 0,
"s2_0": 1,
"s2_7": 1,
"s3_13": 0,
"s2_10": 0,
"s3_12": 0,
"s1_17": 1,
"s1_10": 1,
"s2_17": 1,
"s3_16": 1,
"s1_3": 0,
"s1_18": 1,
"s3_11": 0,
"s1_8": 1,
"s1_16": 1,
"s3_0": 1,
"s3_14": 1,
"s3_3": 1,
"s3_5": 0,
"s1_5": 1,
"s2_13": 1,
"s1_0": 1,
"s1_14": 1,
"s3_17": 1
}

L1 = LFSR(fpoly=poly1, state=[result[f"s1_{i}"] for i in range(19)])
L2 = LFSR(fpoly=poly2, state=[result[f"s2_{i}"] for i in range(19)])
L3 = LFSR(fpoly=poly3, state=[result[f"s3_{i}"] for i in range(19)])

generator = CombinerGenerator(combine, L1, L2, L3)

# read the encrypted flag
with open("flag.png.enc","rb") as f:
	encrypted_flag = f.read()

#decrypt the flag
decrypted_flag = b''
for i in range(len(encrypted_flag)):
	random = generator.generateByte()
	byte = [encrypted_flag[i]]
	decrypted_flag += xor(byte,random)

#write decrypted flag
with open("decrypted_flag.png","wb") as f:
	f.write(decrypted_flag)