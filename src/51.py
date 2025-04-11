import random
def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

random_number = 123456789
print(f"Random string: {generate_random_string(random_number)}")
