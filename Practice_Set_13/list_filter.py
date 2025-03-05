# WAP to filter a list of numbers which are divisible by 5

class List_Filtration:
    
    def __init__(self):
        self.initial_list = []
        for i in range (1,11):
            self.user_input = int(input(f"Please enter {i}/10 number: "))
            self.initial_list.append(self.user_input)
    
    def div_by_5(self, n):
        if (n % 5) == 0:
            return True
        return False
    
    def filter_list_output(self):
        output = filter(self.div_by_5, self.initial_list)
        return print(f"Here is the filtered List with numbers divisible by 5:-\n{list(output)}")

List_Filtration().filter_list_output()