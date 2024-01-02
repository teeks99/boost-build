# Before running: 
# Create user tomkent as sudo
# Create user boost
# Clone https://github.com/teeks99/boost-build to ~/
# Run this script from ~/boost-build/regression/teeks99-05

apt update

apt install -y software-properties-common

apt-get update 
apt-get install -y \
  ca-certificates \
  build-essential \
  git \
  wget \
  python3 \
  python3-dev \
  python3-numpy \
  libjpeg-dev \
  libpng-dev \
  libssl-dev \
  libtiff-dev \
  libbz2-dev \
  liblzma-dev \
  libicu-dev \
  libopenmpi-dev \
  zlib1g-dev \

# Setup work disk
#mkdir /mnt/fs1
#echo 'LABEL=BUILD /mnt/fs1 ext4 defaults 0 0' >> /etc/fstab
#echo 'UUID=88a515e6-46e2-41ac-9a07-9ee6dcec9bb0 swap swap defaults 0 0' >> /etc/fstab

#mount -a
#chmod 777 /mnt/fs1

# Speed up fetch
git config --global submodule.fetchJobs 40

# Install Tool
apt-get update
apt-get install -y gcc-13 g++-13
apt-get install -y clang-17 \
  clang-tools-17 \
  clang-format-17 \
  python3-clang-17 \
  libfuzzer-17-dev \
  lld-17 \
  libc++-17-dev \
  libc++abi-17-dev \
  libomp-17-dev \
  libunwind-17-dev \
  libpolly-17-dev \
  libclc-17-dev

# User Config
cp user-config.jam ~/
cp user-config.jam /home/boost/

# Setup Script
rsync -aL ./ /mnt/fs1/run/teeks99-01/
chown -R boost:boost /mnt/fs1/run/teeks99-01

# Login as boost and run
