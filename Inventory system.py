def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def get_item_quantity(inventory, item_name):
    return inventory.get(item_name, "Item not found in inventory")

def total_inventory_quantity(inventory):
    return sum(inventory.values())

def display_inventory(inventory):
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    inventory = {}
    
    while True:
        print("\nInventory Management System")
        print("1. Add/Update Item")
        print("2. Retrieve Item Information")
        print("3. Display Total Quantity of All Items")
        print("4. Display All Inventory")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, item_name, quantity)
            print(f"Added/Updated {quantity} of {item_name} to the inventory.")
            
        elif choice == '2':
            item_name = input("Enter item name to retrieve: ")
            quantity = get_item_quantity(inventory, item_name)
            print(f"{item_name}: {quantity}")
        
        elif choice == '3':
            total_quantity = total_inventory_quantity(inventory)
            print(f"Total quantity of all items in inventory: {total_quantity}")
        
        elif choice == '4':
            display_inventory(inventory)
        
        elif choice == '5':
            print("Exiting the inventory management system.")
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
