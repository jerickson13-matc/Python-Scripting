#!/usr/bin/env python3
#Author:Jack Erickson
#Week 6 Argparse Assignment

import argparse
import sys

parser = argparse.ArgumentParser(description="This is arguments.py script.")

parser.add_argument('-m', metavar='Basic', help='Enter some text')
parser.add_argument('-i', '--interger', dest='varInteger', default=10, metavar='[an integer]', type=int, required=False, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', dest='varFloat', default=22.2, metavar='[a float]', type=float, help='Enter a simple float')
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default="hello", type=str, help='Enter a simple string')
parser.add_argument('-l', dest='varList', metavar='[String]', nargs='+', help='enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-True', default=False, action='store_true', dest='varbooltrue', help='Toggle from defualt False to True')
parser.add_argument('-f', '--setFalse', default=True, action='store_false', dest='varboolfalse', help='Toggle from default True to False')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0', help="Show program's version number and exit")

myargs = parser.parse_args()

if len(sys.argv) == 1:
    print(parser.print_help())
else:
    print('how')

print(myargs.varInteger)
print(myargs.varFloat)
print(myargs.varString)
print(myargs.varList)