print("--------------------------------------------------------------")
print("                DATA CONVERSION UTILITY PROGRAM               ")
print("--------------------------------------------------------------")

name = str(input("Enter Product Name: "))
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Product Quantity: "))
total = price * quantity
amount = str(total)


print("-------------------------------------------------------------")
print("               TYPE CASTING SUMMARY             ")
print("--------------------------------------------------------------")
print("name                value                  variable type")
print("-------------------------------------------------------------")
print("name                value                  variable type")
print("-------------------------------------------------------------")
print("name                ", name, "          ", type(name))
print("price               ", price,"          ",type(price))
print("quantity            ", quantity,"       ",type(quantity))
print("total               ", total, "         ",type(total))
print("amount              ", amount, "        ",type(amount))
print("---------------------------------------------------------------")

print("------------------------------------------------------------------")
print("               TEXT INVOICE/BILL SUMMARY               ")
print("------------------------------------------------------------------")
print("Product Name:", name)
print(" Price per unit:", price)
print("  Product Quantity:", quantity)
print("--------------------------------------------------------------")
print("Invoice Total: Rs.", amount)
print("=============================================================")




