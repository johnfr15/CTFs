import re

def process_dump(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        match = line.strip().split(" ")
        # print(match)
        if match:
            chr_value = match[1]
            nextchr_expression = "".join(match[3:])
            
            if  "exit" in nextchr_expression or match[2] != "NEXTCHR:":
                print(f"{" ".join(match)}")
            else:
                try:
                    # Safely evaluate the NEXTCHR expression
                    result = eval(nextchr_expression)
                    print(f"CHR: {chr_value} -> NEXTCHR result: {result}")
                except Exception as e:
                    print(f"Error evaluating NEXTCHR for CHR: {chr_value} -> {e}")

# Use the function with the path to your dump.txt file
process_dump('raw.txt')
