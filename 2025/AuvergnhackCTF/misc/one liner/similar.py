def sum_characters_from_files(file1_path, file2_path, output_path):
    # Read the contents of both files
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()

    # Sum the characters from both files and write to the output file
    with open(output_path, 'w') as output_file:
        for char1, char2 in zip(content1, content2):
            # Sum the ASCII values of the characters
            sum_char = chr((ord(char1) * ord(char2)))
            output_file.write(sum_char)

if __name__ == "__main__":
    file1_path = "file1.txt"  # Path to the first file
    file2_path = "file2.txt"  # Path to the second file
    output_path = "summed_characters.txt"  # Path to the output file

    sum_characters_from_files(file1_path, file2_path, output_path)
    print(f"Summed characters have been written to {output_path}")
