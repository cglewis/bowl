FROM ubuntu:precise
MAINTAINER Charlie Lewis
RUN apt-get update
RUN apt-get install -y redis-server
EXPOSE 6379
CMD ["/usr/bin/redis-server"]
