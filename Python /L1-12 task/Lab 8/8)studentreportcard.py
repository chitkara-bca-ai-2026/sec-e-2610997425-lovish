print("=======================================================")
print("               SCHOOL RESULT PROCESSING SYSTEM          ")
print("=======================================================")


name = input("enter your name:")
rollno = int(input("enter your roll no."))

print("-------------student marks for 5 subjects (0-100)---------------")

sub1 = int(input("enter marks for subject 1: "))
sub2 = int(input("enter marks for subject 2: "))
sub3 = int(input("enter marks for subject 3: "))
sub4 = int(input("enter marks for subject 4: "))
sub5 = int(input("enter marks for subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100
if percentage >= 40 and percentage <= 100:
    result = "Pass"
else:
    result = "Fail"

if percentage >= 90:
    
    grade = "A+"    
elif percentage >= 80:
   
    grade = "A"
elif percentage >= 70:
   
    grade = "B"
elif percentage >= 60:
    
    grade = "C"
elif percentage >= 50:
    
    grade = "D"
else:
    
    grade = "E"   

if  grade == "A+":
    remark = "Outstanding"
elif grade == "A":
    remark = "Excellent"
elif grade == "B":
    remark = "Very Good"
elif grade == "C":
    remark = "Good"
elif grade == "D":
    remark = "Average"
else:
    remark = "Fail"

print("========================================================")
print("             STUDENT REPORT CARD                   ")
print("========================================================")

print("Student Name:", name)
print("Student Roll No.:", rollno)

print("------------------------------------------------")
print("TOTAL MARKS:", total)
print("PERCENTAGE:", percentage)
print("RESULT:", result)
print("GRADE:", grade)
print("REMARK:", remark)