#!/usr/bin/env python3

#Author: Jack Erickson
#Midterm - Slicing

print("Name: Jack Erickson\n")

with open("slicing-file.txt", "r") as slicingfile:
    slicinglist = slicingfile.readlines()
    a = slicinglist[-3]
    a2 = ''.join(a).replace('\n', ' ')

    b = slicinglist[2:5:1]
    b2 = ''.join(b).replace('\n', ' ')

    c = slicinglist[-10:-16:-2]
    c2 = ''.join(c).replace('\n', ' ')

    d = slicinglist[10:13:1]
    d2 = ''.join(d).replace('\n', ' ')

    e = slicinglist[-19:-22:-1]
    e2 = ''.join(e).replace('\n', ' ')

    quote = f"{a2}{b2}{c2}{d2}{e2}"
    print(quote)

slicingfile.close()