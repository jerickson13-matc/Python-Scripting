#!/usr/bin/env python3

#Author: Jack Erickson
#This is for the string formatting assignment

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print(f"Hello {varName}")
print(f"{varRed}-{varGreen}-{varBlue}")
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
print(f"My name is {varName.upper()}")
print(f"[++{varRed}++]")
print(f"[{varGreen.lower()}==]")
print(f"[*****{varBlue.lower()}]")
print(f"{varBlue}" * 10)
print(f"{varLoot}")
print(f"{varLoot: <.1f}")
print(f"I have ${varLoot: <.2f}")
print(f"[$$${varRed}$$$] [$${varGreen}$$$] [$$${varBlue}$$$]")
print(f"[   deR    ] [  {varGreen}   ] [   eulB   ]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")