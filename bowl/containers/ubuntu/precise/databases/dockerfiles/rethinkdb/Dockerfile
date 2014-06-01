FROM ubuntu:precise

# install rethinkdb
RUN apt-get update && \
    apt-get install -y python-software-properties && \
    add-apt-repository -y ppa:rethinkdb/ppa && \
    apt-get update && \
    apt-get install -y rethinkdb

# define mountable directories
VOLUME ["/data"]

# define working directory
WORKDIR /data

EXPOSE 8080 28015 29015

# define default command
CMD ["rethinkdb", "--bind", "all"]

