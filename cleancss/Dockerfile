FROM alpine

LABEL maintainer "Alex Chan <alex@alexwlchan.net>"

RUN apk update
RUN apk add nodejs-npm
RUN npm install -g clean-css-cli
RUN which cleancss

ENTRYPOINT ["/usr/bin/cleancss"]
