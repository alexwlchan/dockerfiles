FROM alpine

LABEL maintainer "Alex Chan <alex@alexwlchan.net>"

RUN apk update
RUN apk add ruby
RUN gem install --no-document uniscribe

ENTRYPOINT ["/usr/bin/uniscribe"]
