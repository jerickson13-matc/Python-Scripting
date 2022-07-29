#!/usr/bin/env python3
#Author Jack Erickson
#Week 6 Assignment Networking (Sockets) 
import socket

RHOST = '127.0.0.1'
RPORT = 5000
SND_DATA = ""
RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

while 1:
    SND_DATA = input()
    C_SOCK.send(bytearray(SND_DATA,'utf8'))
    RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
    if SND_DATA == 'exit': break

C_SOCK.close()
