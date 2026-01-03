fruits=["Apple","Orange","Pineapple"]
vegetables=["Tomato","Cucumber","Cabbage"]
bevarages=["Water","Juice","Soda"]
print(fruits)
print(vegetables)
print(bevarages)

fruits.append("Grapes")
print(fruits)

vegetables.insert(2,"Carrot")
print(vegetables)

bevarages.pop()
print(bevarages)

inventory=[fruits,vegetables,bevarages]
print(inventory)

print(fruits[:2])

print(vegetables[-1])

length_fruits=[len(item) for item in fruits]
print(length_fruits)

if "Water" in bevarages:
    print("Yes,'Water' is in  bevarages")
    
else:
      print("NO,'Water' is not in bevarage")

create_tuple=(fruits[0],
              vegetables[0],
              bevarages[0],
              )
print(create_tuple)
