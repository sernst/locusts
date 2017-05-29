# Locusts Docker Image

The locusts docker image is designed for easily composing multi-container 
[locust.io](http://http://locust.io/) 
load testing swarms using Python 3.6. The locusts image functions can function
as either a master or slave depending on whether or not the _--master-host_ 
flag is specified in a container's run execution call.

The docker image is available in 
[Docker Hub](https://hub.docker.com/r/swernst/locusts/). You can pull the 
image with the command:

    $ docker pull swernst/locusts:latest

## Master & Slave

The optional _--master-host_ argument is used to specify that the container 
should be a slave and communicate with the master with the specified host.
For example:

    $ docker run -it --rm \
        -v ./scripts:/scripts \
        swernst/locusts \
        --master-host=127.0.0.1

would specify a slave container where the master resides at the local
`127.0.0.1` host location.

## Script Volume

A locusts container requires that a volume be mounted to the container's 
`/scripts` directory. It expects to find the _locustfile.py_ to run in that 
directory.

## Docker Compose

The multi-container environment is easily specified using docker compose. You 
can see an example in this repository of how that would look:
[docker-compose.yml](docker-compose.yml)
