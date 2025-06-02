# Initial number
n = 696968

# Number of iterations
iterations = 20

# Loop to perform the subtraction
for i in range(iterations):
    n -= n // 2
    print(f"Iteration {i + 1}: {n}")

print("Final result after 20 iterations:", n)
