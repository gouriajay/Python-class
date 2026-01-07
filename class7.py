grocery_list=["Milk","bread","eggs"]
def add_item(item):
    grocery_list.append(item)
def remove_item():
    if grocery_list:
     grocery_list.pop()   
display_items = lambda items: [print(f"Item: {item}") for item in items]
def count_character(item):
    if not item:
        return 0
    return len(item[0]) +count_character(item[1:])
add_item("curd")
remove_item()
display_items(grocery_list)
total_characters=count_character(grocery_list)
print(total_characters)
    
      
   
