# Learning Type Hints

from typing import List, Tuple, Dict, Union

# List of Integers
li_1: List[int] = [1,5,7,8,90]

# Tuple of a string and an Integer
tu_1: Tuple[str, int] = ("Swap.GG", 1)

# Dictionary with Key->Str and Value->Int
dict_1: Dict[str, int] = {"Swap",1 , "GG",2}

# Union type for variables that can hold multiple values
identifier: Union[int, str] = "ID12212"
identifier = 12345 # This is also valid

a: int = 3
name: str = "Swap.GG"

def multiply(num_1: float, num_2: float) -> float:
    return (num_1 * num_2)

print(multiply(899.8374, 92839.8372))