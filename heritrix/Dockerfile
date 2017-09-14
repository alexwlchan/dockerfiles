FROM alpine

LABEL maintainer "Alex Chan alex@alexwlchan.net"
LABEL description "A Docker image for running the Heritrix web crawler"

RUN apk update

# Java 7 instead of Java 8 because Heritrix has issues running under Java 7:
# https://kris-sigur.blogspot.co.uk/2014/10/heritrix-java-8-and-sunsecuritytoolskey.html
RUN apk add bash openjdk7-jre

RUN wget -O /tmp/heritrix.tar.gz http://builds.archive.org/maven2/org/archive/heritrix/heritrix/3.2.0/heritrix-3.2.0-dist.tar.gz
RUN tar -C /usr -xvf /tmp/heritrix.tar.gz

RUN keytool -keystore /usr/heritrix-3.2.0/adhoc.keystore -storepass password -keypass password -alias adhoc -genkey -keyalg RSA -dname "CN=Heritrix Ad-Hoc HTTPS Certificate" -validity 3650

EXPOSE 8443

COPY run.sh /run.sh

CMD ["/usr/heritrix-3.2.0/bin/heritrix", "--web-admin", "heritrix:heritrix", "--web-bind-hosts", "$(hostname -i)", "tail", "-f", "/usr/heritrix-3.2.0/heritrix_out.log"]
