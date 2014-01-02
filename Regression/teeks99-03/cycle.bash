rm loop_finished.log
while true
do
   cd boost_root-develop
   git pull
   cd ..

   #cd boost_root-master
   #git pull
   #cd ..

   for ver in a b
   do
      cd $ver
      ./start.bash
      cd ..
   done

   echo `date` >> loop_finished.log
done
