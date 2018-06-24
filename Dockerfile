FROM ubuntu:18.04

LABEL maintainer swernst@gmail.com

RUN apt-get -y update

RUN apt-get -y install \
        libevent-dev \
        python3.6-dev \
        python3.6 \
        python3-pip && \
    python3.6 -m pip install \
        locustio==0.8

COPY ./run.py /run.py

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

ENTRYPOINT ["python3.6", "-u", "/run.py"]
