import math

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def sum_of_odd_numbers(start, end):
    """Sum of odd numbers from start to end (inclusive)."""
    return sum(i for i in range(start + 1, end + 1) if i % 2 != 0)

def calculate_factorial(num):
    """Calculate the factorial of a number."""
    return math.factorial(num)
