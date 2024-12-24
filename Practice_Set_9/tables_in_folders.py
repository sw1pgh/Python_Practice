def generate_Table(n):
    table = ""
    
    for i in range(1, 11):
        table +=  f"{n} X {i} = {n*i}\n"

    with open(f"Practice_Set_9/tables/table_{n}.txt", "w") as f:
        f.write(table)
        
    
for i in range(1, 21):
    generate_Table(i)