with open("dist.txt", "r") as f:
    xlines = [l.strip() for l in f.readlines()]


# [ print(bytes.fromhex(l)) for l in xlines]

# Find the shortest string by length
shortest_string = min(xlines, key=len)

# Print the shortest string
print("Shortest string:", shortest_string, len(shortest_string))

# KEY BEGIN
# b'4\x11)\xee\xea\x8aM\xc5\x17\xb9\xa1\x89\xb7|\xd5@M\xc6*\x0e&0"\xe6\xd0g\x89\xc4\x10\x14\xc5ke\x1c\xb3K\x12|m?\xfb\xd5'