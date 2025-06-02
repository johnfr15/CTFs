import pwn
import math
from sympy import primefactors

def greatest_prime_factor(n):
    """Returns the greatest prime factor of the given number n."""
    factors = primefactors(n)
    if factors:
        return max(factors)
    else:
        return None
    
def lcm(a, b):
    """Compute the least common multiple of two integers a and b."""
    return abs(a * b) // math.gcd(a, b)

FUNC = {
    "Give_me_the_greatest_common_divisor": math.gcd,
    "Give_me_the_greatest_prime_factor": greatest_prime_factor,
    "Give_me_the_least_common_multiple": lcm,
}
PORT = 10542
HOST = "challs.n00bzunit3d.xyz"

# Establish a connection to the remote host
c = pwn.remote(HOST, PORT, timeout=5)
print("[+] Connected to the server")
response = c.recvline().decode().strip()  # Increase buffer size if necessary
print(response)

while True:

    round = c.recvline().decode().strip()  # Increase buffer size if necessary
    print(round)
    q = c.recv(1024).decode().strip()  
    print(q)

    f = "".join(q.split("of")[0].strip().replace(" ", "_"))
    func = FUNC[f]
    args = [ int(arg.strip()) for arg in q.split("of")[1].replace(":", "").split("and") ]
  
    answer: int = func(*args)
    print("answer", answer)

    c.sendline(str(answer))

    correct = c.recvline().decode().strip()  
    print(correct)
    print("\n\n\n")

