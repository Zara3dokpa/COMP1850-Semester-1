import sys
# Worksheet 1.2: Task 1 Solution

grade = input("Enter an integer grade from 0 to 100: ")
if(grade.isdecimal()==False):
  sys.exit("Error: Grade must be an integer between 0 and 100")
  
grade = int(grade)

if(grade<0 or grade>100):
  sys.exit("Error: Grade must be an integer between 0 and 100")

if(grade<=39):
  print (f"{grade} is a Fail")
elif(grade>39 and grade<=69):
  print (f"{grade} is a Pass")
else:
  print (f"{grade} is a Distinction")