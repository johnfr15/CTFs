import re

def process_and_sort_dump(file_path):
    results = []
    pattern = r'CHR: (.*?) NEXTCHR: (.+)'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        match = re.match(pattern, line.strip())
        if match:
            chr_value = match.group(1)
            nextchr_expression = match.group(2)

            try:
                result = eval(nextchr_expression)
                results.append((chr_value, result))
            except Exception as e:
                print(f"Error evaluating NEXTCHR for CHR: {chr_value} -> {e}")

    # Sort the results by the NEXTCHR result value
    results.sort(key=lambda x: x[1])

    # Print the sorted results
    for chr_value, result in results:
        print(f"CHR: {chr_value} -> NEXTCHR result: {result}")

# Use the function with the path to your dump.txt file
process_and_sort_dump('flag.txt')
