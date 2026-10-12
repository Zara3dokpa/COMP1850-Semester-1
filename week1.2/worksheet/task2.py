# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers


numbers= read_numbers()
if (len(numbers)==0):
    sys.exit("Error: no numbers provided")

numbers.sort()

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
mean = sum(numbers)/len(numbers)
print(f"Mean = {mean}")

numbers.sort()
if (len(numbers)%2==1):
   midIndex=len(numbers)//2
   median=numbers[midIndex]
   print(f"Median = {median}")
elif (len(numbers)%2==0):
    index1=len(numbers)//2
    index2=index1-1
    median=(numbers[index1]+numbers[index2])/2
print(f"Median = {median}")