print("=========================================================")
print("                 CALENDAR VERFICATION SYSTEM             ")
print("=========================================================")
year = int(input("ENTER YEAR = "))
print("---------------------------------------------------------")
print("YEAR =",year)

cyear=100
if year > 0:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("STATUS: LEAP YEAR")
        print("DAYS IN YEAR :366")
        print("FEBRURAY: 29 DAYS")
        print("REASON: DIVISIBLE BY 4 AND NOT A CENTURY YEAR")
        print("---------------------------------------------------------")
        
    else:
        print("all year are commmon years")
        print("STATUS :NOT A LEAP YEAR ")
else:
    print("error")
  