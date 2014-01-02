rm loop_finished.log
while true
do
   cd boost-trunk
   svn up
   cd ..

   cd boost-release
   svn up
   cd ..

   cd a
   ./start.bash
   cd ..

   cd b
   ./start.bash
   cd ..

   cd c
   ./start.bash
   cd ..

   cd d
   ./start.bash
   cd ..

   cd e
   ./start.bash
   cd ..

   cd f
   ./start.bash
   cd ..

   cd g
   ./start.bash
   cd ..

   cd h
   ./start.bash
   cd ..

   cd m
   ./start.bash
   cd ..

   cd n
   ./start.bash
   cd ..

   cd o
   ./start.bash
   cd ..

   cd p
   ./start.bash
   cd ..

   cd q
   ./start.bash
   cd ..

   cd r
   ./start.bash
   cd ..

   cd s
   ./start.bash
   cd ..

   cd t
   ./start.bash
   cd ..


   echo `date` >> loop_finished.log
done
