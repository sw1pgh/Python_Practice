# A list contains the multiplication table of 7. WAP to convert it to vertical string of same numbers

class Vertical_String:

    def conversion_logic(self):

        table_of_7 = [f"7 * {i} = {7 * i}" for i in range(1, 11)]

        print("The table of 7 presented vertically is:")

        output_string = "\n".join(table_of_7)

        return print(output_string)


Vertical_String().conversion_logic()