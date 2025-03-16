def random_code():
    import random

    # Generate a random number between 1 and 50
    num = random.randint(1, 50)

    # Check if the number is even or odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
