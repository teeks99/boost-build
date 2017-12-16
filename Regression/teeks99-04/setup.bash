# Before running: 
# Create user tomkent as sudo
# Create user boost
# Setup /dev/vda1 as /mnt/fs1, world 777
# Clone https://github.com/teeks99/boost-build to ~/
# Run this script from ~/boost-build/regression/teeks99-04

fallocate -l 4G /swap4g
chmod 600 /swap4g
mkswap /swap4g
swapon /swap4g
echo '/swap4g none swap sw 0 0' >> /etc/fstab

apt update

apt install -y software-properties-common

add-apt-repository -y ppa:git-core/ppa
apt-get update 
apt-get install -y \
  ca-certificates \
  byobu \
  vim \
  build-essential \
  git \
  wget \
  python2.7 \
  python2.7-dev \
  python3.5 \
  python3.5-dev \
  libbz2-dev \
  zlib1g-dev 

cd /usr/bin
ln -s python2.7 python

# Speed up fetch
git config --global submodule.fetchJobs 40

# Enable Compiler Repo
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test

# Install Tool
apt-get update
apt-get install -y gcc-7 g++-7

# User Config
cp user-config.jam ~/

# Setup Script
rsync -a ./ /mnt/fs1/teeks99-04/
chown -R boost:boost /mnt/fs1/teeks99-04

# Login as boost
#cd /mnt/fs1/teeks99-04 && git clone --recursive https://github.com/boostorg/boost boost_root
