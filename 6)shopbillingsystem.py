print("=======================================================")
print("             CLOTHING STORE BILLING SYSTEM                       ")
print("=======================================================")

custmrname = input("enter customer name:")
garmname = input("enter garment name:")
garmprice = float(input("enter garment price:"))
numgarments = int(input("enter number of garments:"))

print("========================================================")
print("                           BILL                           ")
print("========================================================")

print("Customer Name: ", custmrname)
print("Garment Name: ", garmname)   
print("Garment Price: ", garmprice)
print("quantity: ", numgarments)
print("Total amount: ", garmprice * numgarments)
