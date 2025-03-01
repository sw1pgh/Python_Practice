# Store the multiplication table generated in prob_3.py in a file named Tables.txt

class Table_List_Comprehension:
    
    def __init__(self):
        self.n = int(input("Please enter any number to create a multiplication table: "))
        
    def table_list_generator(self):
        table = [self.n * i for i in range (1,11)]
        with open("Practice_Set_12/Tables.txt", 'w')as f:
            f.write(str(table))

    
Table_List_Comprehension().table_list_generator()