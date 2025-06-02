import sys
from PIL import Image

sys.set_int_max_str_digits(100000)

WIDTH = 400
HEIGHT = 200

with open('./number.txt', 'r') as f:
    enc = int(f.read().strip(), 10)

def convert_image(image_path):
    image = Image.open(image_path).convert('L')
    pixels = list(image.getdata())
    binary_representation = ''.join(['1' if pixel == 255 else '0' for pixel in pixels])
    return int(binary_representation,2)

def reconstruct_image(value: int, width: int, height: int):
    """
    Reverse of convert_image:
      - value: the integer returned by convert_image
      - width, height: dimensions of the original image
      - output_path: where to save the reconstructed image
    """
    # 1. Convert the integer back to a binary string of the right length
    total_pixels = width * height
    bin_str = bin(value)[2:].zfill(total_pixels)

    # 2. Create a new 'L' (grayscale) image and map bits back to pixels
    img = Image.new('L', (width, height))
    pixels = img.load()
    for idx, bit in enumerate(bin_str):
        x = idx % width
        y = idx // width
        # In the original, 255→'1', else→'0'
        pixels[x, y] = 255 if bit == '1' else 0

    # 3. Save out
    img.save("./flag.png")
    print(f"Reconstructed image saved to {"./flag.png"}")


def encrypt_number(number,key):
    new_number = 0
    shift = 0
    while number:
        bloc = (number & 0xFFFF_FFFF_FFFF_FFFF) ^ key
        new_number |= (bloc << shift) 
        number >>= 64 
        shift += 64
    return new_number

def decrypt_number(encrypted, key):
    """Reverse the block‑wise XOR encryption."""
    original = 0
    shift    = 0
    n        = encrypted
    while n:
        # Extract the low 64‑bit block, XOR with key to recover original block
        bloc = (n & 0xFFFF_FFFF_FFFF_FFFF) ^ key
        # Reassemble into the output integer at the correct position
        original |= (bloc << shift)
        # Move to next 64‑bit block
        n >>= 64
        shift += 64
    return original

key = 0xFFFF_FFFF_FFFF_FFFF ^ int.from_bytes(b"~\xd8y7\xd8\xed\n\x11")
number = decrypt_number(int(enc), key)
reconstruct_image(number, WIDTH, HEIGHT)
