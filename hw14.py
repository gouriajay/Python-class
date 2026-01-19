import random
import math
names_input = input("Enter customer names (comma-separated): ")
names_list = list(set([name.strip() for name in names_input.split(",")]))
random.shuffle(names_list)
if len(names_list) >= 2:
    winners = random.sample(names_list, 2)
else:
    winners = names_list 

winners_reversed = [winner[::-1] for winner in winners]


print("\n Lucky Draw Winners (reversed names)")
for i, winner in enumerate(winners_reversed, start=1):
    print(f"Winner {i}: {winner}")

num_participants = len(names_list)
print("\nTotal unique participants:", num_participants)

sqrt_participants = round(math.sqrt(num_participants))
print("Square root of participants (rounded):", sqrt_participants)
