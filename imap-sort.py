#!/bin/python
from imapclient import IMAPClient
import sys,getpass
user = sys.argv[1:]

server = IMAPClient("imap.google.com",ssl=True)
server.login(user,getpass.getpass())
server.select_folder("inbox")
data = server.search("*")

data = server.fetch("ALL",['BODY[HEADER.FIELDS (SUBJECT FROM DATE)]'])
from_key = 'BODY[HEADER.FIELDS (FROM)]'

for key in data:
     string = data[key][akey]
     i1 = string.index("<")
     i2 = string.index(">")
     print string[i1+1:i2]

server.logout()
