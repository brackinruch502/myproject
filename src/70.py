import random

def generate_random_string(length=16):
    """Generate a random string of specified length."""
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))

print(generate_random_string())
