print("=======================================================")
print("             ENGENEERING CALCULATION TOOL PROGRAM             ") 
print("=======================================================")
numvalue = int(input("Enter a Numeric Value: "))
expvalue = int(input("Enter the Exponent Value: "))
decivalue = float(input("Enter a Decimal Measurement: "))
powervalue = numvalue ** expvalue
squarevalue = numvalue ** 2
ceilvalue = round(decivalue)
floorvalue = int(decivalue)


print("--------------OUTPUT/RESULT------------")


print("value         : ", numvalue)
print("exponent      : ", expvalue)
print("power         : ", powervalue)
print("square        : ", squarevalue)
print("decimal value : ", decivalue)
print("ceil value    : ", ceilvalue)
print("floor value   : ", floorvalue)

print("=======================================")
