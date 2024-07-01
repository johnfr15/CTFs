from itertools import cycle

# Create a cycle iterator for a list
cyclic_iterator = cycle([1, 2, 3])

# Using the cyclic iterator
for _ in range(10):  # Just an example to show the cycling behavior
    print(next(cyclic_iterator))


flag = "exampleflag"
key = "key"

# Create an infinite cycle of the key
key_cycle = cycle(key)

# Zip the flag with the cycled key
result = zip(flag, key_cycle)

# You might want to collect the results into a list or tuple
result_list = list(result)

print(result_list)
