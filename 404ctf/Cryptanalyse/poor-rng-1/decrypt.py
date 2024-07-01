from itertools import islice
from my_decrypt_random import MyGenerator

def get_key(a, b):
    key = []
    mapped = zip(a, b)

    for a, b in islice(mapped, 2000):
        key.append(a ^ b)

    return key

def xor(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def get_blocks(data,block_size):
	return [data[i:i+block_size] for i in range(0,len(data),block_size)]

def pad(data,block_size):
	return data+b'\x00'*(block_size-len(data)%block_size)

def decrypt(data, block_size, key):
    padded_data = pad( data,block_size )
    data_blocks = get_blocks( padded_data, block_size )
    generator = MyGenerator(key)
    encrypted = b''

    for block in data_blocks:
        rd = generator.get_random_bytes(block_size)
        xored = xor(block,rd)
        encrypted += xored

    return [byte for byte in encrypted]




BLOCK_SIZE = 4
flag = None

with open("flag.png.enc", "rb") as f:
    flag_png_enc = [ byte for byte in f.read() ]

with open("flag.png.part", "rb") as f:
    flag_png_part = [ byte for byte in f.read() ]






if __name__ == '__main__':
    key = get_key( flag_png_enc, flag_png_part )
    flag = []

    for i in range(2000):
        flag.append(flag_png_enc[i] ^ key[i])

    with open("flag.png.enc", "rb") as f:
        flag_png_enc = f.read()  

    flag += decrypt(flag_png_enc[2000:], BLOCK_SIZE, key)

    with open("flag.png", "w+b") as f:
        for byte in flag:
            f.write(bytes([byte]))




# OUTPUT


print("Fichier déchiffré enregistré avec succès.")