rm output.log
echo Starting at: `date` > run_started.log

rsync -a ../boost-release/ boost/
source vars.bash

python run.py --runner=teeks99-09${id}-Ubuntu12.04-64 --toolsets=${tools} --force-update --tag=branches/release --bjam-options=-j2 --comment=../info.html 2>&1 | tee output.log

rm -rf boost/ results/
rm -rf /tmp/*.cpp

mv run_started.log last_run.log
echo Finished at: `date` >> last_run.log