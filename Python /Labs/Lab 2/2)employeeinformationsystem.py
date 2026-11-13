name = input("enter employee name: ")
print(type(name))

id = input("enter employee id: ")
print(type(id))

salary = float(input("enter employee salary: "))
print(type(salary))

department = input("enter employee department: ")
print(type(department))

active = bool(input("is employee active? (yes/no): "))
print(type(active))

print("----- Employee Details -----")

print("Employee Name:", name)
print("Employee ID:", id)
print("Employee Salary:", salary)
print("Employee in Department:", department)
print(" Employee Active?:", active)
