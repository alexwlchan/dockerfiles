FROM alpine

LABEL maintainer "Alex Chan alex@alexwlchan.net"
LABEL description "A Docker image containing Pillow and its minimal dependencies"

RUN apk update
RUN apk add python py-pip

RUN apk add build-base jpeg-dev python-dev zlib-dev

RUN pip install Pillow
