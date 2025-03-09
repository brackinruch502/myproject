import random

def get_random_number(n):
    return random.randint(0, n)

def get_random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

def get_random_boolean():
    return random.choice([True, False])

def get_random_tuple(length, elements):
    return tuple(random.choice(elements) for _ in range(length))

def get_random_list(length, elements):
    return [random.choice(elements) for _ in range(length)]

def get_random_dictionary(keys, values):
    return dict((random.choice(keys), random.choice(values)) for _ in range(len(keys)))
