FROM ubuntu:trusty
MAINTAINER Thomas Kent <teeks99@yahoo.com>

# Enable PPA


# Install pre-reqs
RUN apt-get update && apt-get install -y \
 build-essential \
 git \
 wget \
 python2.7 \
 python2.7-dev \
 python3.4 \
 python3.4-dev \
 libbz2-dev \
 zlib1g-dev

# Install Tool
RUN apt-get update && apt-get install -y clang-3.6 

# Symlink tools


# Add the tool configs
ADD user-config.jam /
