import random

# Example of generating a random list of numbers between 1 and 50
random_list = random.sample(range(1, 51), random.randint(5, 20))  # Randomly sample 5 to 20 numbers between 1-50

print(random_list)
