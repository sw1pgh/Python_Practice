# write a list comprehension to print a list which contains the multiplication table of a user entered number

class Table_List_Comprehension:
    
    def __init__(self):
        self.n = int(input("Please enter any number to create a multiplication table: "))
        
    def table_list_generator(self):
        table = [self.n * i for i in range (1,11)]
        return print(table)
    
Table_List_Comprehension().table_list_generator()