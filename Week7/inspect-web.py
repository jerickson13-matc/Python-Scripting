#!/usr/bin/env python3
#Author: Jack Erickson
#Week 7 Interacting with a website Assignment

import requests,bs4

res = requests.get("https://notpurple.com")
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text,features="html.parser")

for link in myHTML.find_all("a"):
    print(f"Links : {link.text}")