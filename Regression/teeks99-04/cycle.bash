rm loop_finished.log
while true
do
   cd boost-trunk
   svn up
   cd ..

   cd boost-release
   svn up
   cd ..

   for ver in a b
   do
      cd $ver
      ./multi_start.bash
      cd ..
   done

   echo `date` >> loop_finished.log
done
