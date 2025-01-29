# Create a class "Programmer" for storing information of few programmers at Microsoft.

class Programmer:
    
    name = ["Swap", "Sw1P", "sw1pgh"]
    company = "Microsoft"
    job_role = ["SDET", "QA", "SE"]

obj_prog = Programmer()

for i in range (0 , len(obj_prog.name)):
    print(f"")
    print(f"Name = {obj_prog.name[i]}\nCompany = {obj_prog.company}\nJob Role = {obj_prog.job_role[i]}")
    print("")