import random
import numpy as np
import matplotlib.pyplot as plt

def kg(l):
    return bytes([random.randint(0,255) for i in range(l)])

def c(p):
    k = kg(len(p))
    return (k, bytes([k[i] ^ p[i] for i in range(len(p))]))

def generate(n):

    keys = []
    rn = []
    for _ in range(n):
        (k, random) = c("secret".encode())
        keys += k
        rn += random
    
    return (keys, rn)

# Generate OTP keys and random numbers
(otp_keys, random_numbers) = generate(1000)

# Perform statistical analysis
# Calculate Pearson correlation coefficient
correlation_coefficient = np.corrcoef(otp_keys, random_numbers)[0, 1]
print("Pearson correlation coefficient:", correlation_coefficient)

# Create scatter plot
plt.scatter(otp_keys, random_numbers)
plt.xlabel("OTP keys")
plt.ylabel("Random numbers")
plt.title("Scatter plot of OTP keys vs. Random numbers")

# Save the plot as an image file
plt.savefig('scatter_plot.png')

plt.show()
