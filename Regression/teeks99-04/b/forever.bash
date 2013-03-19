rm loop_finished.log
while true
do
   ./start.bash
   echo `date` >> loop_finished.log
done
