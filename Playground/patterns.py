class Patterns:
    def pattern(self):
        n = int(input("Please enter the number of lines: "))
        for i in range(1, n + 1):
            print(" " * (n - i) + "* " * i)

Patterns().pattern()


# def pat(self):
#     n = int(input("Please enter the number of lines: "))
#     for i in range(1,n+1):
#             print("* " * i)
#             print("")