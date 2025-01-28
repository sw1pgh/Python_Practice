# Create a class "Programmer" for storing information of few programmers at Microsoft.

class Programmer:
    
    name = ["Swap", "Sw1P", "sw1pgh"]
    company = "Microsoft"
    job_role = ["SDET", "QA", "SE"]

obj_prog = Programmer()

n = len(obj_prog.name)

for i in range (0 , n):
    print(f"Name = {obj_prog.name[i]}\nCompany = {obj_prog.company}\nJob Role = {obj_prog.job_role[i]}")
    print("")