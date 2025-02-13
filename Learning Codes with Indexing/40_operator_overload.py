class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):
        return self.n + num.n  # Operator being overloaded here 
    
n = Number(1)
m = Number(2)

print(f"m + n = {m + n}")