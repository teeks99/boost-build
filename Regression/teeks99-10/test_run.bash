update_repo ()
{
   pushd boost_root
   git checkout $1
   git pull
   git submodule update --init
   popd
   rsync -a --delete boost_root run/boost_root
}


while [ 1 ]
do 
   update_repo develop
   docker run -v /mnt/fs1/boost:/var/boost --rm -i -t teeks99/gcc-5.1 /bin/bash /var/boost/run/run_a.bash

   update_repo develop
   docker run -v /mnt/fs1/boost:/var/boost --rm -i -t teeks99/clang-3.6 /bin/bash /var/boost/run/run_b.bash
done
