FROM ghcr.io/gsk-tech/cz_base-images/cz-python-builder:3.9.15-1.6.3
WORKDIR /usr/local/pyiohat
ENV PYTHONPATH=.
RUN useradd --create-home --shell /bin/bash -u 512 hdbapp

RUN apt-get update -y \
    &&  apt-get install -y \
    unzip \
    libaio1 \
    dumb-init

ADD requirements.txt .
ARG PIP_INDEX_URL
ARG PIP_EXTRA_INDEX_URL
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
ADD pyiohat .
ADD setup.py .
RUN python setup.py install




ENV PYTHONPATH="/usr/local//"
