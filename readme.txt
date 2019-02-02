START CONTAINERIZED SERVICE, mapping port to local host (docker host): socket-message-listener
===========================

docker run -it -p 28812:28812 socket-message-listener

See below how to use the provided client program to interact with this service and send messages...


Dockerfile
----------

FROM centos:latest

RUN yum update -y
RUN yum install python python-pip -y

RUN mkdir /opt/socketmessage
COPY *.py /opt/socketmessage/

ENTRYPOINT ["python","/opt/socketmessage/socket-server.py","--host:0.0.0.0"]


docker build command
--------------------

docker build . -t socket-message-listener


Server code : socket-server.py (Python 3)
------------

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


CLIENT: Connects to port 28812 on local host (127.0.0.1) and sends messages to the server:
======

Client code : socket-client.py (Python 3)
-----------

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


Execution:
----------

# python socket-client.py
Connected to socket server. Enter a message. Press ENTER to send. Empty message to exit this client.
Enter message > hello
Enter message > how are you
Enter message > good and you
Enter message > good, thank you
Enter message > I gotta go
Enter message > ok
Enter message > see you later
Enter message > bye!
Enter message >
[root@vgomesvm socketmessage]#
[root@vgomesvm socketmessage]#

Meanwhile: Reaction to the messages by the service (docker container):
---------

# docker run -it -p 28812:28812 socket-message-listener
('Server up and listening in port: ', 28812)
Waiting for a client connection...
('Connection from client: ', ('172.17.0.1', 36172))
Fri Feb  1 20:34:18 2019 : MESSAGE RECEIVED FROM  None : hello
Fri Feb  1 20:34:20 2019 : MESSAGE RECEIVED FROM  None : how are you
Fri Feb  1 20:34:22 2019 : MESSAGE RECEIVED FROM  None : good and you
Fri Feb  1 20:34:25 2019 : MESSAGE RECEIVED FROM  None : good, thank you
Fri Feb  1 20:34:29 2019 : MESSAGE RECEIVED FROM  None : I gotta go
Fri Feb  1 20:34:31 2019 : MESSAGE RECEIVED FROM  None : ok
Fri Feb  1 20:34:33 2019 : MESSAGE RECEIVED FROM  None : see you later
Fri Feb  1 20:34:35 2019 : MESSAGE RECEIVED FROM  None : bye!
Waiting for a client connection...
#


