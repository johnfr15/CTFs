def xor_files(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        data1 = f1.read()
        data2 = f2.read()
    
    # Ensure both files have the same length
    if len(data1) != len(data2):
        raise ValueError("Files must be of equal length")
    
    # Perform XOR operation
    result = bytes(a ^ b for a, b in zip(data1, data2))
    
    # Write the result to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(result)

if __name__ == "__main__":
    xor_files('file1.txt', 'file2.txt', 'file3.txt')
