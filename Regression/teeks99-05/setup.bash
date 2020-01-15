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
  byobu \
  vim \
  build-essential \
  git \
  wget \
  parted \
  python2.7 \
  python2.7-dev \
  python3.5 \
  python3.5-dev \
  libbz2-dev \
  zlib1g-dev 

# Setup work disk
mkdir /mnt/fs1
echo 'LABEL=BUILD /mnt/fs1 ext4 defaults 0 0' >> /etc/fstab
echo 'UUID=88a515e6-46e2-41ac-9a07-9ee6dcec9bb0 swap swap defaults 0 0' >> /etc/fstab

mount -a
chmod 777 /mnt/fs1

# Speed up fetch
git config --global submodule.fetchJobs 40

# Install Tool
apt-get update
apt-get install -y gcc-8 clang-9

# User Config
cp user-config.jam ~/
cp user-config.jam /home/boost

# Setup Script
rsync -aL ./ /mnt/fs1/teeks99-05/
chown -R boost:boost /mnt/fs1/teeks99-05

# Login as boost and run
