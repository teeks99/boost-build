rm loop_finished.log
while true
do
   #cd boost_root-develop
   #git pull --recurse-submodules
   #cd ..

   cd boost_root-master
   git pull
   cd ..

   for ver in a b c d e f g h i j
   do
      cd $ver
      ./start.bash
      cd ..
   done

   echo `date` >> loop_finished.log
done
