#!/usr/bin/env python3

# Author: Jack Erickson
# Week 4 Dictionaries Assignment

Mappings = {"server1.testlab.com":"192.168.1.10",
            "server2.testlab.com":"192.168.1.11",
            "server3.testlab.com":"192.168.1.12",
            "server4.testlab.com":"192.168.1.13",
            "server5.testlab.com":"192.168.1.14",
            "server6.testlab.com":"192.168.1.15",
            "server7.testlab.com":"192.168.1.16",
            "server8.testlab.com":"192.168.1.17"}

#Lists all FQDN's
print("FQDN's")
print(Mappings.keys())

#Lists all IP Adresses
print("\n IP Addresses")
print(Mappings.values())

#Lists all keys and values
print("\n Keys/Values")
print(Mappings.items())

#Checks for containment
print("\n Checks")
check1 = "server2.testlab.com"
check2 = "server10.testlab.com"

if check1 in Mappings:
    print(f"{check1} is contained")

if check2 in Mappings:
    print("how?")
else:
    print(f"{check2} isn't contained")





