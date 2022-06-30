#!/usr/bin/env python3

#Author: Jack Erickson
#Week 2 Assignment - Data Types


varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]


print(f"{varString[3::]}")
print(f"{varString[0:3:1]}")
print(f"{varString[3:12:1]}")
print(f"{varString[::2]}")
print(f"{varString[::-1]}")


print(f"{varList[::-1]}")
print(f"{varList[-5::-1]}")
print(f"{varList[2:4:1]}")
print(f"{varList[::3]}")
print(f"{varList[1::1]}")


for element in varString:
    print(f"char: {element}")

for element in varList:
    print(f"char: {element}")