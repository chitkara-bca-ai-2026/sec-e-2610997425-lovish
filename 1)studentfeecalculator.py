ttnfees = (input("enter tution fees: "))
labfees = (input("enter lab fees: "))
libfees = (input("enter library fees: "))
examfee = (input("enter exam fees: "))
discamount = (input("enter discount amount: "))

totalfees = int(ttnfees) + int(labfees) + int(libfees) + int(examfee)
print("total fees:", totalfees)

feeafterdiscount = totalfees - int(discamount)
print("fee after discount:", feeafterdiscount)

annualfees = feeafterdiscount * 2
print("annual fees:", annualfees)

monthlyinstallment = annualfees/12
print("monthly installment:", monthlyinstallment)
