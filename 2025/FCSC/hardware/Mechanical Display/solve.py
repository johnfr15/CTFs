input_file = './mechanical-display.vcd'
with open(input_file, 'r') as f:
    lines = f.readlines()[12:]
from math import ceil, floor


table = "123456789abcdfs{}_"
nb_symbols = len(table)

step = 10 * 10  # Nombre de valeurs entières par caractère

char_to_range = {}

for i, char in enumerate(table):
    start = i * step + 1
    end = start + step
    for j in range(start, end):
        char_to_range[j] = char

print(char_to_range)

def get_value(start: int, end: int) -> str:
    min_us = 0.6 * 1000  # Convert 0.6V into equivalent "tick" (μs or time units)
    max_us = 2.4 * 1000  # Upper bound
    max = max_us - min_us

    pulse_width = (end - start) * 10 
    pulse = pulse_width - min_us

    if pulse <= 0:
        return "0"
    elif pulse >= max:
        return table[-1]

    return char_to_range[int(pulse)], pulse
 

for start, end in zip(lines[::2], lines[1::2]):
    start = int(start.split(" ")[0][1:])
    end = int(end.split(" ")[0][1:])

    print(get_value(start, end))
    