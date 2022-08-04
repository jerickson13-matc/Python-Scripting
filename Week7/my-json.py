#!/usr/bin/env python3
#Author: Jack Erickson
#Week 7 JSON assignment

import requests,json,argparse

parser = argparse.ArgumentParser(description='Allowing an IP Address to be entered')
parser.add_argument('-i', '--ipaddress', dest='varIP', help="Enter an IP Address.")
myargs = parser.parse_args()

json_raw = requests.get(f'http://ipinfo.io/{myargs.varIP}/json')

myDict = json.loads(json_raw.text)

for key in myDict:
    print(f"{key} : {myDict[key]}")
