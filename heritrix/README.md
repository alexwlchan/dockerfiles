# heritrix

This is a Docker image for running the [Heritrix web crawler][ia].

## Usage

```console
$ docker build -t heritrix .
$ mkdir jobs
$ docker run -d -p 8443:8443 -v $(pwd)/jobs:/usr/heritrix-3.2.0/jobs heritrix
```

To access the web interface, go to <http://localhost:8443> in your browser.
Username/password is `heritrix`/`heritrix`.

[ia]: https://webarchive.jira.com/wiki/display/Heritrix/Heritrix
