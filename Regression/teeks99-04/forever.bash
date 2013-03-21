rm loop_finished.log
while true
do
   ./multi_start.bash
   echo `date` >> loop_finished.log
done
