FROM phusion/baseimage
MAINTAINER Jignasha
 
ENV DEBIAN_FRONTEND noninteractive
 
RUN apt-get update
RUN apt-get install -y python python-pip python-dev 
RUN apt-get install -y libmysqlclient-dev
 
ADD . /app/src/
 
WORKDIR /app/src/inmar
RUN pip install -r requirements.txt
 
EXPOSE 3001
