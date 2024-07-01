import numpy as np

def read_file(filename):
    with open(filename, "r") as f:  # Open the file for reading
        lines = f.readlines()  # Read all lines from the file
        bytes_data = []  # Initialize an empty list to store the bytes data
        for line in lines:  # Iterate over each line in the file
            hex_string = line.strip()  # Remove leading/trailing whitespace
            byte_list = list(bytes.fromhex(hex_string))  # Convert hex string to bytes list
            bytes_data.append(byte_list)  # Append the bytes list to the result
    return np.array(bytes_data) 

# Calculate the median value of each byte index
def calculate_median(bytes_data):

    median = []
    for i in range(len(bytes_data[0])):
        median.append(int(np.median(bytes_data[:, i])))

    return np.array(median)

# XOR median values with the median value of range(0, 255)
def xor_with_median(median_values):
    median_xor = median_values ^ np.array([126] * 19)
    return median_xor

# Main function
def main(filename):
    # Read file and extract bytes
    bytes_data = read_file(filename)
    
    print(bytes_data)

    # Calculate median values
    median_values = calculate_median(bytes_data ^ 128)
    print("Median values of each byte index:", median_values)

    # XOR with median of range(0, 255)
    # median_xor = xor_with_median(median_values)
    # print("XOR with median of range(0, 255):", median_xor)

if __name__ == "__main__":
    filename = "dictionnary.txt"  # Change this to your file name
    main(filename)
