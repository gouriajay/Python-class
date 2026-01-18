item = input("Enter the name of a new item: ")
with open("items.txt", "a") as file:
    file.write(item + "\n")
print("\nFull list of items:")
with open("items.txt", "r") as file:
    for line in file:
        print(line.strip())
