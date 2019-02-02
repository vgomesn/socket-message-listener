# Veronica Gomes
# File: socket-server.py (Python 3)
#
# Used reference code from these sources:
# Jesse Smith, Python Guide for the Total Beginner LiveLessons
# http://www.informit.com/articles/article.aspx?p=2234249
#
# Description:
# Socket server which listens forever (until kill/term signal) on port 28812 (configurable) for new messages coming from clients
# Upon arrival of a new message, it prints the timestamp the message arrived, the client's IP address, and the message itself
# 
# To run: python socket-server.py
#
# Sample client: socket-client.py
#
#


from socket import *
from time import ctime
HOST = 'localhost'
HOST = '0.0.0.0'
PORT = 28812
BUFSIZE = 1024
ADDR = (HOST, PORT)

serversock = socket(AF_INET,SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(50)

print("Server up and listening in port: ", PORT)
 
while True:
  print('Waiting for a client connection...')
  clientconn, addr = serversock.accept()
  print('Connection from client: ', addr)

  while True:
    data, addr = clientconn.recvfrom(BUFSIZE)
    if not data:
      break
    print("%s : MESSAGE RECEIVED FROM  %s : %s" % (ctime(), addr, data))

  clientconn.close()
serversock.close() 

