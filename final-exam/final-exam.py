#!/usr/bin/env python3
#Author: Jack Erickson
#Final Exam Script

import argparse,requests,json,bs4,socket
from multiprocessing.sharedctypes import Value
from optparse import Values

parser = argparse.ArgumentParser(description='Allowing an IP Address to be entered')
parser.add_argument('-i', '--ipaddress', dest='varIP', type=str, required=True, help="Enter an IP Address.")
parser.add_argument('-q', '--question', dest='varQuestion', type=int, required=True, help="Enter the question # you want." )
myargs = parser.parse_args()

URL = f"http://{myargs.varIP}/q{myargs.varQuestion}"
print("Name: Jack Erickson")
print(URL)

#Function 1
if myargs.varQuestion == 1:
    get_response = requests.get(URL)
    print(f"ANSWER: {get_response.text}")

#Function 2
elif myargs.varQuestion == 2:
    parse_string = requests.get(URL)
    parse_string.raise_for_status()
    question2 = bs4.BeautifulSoup(parse_string.text,features="html.parser")
    message = question2.find("h2")
    secretmessage = message.text[7:32:3]
    print(f"ANSWER: {secretmessage} Jack")

#Function 3
elif myargs.varQuestion == 3:
    parse_header = requests.get(URL)
    print(f"ANSWER: {parse_header.headers['FINAL-HEADER']}")

#Function 4
elif myargs.varQuestion == 4:
    parse_json = requests.get(URL)
    Dictionary = dict("")
    Dictionary = json.loads(parse_json.text)
    for key in Dictionary["Music And Books"]:
        if key['title'] == "The Shining":
            print(f"ANSWER: {key['publish_info']['publish_year']}")


#Function 5
elif myargs.varQuestion == 5:
    socket_client = myargs.varIP
    print(socket_client)
    SND_DATA = "secret"
    RCV_DATA = ""
    RPORTS = range(5000, 7000)

    for RPORT in RPORTS:
        C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            C_SOCK.connect((socket_client, RPORT))
            C_SOCK.send(bytearray(SND_DATA, 'utf8'))
            RCV_DATA = C_SOCK.recv(1024)
            C_SOCK.close()
            print(f"ANSWER: {RCV_DATA.decode()[0:9:]}")
            print(f"Port: {RPORT}")
        except:
            C_SOCK.close()      


