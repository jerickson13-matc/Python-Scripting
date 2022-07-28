#!/usr/bin/env python3
#Author: Jack Erickson 
#Week 5 Subproccess assignment

#Part 1
import subprocess

CompletedProcess = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)

myProc = CompletedProcess.stdout

#Part 2:
myProcString = myProc.decode()

myProcList = myProcString.split('\n')

#Part 3:
for line in myProcList:
    print(line)

print(len(myProcList[1::1]))