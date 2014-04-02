FROM ubuntu:saucy
MAINTAINER Charlie Lewis

RUN apt-get update
RUN apt-get install -y python-setuptools
RUN easy_install pip
ADD . /bowl
RUN cd /bowl; python setup.py install

ENTRYPOINT ["/usr/local/bin/bowl"]
CMD ["new"]
