import random

def gen_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_str = ''.join(random.sample(letters, length))
    return result_str

random_length = 10
random_string = gen_random_string(random_length)
print("Random String:", random_string)
