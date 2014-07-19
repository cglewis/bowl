FROM ubuntu:trusty
MAINTAINER Charlie Lewis

# install rethinkdb
RUN apt-get update && \
    apt-get install -y python-software-properties && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:rethinkdb/ppa && \
    apt-get update && \
    apt-get install -y rethinkdb

EXPOSE 8080 28015 29015

# define default command
CMD ["rethinkdb", "--bind", "all"]

