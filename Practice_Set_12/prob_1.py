# WAP to open 3 files 1.txt, 2.txt, 3.txt and if any of these files are not present,
# a message without exiting the program must be printed prompting the same


class Open_Files:
    def message_passing(self):
        try:
            open("1.txt", "r")
            open("2.txt", "r")
            open("3.txt", "r")
            
        except Exception as e:
            print(f"The files do NOT exist")


Open_Files().message_passing()