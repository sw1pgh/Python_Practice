class Even_or_Odd:
    def number_checker(self, num: int) -> str:
        if num == 0:
            return 'even'
        while (num != 0):
            if (num % 2 == 0):
                return 'even'
            else:
                return 'odd'
            
print(Even_or_Odd().number_checker(num = 66))