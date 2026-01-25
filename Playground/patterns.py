class Patterns:
    def pattern(self):
        n = int(input("Please enter the number of lines: "))
        o = n
        for i in range(1,n+1):
            print("* " * o)
            o = o-1
        print("\n")

Patterns().pattern()