#!/usr/bin/env python3

#Author Jack Erickson

#File Data Interactions Assignment week 3.

#Step 1

passwordfile = open("/etc/passwd", "r")
passwd = passwordfile.read()
passwordfile.close()
print(len(passwd))

print("len() function counts the amount of indiviual characters in the file")
print("You would use this read function over the other read functions when you want to do something with the entrie file all at once")

#Step 2

passwordfile = open("/etc/passwd", "r")
passwdlist = passwordfile.readlines()
print(len(passwdlist))
passwordfile.close()

print("The Len() function counts the amount of lines in the file")
print("You would use this read function to go through the file one line at a time")

#Step 3

with open("/etc/passwd", "r") as passwdlength:
    passwdline = passwdlength.read()
    while passwdline:
        print(len(passwdline))
        passwdline =passwdlength.readline()
print("You would use a loop and read function to go through a text file without haveing to write the same code over and over again")