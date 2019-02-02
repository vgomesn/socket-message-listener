FROM centos:latest 

RUN yum update -y
RUN yum install python python-pip -y

RUN mkdir /opt/socketmessage
COPY *.py /opt/socketmessage/

ENTRYPOINT ["python","/opt/socketmessage/socket-server.py","--host:0.0.0.0"]


