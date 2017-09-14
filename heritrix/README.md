# heritrix

This is a Docker image for running the [Heritrix web crawler][ia].

I was testing this for something (I don't remember what now), and it was more convenient to install it in Docker than try to run it locally.

## Usage

```console
$ docker build -t heritrix .
$ mkdir jobs
$ docker run -d -p 8443:8443 -v $(pwd)/jobs:/usr/heritrix-3.2.0/jobs heritrix
```

To access the web interface, go to <http://localhost:8443> in your browser.
Username/password is `heritrix`/`heritrix`.

[ia]: https://webarchive.jira.com/wiki/display/Heritrix/Heritrix
