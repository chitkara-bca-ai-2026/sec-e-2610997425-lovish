print("=======================================================")
print("             ENGENEERING CALCULATION TOOL               ")
print("=======================================================")
numvalue = int(input("enter a numeric value: "))
expvalue = int(input("enter the exponent value: "))
decivalue = float(input("enter a decimal measurement: "))
powervalue = numvalue ** expvalue
squarevalue = numvalue ** 2
ceilvalue = round(decivalue)
floorvalue = int(decivalue)


print("--------------result------------")


print("value         : ", numvalue)
print("exponent      : ", expvalue)
print("power         : ", powervalue)
print("square        : ", squarevalue)
print("decimal value : ", decivalue)
print("ceil value    : ", ceilvalue)
print("floor value   : ", floorvalue)

print("=======================================")
