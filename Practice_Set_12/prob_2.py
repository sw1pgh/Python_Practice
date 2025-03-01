# WAP to print 3rd, 5th and 7th element from a list using enumerate function

list1 = [1,3,43,4111,35,4,6,5,76,8,8,6]

for index, i in enumerate(list1):
    if index == 2 or index == 4 or index == 6:
        print(f"The {index + 1} no. element is {i}")