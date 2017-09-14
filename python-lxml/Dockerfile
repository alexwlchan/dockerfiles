FROM alpine

LABEL maintainer "Alex Chan alex@alexwlchan.net"
LABEL description "A Docker image containing Python 3, lxml and its dependencies"

RUN apk update
RUN apk add build-base libxml2-dev libxslt-dev python3 python3-dev
RUN pip3 install lxml
