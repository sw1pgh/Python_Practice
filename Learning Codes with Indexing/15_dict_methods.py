marks = {
    "A": 19,
    "B": 12,
    "C":39
}

print(f"{marks.items()}")
print(f"{marks.keys()}")
marks.update({'A': 300, 'D':200})
print(f"{marks}")
print(f"{marks.get('D')}")

'''
Difference between:
1. print(marks.get('A'))  and,
2. print(marks['A'])

The main difference is that if 'A' does NOT exist in the dictionary, '1' returns 'None' as Output. However, '2' returns Error in the Code.

'''