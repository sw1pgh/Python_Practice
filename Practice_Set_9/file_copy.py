with open("Practice_Set_9/og.txt", "r") as f:
    original_content = f.read()
    
with open("Practice_Set_9/copy.txt", "w") as f:
    f.write(original_content)