#!/usr/bin/env python3
#Author: Jack Erickson 
#Week7 Interacting with a Website Assignment

import requests

response = requests.get("https://notpurple.com")

with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)

