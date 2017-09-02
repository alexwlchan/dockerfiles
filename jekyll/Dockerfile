FROM alpine

LABEL maintainer "Alex Chan <alex@alexwlchan.net>"
LABEL description "A Docker image for Jekyll, the static site generator"

# Some links that were useful in getting 'gem install' to work:
#
#   - https://jekyllrb.com/docs/installation/
#   - https://github.com/ffi/ffi/issues/485
#
RUN apk update
RUN apk add build-base libffi-dev ruby ruby-dev ruby-irb ruby-rdoc

RUN gem install bundler jekyll

ENTRYPOINT ["/usr/bin/jekyll"]
