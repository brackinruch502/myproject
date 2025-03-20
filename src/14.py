import random

def add_random_number_to_string():
    # Generate a random number between 1 and 9
    random_number = random.randint(1, 9)
    
    # Randomly add this number to a string of letters 'abc'
    words = "abc"
    string_of_letters = "".join(random.sample(words, random.randint(5, 8)))
    
    return string_of_letters + str(random_number)

if __name__ == "__main__":
    result = add_random_number_to_string()
    print(result)
