import random
import math
user_input=input("Enter a list of names of invited guests(comma-seperated)")
duplicate_names=[user_input.strip() for name in user_input.split(",")]
unique_names = list(set(duplicate_names))

selected_name = random.choice(unique_names)

reversed_name = selected_name[::-1]
count = len(unique_names)

rounded_sqrt = round(math.sqrt(count))

print("\n🎲 Selected Name:", selected_name)
print("🔁 Reversed Name:", reversed_name)
print("👥 Total Unique Names:", count)
print("🔢 Rounded Square Root:", rounded_sqrt)