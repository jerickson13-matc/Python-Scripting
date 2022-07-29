#!/usr/bin/env python3
#Author Jack Erickson
#Week 6 Networking (Sockets)

import socket

LHOST = ''
LPORT = 5001
RCV_DATA = ""

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while 1:
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print('Connected by ', addr)
    RCV_DATA = L_CONN.recv(1024)

    newfile = open("NewFile.txt", "w")

    str = repr(RCV_DATA)
    newfile.write("RCV_DATA = " + str)

    newfile.close()
    break
L_CONN.close()

f = open("NewFile.txt", "r")
fr = f.read()
print(fr)
f.close()
