A_example_set = {21, 34, 29}
B_example_set = {"Swap", "GG", 18}


A_example_set.add('290') # Adds 290 at the end of the Set

print(A_example_set)
print(f"{len(A_example_set)}")
print(f"{A_example_set.pop()}\n")

print(f"{A_example_set.union(B_example_set)}")
print(f"{A_example_set.intersection(B_example_set)}") # returns an empty set since nothing is common
