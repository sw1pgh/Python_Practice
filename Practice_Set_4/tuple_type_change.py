# Python program to prove that tuples are immutable

def demonstrate_tuple_immutability():
    """Demonstrates that tuples are immutable in Python."""
    # Create a tuple
    my_tuple = (1, 2, 3, 4)
    print(f"Original tuple: {my_tuple}")

    # Attempt to modify an element of the tuple
    try:
        my_tuple[1] = 99  # This will raise a TypeError
    except TypeError as e:
        print(f"Error: {e}")

    # Verify that the tuple remains unchanged
    print(f"Tuple after attempted modification: {my_tuple}")

if __name__ == "__main__":
    demonstrate_tuple_immutability()