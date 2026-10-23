inventory = ['notebook', 'pen', 'eraser', 'ruler']

while True:
    choice = input("Choose one:\n1. Add item\n2. Remove item\n3. View inventory\n4. Exit\n")
    if choice == '1':
        p=input("Enter the item to add: ")
        inventory.append(p.title())
        print("added")
    elif choice==2:
        p=input("Enter the item to remove: ")
        if p.title() in inventory:
            inventory.remove(p.title())
            print("removed")
    elif choice == '3':
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")
    elif choice == '4':
       print("exiting...")
       break
    else:
        print("invalid inventory")