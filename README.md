# dockerfiles

This repo contains some of my useful Dockerfiles.

Some of them produce images that I run directly (for example, *flake8* or *travis*) to avoid having to install dependencies locally.
These are pushed to Docker Hub and can be accessed through `docker pull`.

Others serve as building blocks for bigger projects.
For example, I have some Dockerfiles for Python libraries with non-trivial dependencies.
When I need one of those dependencies in a project, I'll copy the relevant parts from the Dockerfile in this repo, rather than rederiving it from scratch.

## License

MIT.
