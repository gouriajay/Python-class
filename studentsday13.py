filename = "students.txt"
try:
    with open(filename, "r") as file:
        existing_names = file.read()
        if existing_names:
            print("Existing student names:")
            print(existing_names)
        else:
            print("No existing student names.")
except FileNotFoundError:
    print("File does not exist. A new file will be created.")
n = int(input("How many student names do you want to add? "))
with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter student name {i+1}: ")
        file.write(name + "\n")
print("\nUpdated list of student names:")
with open(filename, "r") as file:
    print(file.read())
