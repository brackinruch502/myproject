import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse using the Pythagorean theorem.
    
    Args:
    a (float): The first side length.
    b (float): The second side length.
    
    Returns:
    float: The length of the hypotenuse.
    """
    return math.sqrt(a**2 + b**2)

def main():
    # Example usage
    side_a = 5.0
    side_b = 7.0
    result = calculate_hypotenuse(side_a, side_b)
    
    print(f"The length of the hypotenuse is: {result:.2f}")

if __name__ == "__main__":
    main()
