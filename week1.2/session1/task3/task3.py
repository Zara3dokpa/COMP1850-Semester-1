# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
bananaPos =fruit.index('banana')
print(f"Banana appears at index {bananaPos}")

# Display how many times "cherry" occurs
cherryNum =fruit.count('cherry')
print(f"Cherry appears {cherryNum} time(s)")

# Display how many times "strawberry" occurs
strawNum =fruit.count('strawberry')
print(f"Strawberry appears {strawNum} times")

# Unpack tuple into variables
(first,second,third)=fruit
print(first)
print(second)
print(third)