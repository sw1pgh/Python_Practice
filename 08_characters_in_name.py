your_name = input("Please enter your name without any special character. However, you can use blank space: ")

character_count = 0

for i in your_name:
    if (i != " "):
        character_count +=1
    else:
        continue

print(f"The number of characters in {your_name} is: {character_count}")