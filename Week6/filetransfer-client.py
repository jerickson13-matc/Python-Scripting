#!/usr/bin/env python3
#Author: Jack Erickson
#Week 6 Networking (Sockets)

import socket

RHOST = "127.0.0.1"
RPORT = 5001

file = open("/etc/passwd", "r")
SND_DATA = file.read()
RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
C_SOCK.send(bytearray(SND_DATA, 'utf8'))

file.close()
