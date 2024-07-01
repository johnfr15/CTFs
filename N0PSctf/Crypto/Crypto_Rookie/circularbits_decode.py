# Translate a "bitstr" to its decimal value eg.('01000011' => 67 )
#
def  bitstr_to_byte(bitstr: str) -> int:
    n: int = 0

    bits = [bit for bit in bitstr]
    bits = bits[::-1]

    # For each bit in the bitstr we will bind it to a "byte" (eg. 0000 0000)
    # 0000 0000 | (0000 0001 << 0) == 0000 0001
    # 0000 0001 | (0000 0000 << 1) == 0000 0001
    # 0000 0001 | (0000 0001 << 2) == 0000 0101
    # ...
    # 0000 0101 | (0000 0001 << 7) == 1000 0101
    #
    for idx, bit in enumerate(bits):
        n = n | (int(bit) << idx) 

    return n


# Translate a string to its "bitstr" value 
# example: 'Hello' => "0110111101101100011011000110010101001000"
#
def text_to_strbit(text: str, base: int = 8) -> int:
    strbit = ''

    for char in text:
        i = 0
        n = ord(char)
        
        while i != base:
            if n & 0x01 == 0x01:
                strbit += '1'
            else:
                strbit += '0'

            n = n >> 1
            i += 1

    return strbit[::-1]



# Translate a decimal to its "bitstr" value 
# example: 67 => "01000011"
#
def byte_to_strbit(number: int, base: int = 8) -> str:
    strbit = ''
    i = 0

    while i != base:

        if number & 0x01 == 0x01:
            strbit += '1'
        else:
            strbit += '0'
        number = number >> 1

        i += 1

    return strbit[::-1]



# Where
#   n = number. Our initial number
#   s = shift. How many bits we wanna shift
#   b = base. How much bits we gonna use before circulating
def left_circular_shift(n: int, s: int, b: int = 8) -> int:

    n = (n << s) | (n >> (b - s)) # Perform the rotation
    n &= (1 << b) - 1 # Clean the moved bits after our base length

    return n



# Perform bit shifting (in this case "char" rotation) for every blocks
def left_rotation(blocks: str, shift: int) -> int:
    rotated = []

    for block in blocks:
        s_block = block[:shift]
        block = block[shift:]
        rotated.append( ''.join(block + s_block) )

    return rotated




# Where
#
#   data:  The ciphered information
#   shift: How many bits we wanna shift
#   base:  How much bits we gonna use before circulating
#
def recover(data: str, shift: int, blockSize: int) -> str:
    blocks = []

    # 1. Divide the "bits string" into blocks of size defined in the parameters
    bits = data.split(" ")

    for i in range(0, len( bits ), blockSize):
        blocks.append( ''.join( bits[i:i+blockSize] ) )

    # 2. Perform left "bit shifting" for every blocks
    bits = left_rotation(blocks, shift)
    bits = ''.join( bits ) # Reassemble our initial "bits string" but without the spaces

    # 3. Split the "bits string" into 8 bits array (the size of 1 byte) 
    chunks = [ bits[i:i+8] for i in range(0, len(bits), 8) ]

    # 4. Get our final deciphered string. For each element in array we translate the "bits string" into its decimal value
    deciphered = ''
    for chunk in chunks:
        n = bitstr_to_byte( chunk ) # from bitstr to decimal eg.('01000011' => 67 )
        deciphered += chr( n ) # from decimal to ascii
    
    return deciphered



if __name__ == '__main__':

    data = "01010011 01010100 01010011 01000001 01000010 01000101 01000001 01001111 01000101 00100000 01001111 01000101 01001001 01000101 01000001 01001100 01000111 01010011 01000101 01010100 01010010 01001000 01001110 01000011 01001111 01001001 00100000 01001101 01001101 01000110 01001001 01010100 01010100 01000001 01001011"


    for shift in range(-25, 25):
        for blockSize in range(1,10):
            text = recover(data, shift, blockSize)
            print(f"[shift: {shift}, blockSize {blockSize}]     {text}")

    print( byte_to_strbit(67) )