#!/bin/python
from imapclient import IMAPClient
import sys,getpass
user = sys.argv[1:]

server = IMAPClient("imap.google.com",ssl=True)
server.login(user,getpass.getpass())
server.select_folder("inbox")
data = server.search("*")

data = server.fetch("1:*",['BODY[HEADER.FIELDS(SUBJECT FROM DATE)]'])
server.logout()
