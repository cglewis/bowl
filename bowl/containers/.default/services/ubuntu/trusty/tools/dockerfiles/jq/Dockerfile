FROM ubuntu:trusty
RUN apt-get update
RUN apt-get install -y git make
RUN git clone https://github.com/stedolan/jq.git
WORKDIR jq
RUN make install
CMD [""]
# !! TODO

