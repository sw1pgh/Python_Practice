class Patterns:
    
    def pattern_1(self):
        n = int(input("Please enter the number of lines: "))
        for i in range(1, n + 1):
            print(" " * (n - i) + "* " * i)

    def pattern_2(self):
        n = int(input("Please enter the number of lines: "))
        
        # Top half (straight)
        for i in range (1, n+1):
            print(" " * (n - i) + "* " * i)
            
        # Bottom half (reverse)
        for i in range(n - 1, 0, -1):
            print(" " * (n - i) + "* " * i)
            
    def pattern_3(self):
        n = int(input("Please enter the number of lines: "))
        for i in range(n, 0, -1):
            print("* " * i)

Patterns().pattern_3()