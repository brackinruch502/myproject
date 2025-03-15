def generate_random_python(n):
    # Generate a random number between 1 and n
    rand_num = random.randint(1, n)

    # Create a list of numbers from 1 to n
    nums = list(range(1, n+1))

    # Remove the random number from the list
    nums.remove(rand_num)

    # Return the remaining number as the result
    return nums[0]
