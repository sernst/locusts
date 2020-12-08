# Locusts Docker Image

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-white)](https://gitlab.com/pycqa/flake8)
[![Code style: mypy](https://img.shields.io/badge/code%20style-mypy-white)](http://mypy-lang.org/)

The locusts docker image is designed for easily composing multi-container 
[locust.io](http://http://locust.io/) 
load testing swarms using Python 3.8+. The locusts image functions can function
as either a main or worker depending on whether or not the `--master-host` 
flag is specified in a container's run execution call.

The docker image is available in 
[Docker Hub](https://hub.docker.com/r/swernst/locusts/). You can pull the 
image with the command:

```bash
$ docker pull swernst/locusts:latest
```

## Main & Workers

The optional `--main-host` argument is used to specify that the container 
should be a worker and communicate with the main with the specified host.
For example:

```bash
$ docker run -it --rm \
    -v ./scripts:/scripts \
    swernst/locusts \
    --main-host=127.0.0.1
```

would specify a worker container where the main resides at the local
`127.0.0.1` host location.

## Script Volume

A locusts container requires that a volume be mounted to the container's 
`/scripts` directory. It expects to find the *locustfile.py* to run in that 
directory as well as a *locust.config.yaml* file.

Alternatively, this image can be used as a base image and the files copied
into the scripts directory of the built container image.

## Docker Compose

The multi-container environment is easily specified using docker compose. You 
can see an example in this repository of how that would look:
[docker-compose.yml](docker-compose.yml)
