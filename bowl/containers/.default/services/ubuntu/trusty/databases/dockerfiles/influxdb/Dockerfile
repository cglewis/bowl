FROM ubuntu:trusty
MAINTAINER Charlie Lewis

RUN apt-get update
RUN apt-get install -y wget
RUN wget http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb
RUN mkdir -p /opt/influxdb/shared/data && \
    dpkg -i /influxdb_latest_amd64.deb && \
    rm -rf /opt/influxdb/shared/data && \
    chown -R daemon:daemon /opt/influxdb

USER daemon
EXPOSE 8083 8086

ENTRYPOINT ["/usr/bin/influxdb"]
CMD ["-config=/opt/influxdb/shared/config.toml"]
