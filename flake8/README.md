# flake8

This is a Docker image for running the [flake8](https://pypi.org/project/flake8/) linting tool.

The entrypoint of the image is flake8 itself:

    $ docker run greengloves/flake8 --version
    3.4.1 (mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.5.0)

To run it over your own files, map your code into a volume in the container, and set that volume as the working directory. For example:

    $ docker run --volume $(pwd):/src --workdir /src greengloves/flake8
