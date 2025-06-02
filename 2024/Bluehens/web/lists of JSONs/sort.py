import re

# Open and read the contents of "calc.txt"
with open("calc.txt", "r") as file:
    data = file.read()

# Regular expression to match the relevant lines
pattern = r"CHR: (.) -> NEXTCHR result: (\S+)"

# Create a list to store parsed data
entries = []

# Parse the data
for line in data.splitlines():
    match = re.search(pattern, line)
    if match:
        char = match.group(1)
        result = float(match.group(2)) if '.' in match.group(2) else int(match.group(2))
        entries.append((char, result))

# Sort the entries by result
sorted_entries = sorted(entries, key=lambda x: x[1])

# Print sorted results
for char, result in sorted_entries:
    print(f"CHR: {char} -> NEXTCHR result: {result}")
