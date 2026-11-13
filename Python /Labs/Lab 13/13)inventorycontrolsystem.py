print("=============================")
print("INVENTORY CONTROL SYSTEM by LOVISH GOYAL")
print("=============================")
inventory=[]

while True:
    choice = int(input("choose one :\n1.add\n2.remove\n3.view\n4.sort\n5.exit\n"))

    if choice == "1":
        p = input("enter product name : ")
        inventory.append(p.title())
        print("product added successfully")

    elif choice == "2":
        p = input("enter product name : ")
        inventory.remove(p.title())
        print("product removed successfully")
        
    elif choice == "3":
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")
            
    elif choice == "4":
        inventory.sort()
        print("inventory sorted successfully")
        
    else:
        print("exiting the program")
        