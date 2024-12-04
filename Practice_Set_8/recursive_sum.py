# WAP in Python to create a recursive function to calculate the sum of first n natural numbers

def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)
    
if __name__ == "__main__":
    limit = int(input("Please enter the limit: "))
    print(f"Sum of first {limit} natural numbers is = {sum_natural(limit)}")