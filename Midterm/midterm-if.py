#!/usr/bin/env python3

#Author: Jack Erickson
#Midterm-if
print("Name:Jack Erickson")

Total = 0
line_number = -1

#keywords
key1 = "gmeach18@ed.gov"
key2 = "248.253.63.149"
key3 = "Whiteland"
key4 = "80.222.19.190"
key5 = "Kayley"
key6 = "dcassyqw@microsoft.com"

midtermfile = open("Midterm-if.txt", "r")
midtermread = midtermfile.readlines()

for line in midtermread:
    line_number += 1

    if key1 in line:
        Total += line_number
        line_number = -1 # line number = -1 becaue of the initial line in Midterm-if.txt, The total would be greater than 2425 if used the python line number.
        break

for line in midtermread:
    line_number += 1
    if key2 in line:
        Total += line_number
        line_number = -1
        break
    
for line in midtermread:
    line_number +=1
    if key3 in line:
        Total += line_number
        line_number = -1
        break

for line in midtermread:
    line_number +=1
    if key4 in line:
        Total += line_number
        line_number = -1
        break

for line in midtermread:
    line_number +=1
    if key5 in line:
        Total += line_number
        line_number = -1
        break

for line in midtermread:
    line_number +=1
    if key6 in line:
        Total += line_number
        line_number = -1
        break

midtermfile.close()

print(f" The total is: {Total}")