rm loop_finished.log
while true
do
   pushd boost_root
   git checkout develop
   git pull --recurse-submodules
   git submodule update --init
   git submodule update

   git checkout master
   git pull --recurse-submodules
   git submodule update --init
   git submodule update
   popd
	
   while read ver; do
      cd $ver
      ./start.bash
      cd ..
   done < version_dirs.txt

   echo `date` >> loop_finished.log
done
