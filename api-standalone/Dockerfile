#FROM ubuntu:16.04
FROM nvidia/cuda:8.0-runtime-ubuntu16.04
LABEL maintainer="Tony Lin"

ENV downloads /downloads
RUN apt update -y && apt upgrade -y && apt-get install -y \
    wget \
    unzip \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
    python-pip \
    python-dev \
    build-essential \
    cmake \
    pkg-config \ 
    libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev

RUN echo 'alias ll="ls -al --color"' >> ~/.bashrc

RUN mkdir -p $downloads && cd $downloads && curl -O https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh
WORKDIR $downloads
RUN bash Anaconda3-4.3.1-Linux-x86_64.sh -b -f -p ~/anaconda3 
ENV PATH "/root/anaconda3/bin:$PATH"
RUN /root/anaconda3/bin/conda create -f --name aoi_py3 python=3.6 

#Application Specific Python Libraries
RUN pip install scikit-image pandas gevent python-socketio gevent-websocket 

ENV PYTHONPATH="/app/lib:${PYTHONPATH}"
ENV LD_LIBRARY_PATH="/app/lib"

RUN mkdir -p /app/data/
VOLUME ["/app/lib"]
VOLUME ["/training"]
VOLUME ["/app/data"]

# Exposes this port from the docker container to the host machine
EXPOSE 8081

# Copy App Specific Artifacts - Most frequently fhanged files (such as main program) should go last 
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY src/static /app/static
COPY src/templates /app/templates
COPY src/lib /app/lib
COPY src/api_standalone.py /app
COPY doc/service-doc/html /app/static/

ENV __FLUSH_LOG 1

ENTRYPOINT "python" "/app/api_standalone.py"




