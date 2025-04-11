import random

def random_code_generator():
    """
    Generates a random code.
    """
    return f"random_code_{random.randint(10000, 99999)}"

code = random_code_generator()
print(code)
