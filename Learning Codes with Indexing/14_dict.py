marks = {
    "A": 19,
    "B": 12,
    "C":39
}
print(f"{marks}, {type(marks)}")
print(f"{marks['A']}") # We use dictionary because the time complexity is the least for dictionaries
# We could have done the same thing with List as well but the traversing/lookup will cost us much more time and the logic will be more complex