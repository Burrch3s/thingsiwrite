#!/usr/bin/python
import socket

target_host = "www.google.com"
target_port = 80

#socket object
#        socket obj/module    std. ipv4/hostname tcp client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\nHost: google.com\n\n")

response = client.recv(4096)
print response
