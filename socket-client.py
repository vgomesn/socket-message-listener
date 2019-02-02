#
# Veronica Gomes
# File: socket-server.py (Python 3)
#
# Used reference code from these sources:
# Jesse Smith, Python Guide for the Total Beginner LiveLessons
# http://www.informit.com/articles/article.aspx?p=2234249
# 
# Description:
# Socket client is a client app that will connect to a socket-server running on localhost (configurable) on port 28812 (default)
# And then, it will prompt the user to enter new messages. Each message ends with the user pressing ENTER key
# The user can enter as many messages as they want. When done sending messages, the user can press ENTER (with no message) to exit the program.
# 

from socket import *
#HOST = '172.17.0.2'
HOST = '127.0.0.1'
PORT = 28812
BUFSIZE = 1024
ADDR = (HOST, PORT)

clientconn = socket(AF_INET, SOCK_STREAM)
clientconn.connect(ADDR)

print("Connected to socket server. Enter a message. Press ENTER to send. Empty message to exit this client.")

while True:
  data = input('Enter message > ')
  if not data:
      break
  clientconn.sendto(data.encode('utf-8'),ADDR)
  #data = clientconn.recv(BUFSIZE)
  #if not data:
  #    break
  #print(data)

clientconn.close()

