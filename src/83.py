def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number to be added.
    b (int): The second number to be added.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

def calculate_derivative(f, x0, h):
    """
    Calculates the derivative of a function f at x0 using the forward difference method with step size h.
    
    Parameters:
    f (function): The function to differentiate.
    x0 (float): The point around which to calculate the derivative.
    h (float): The step size for the forward difference approximation.
    
    Returns:
    float: The value of the derivative at x0.
    """
    return (f(x0 + h) - f(x0)) / h

def square_root(n):
    """
    Calculates the square root of a given number n using the Newton-Raphson method.
    
    Parameters:
    n (float): The number to calculate the square root of.
    
    Returns:
    float: The approximate square root of n.
    """
    if n >= 1.0:
        return 1.0
    else:
        a = n - 1.0
        b = 2.0
        epsilon = 1e-6
        while abs(b - a) > epsilon:
            x1 = (a + b) / 2
            if x1 * x1 == n:
                return x1
            else:
                a, b = b, x1
