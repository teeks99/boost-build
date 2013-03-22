rm loop_finished.log
while true
do
   cd boost-trunk
   svn up
   cd ..

   cd a
   ./multi_start.bash
   cd ..

   cd b
   ./multi_start.bash
   cd ..

   cd c
   ./multi_start.bash
   cd ..

   echo `date` >> loop_finished.log
done
