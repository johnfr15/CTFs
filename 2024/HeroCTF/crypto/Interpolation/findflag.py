import itertools

# Possible characters for each position
positions = [
    ['T', 't', '7'],  # First character could be 'T', 't', or '7'
    ['H', 'h'],       # Second character could be 'H' or 'h'
    ['3', 'e', 'E'],  # Third character could be '3', 'e', or 'E'
]

# Generate all combinations of the missing part
combinations = [''.join(combo) for combo in itertools.product(*positions)]

# Template for the string with a placeholder for the missing part
template = "Hero{{{}r3_4r3_tw0_typ35_0f_p30pl3_1n_th15_w0rld_th053_wh0_c4n_3xtr4p0l4t3_fr0m_1nc0mpl3t3_d4t4}}"

# Construct each complete string with the missing part filled in
full_strings = [template.format(combo) for combo in combinations]

# Display each generated string
for string in full_strings:
    print(string)
