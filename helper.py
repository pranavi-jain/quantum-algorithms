import random
import uuid

## Generate a UUID based unique key
def generate_short_key():
    return str(uuid.uuid4())[:8]  # First 8 characters of a UUID


## Generate random list of n-bit strings of length atmost 4
def generate_random_n_bit_strings(n):
    # Step 1: Generate a random number x less than 4
    if n<=3:
        x = 1
    else:
        x = random.randint(1, 4)
    
    # Step 2: Generate x random n-bit binary strings
    n_bit_strings = [format(random.randint(0, 2**n - 1), f'0{n}b') for _ in range(x)]
    
    return n_bit_strings
