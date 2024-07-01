import numpy as np



#############################
#          2nd PART         #
#############################

def check_parity(data):
    # Calculate the sum of all bits except the parity bit
    sum_bits = sum(data[:-1])
    
    # Calculate the expected parity based on the sum
    expected_parity = sum_bits % 2
    
    # Check if the expected parity matches the actual parity bit
    return expected_parity == data[-1]


     
def decode_data(d):

    if ( check_parity(d) == False ):
        d[3] = (d[3] + 1) % 2

    return list( d[:-1] ) 



def decode_file(bits):
    
    input = []
    for i in range(0,len(bits),8):
        decoded = decode_data( bits[i:i+8] )
        input += decoded.copy()
    
    _bytes = np.packbits(input)

    return _bytes
    




#############################
#          1st PART         #
#############################

def decode_channel(channel):
    with open("channel_" + str(channel), "rb") as f:
        data = np.fromfile(f, dtype='uint8')

    # Convert ASCII values to integers 0 and 1
    bits = data - 48
    
    return bits



def decode_transmission():
    # Load data from each channel
    from_channel_1 = decode_channel(1)
    from_channel_2 = decode_channel(2)
    from_channel_3 = decode_channel(3)
    from_channel_4 = decode_channel(4)
    from_channel_5 = decode_channel(5)
    from_channel_6 = decode_channel(6)
    from_channel_7 = decode_channel(7)
    from_channel_8 = decode_channel(8)
    # Reconstruct the transmitted data
    transmitted_data = np.zeros( (len(from_channel_1), 8), dtype=int )
    transmitted_data[:,0] = from_channel_1
    transmitted_data[:,1] = from_channel_2
    transmitted_data[:,2] = from_channel_3
    transmitted_data[:,3] = from_channel_4
    transmitted_data[:,4] = from_channel_5
    transmitted_data[:,5] = from_channel_6
    transmitted_data[:,6] = from_channel_7
    transmitted_data[:,7] = from_channel_8


    # Recover the original data by removing the checksum and converting back to bytes
    original_data = np.concatenate(transmitted_data)

    return original_data





#############################
#           START           #
#############################

if __name__ == "__main__":
    transmission = decode_transmission()
    flags = decode_file(transmission)

    with open("flag.png", "wb") as f:
        f.write(bytes(flags))