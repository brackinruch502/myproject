import numpy as np
import pandas as pd

def calculate_mean(data):
    """
    Calculate the mean of the given dataset.
    
    Args:
        data (list or array): The dataset containing numerical values.
        
    Returns:
        float: The mean value of the dataset.
    """
    return sum(data) / len(data)

# Example usage
data = [1, 2, 3, 4, 5]
mean_value = calculate_mean(data)
print(f"The mean value is: {mean_value}")
