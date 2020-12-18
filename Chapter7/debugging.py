# Code to demonstate debugging techniques

big = input("enter a number")
small = input("enter a second number")

if small > big:
    small = big
    big = small

print("The bigger number is", big)
print("The smaller number is", small)
