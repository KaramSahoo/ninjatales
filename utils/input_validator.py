import argparse

def validate_positive_int(value):
    """
    Validates if the input value is a positive integer.
    
    Args:
        value: The input value to validate
        
    Returns:
        int: The validated positive integer
        
    Raises:
        argparse.ArgumentTypeError: If the value is not a positive integer
    """
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise ValueError
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")