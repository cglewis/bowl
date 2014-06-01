FROM ubuntu:precise
MAINTAINER Charlie Lewis

# install java
RUN apt-get update && \
    apt-get install -y python-software-properties && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java7-installer

# install elasticsearch
RUN cd /tmp && \
    wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.1.tar.gz && \
    tar xvzf elasticsearch-1.1.1.tar.gz && \
    rm -f elasticsearch-1.1.1.tar.gz && \
    mv /tmp/elasticsearch-1.1.1 /elasticsearch

EXPOSE 9200 9300

CMD ["/elasticsearch/bin/elasticsearch"]

