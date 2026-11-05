for  i in range(1,8):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for  i in range(8,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()   
    

    rows = 5

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


   
for i in range(1, 6):
    for i in range(1, i + 1):
        print("*", end=" ")
    print()
