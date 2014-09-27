FROM ubuntu:trusty
MAINTAINER Charlie Lewis
ENV GOPATH /usr/local/lib/go
RUN apt-get -y update
RUN apt-get -y install golang-go bzr git ca-certificates
RUN go get launchpad.net/godeb
RUN apt-get -y remove golang-go
RUN apt-get -y autoremove
RUN /usr/local/lib/go/bin/godeb install
