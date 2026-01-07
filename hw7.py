inventory=[]

def add_item(item):
    inventory.append(item)
    
def count_items(item): 
    if not item:
        return 0
    return 1 + count_items(item[1:]) 

show_item=lambda item:print(f"Item in Stock:{item}") 
 
def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")
    
 
    for item in inventory:
        show_item(item)
    
    total=count_items(inventory)
    print(total)



main()        
