#!/usr/bin/env python3
#Author Jack Erickson
#Second half of the week5 Assignment Functions

import f2c
input_temp = input("Input a \u00B0F temp to convert to \u00B0C: ")
Celsius = f2c.convert_temp(int(input_temp))

print(input_temp,"\u00B0F =", Celsius ,"\u00B0C")